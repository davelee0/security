"""Email checks: who is allowed to send email as your domain?

Background, in one paragraph: email was designed with no proof of who
sent a message. Anyone can send mail that *says* it's from
office@yourparish.org. Three DNS records fix this together:

  * SPF   lists the servers allowed to send your mail.
  * DKIM  lets your provider sign each message, so receivers can verify it.
  * DMARC tells receivers what to do when a message fails those checks
          (nothing / spam folder / reject), and where to send reports.

Without DMARC enforcement, a scammer can email your parents or your
bookkeeper "from" you about a changed bank account or an unpaid tuition
invoice. That kind of impersonation fraud is where small organizations
lose the most money.

Everything here only reads public DNS records, the same lookups every
mail server in the world makes when it receives a message from you.
"""

from __future__ import annotations

from typing import Protocol

from .findings import Finding, Severity

AREA = "Email"


class LookupFailed(Exception):
    """DNS didn't answer (timeout, server failure). Not the same as 'no record'."""


class Resolver(Protocol):
    """What the checks need from DNS. Tests pass in a fake; the CLI passes
    a real one (see resolver.py). This is called dependency injection: it
    keeps the logic testable without network access."""

    def txt(self, name: str) -> list[str]: ...
    def mx(self, name: str) -> list[str]: ...
    def exists(self, name: str) -> bool: ...


# --- Which email provider? ---------------------------------------------------

GOOGLE = "Google Workspace"
MICROSOFT = "Microsoft 365"


def detect_provider(mx_hosts: list[str]) -> str | None:
    hosts = " ".join(h.lower() for h in mx_hosts)
    if "google.com" in hosts or "googlemail.com" in hosts:
        return GOOGLE
    if "outlook.com" in hosts:  # *.mail.protection.outlook.com
        return MICROSOFT
    return None


# Where to switch on DKIM, per provider. Click paths change over time, so
# these are kept short and point at the vendor's own help page wording.
DKIM_HOWTO = {
    GOOGLE: (
        "In the Google Admin console go to Apps > Google Workspace > Gmail > "
        "Authenticate email, generate a DKIM key, add the DNS record it shows "
        "you, then click 'Start authentication'. Google leaves this OFF by default."
    ),
    MICROSOFT: (
        "In the Microsoft Defender portal go to Email & collaboration > Policies "
        "& rules > Threat policies > Email authentication settings > DKIM, pick "
        "your domain, add the two CNAME records it shows, then enable signing."
    ),
}

# Common DKIM selector names. DKIM records live at
# <selector>._domainkey.<domain>, and there is no way to list selectors,
# so we can only try likely names. Not finding one proves nothing.
DKIM_SELECTORS = {
    GOOGLE: ["google"],
    MICROSOFT: ["selector1", "selector2"],
    None: ["default", "dkim", "k1", "s1", "s2", "mail", "selector1", "google"],
}


# --- MX -----------------------------------------------------------------------

def check_mx(domain: str, resolver: Resolver) -> tuple[list[Finding], list[str] | None]:
    """Returns findings plus the mail server names ([] = no email, None = unknown)."""
    try:
        hosts = resolver.mx(domain)
    except LookupFailed:
        return [Finding("mx.error", AREA, Severity.UNKNOWN,
                        "Couldn't look up where this domain receives email.",
                        fix="Try again later or from another network.")], None

    # A "null MX" (a single record pointing at ".") means "we never receive mail".
    real = [h for h in hosts if h.strip(".")]
    if not real:
        return [Finding(
            "mx.none", AREA, Severity.INFO,
            "This domain doesn't receive email.",
            why="Scammers can still send email pretending to be a domain that "
                "doesn't use email, so it's worth locking down anyway.",
            fix='Publish an SPF record of "v=spf1 -all" and a DMARC record of '
                '"v=DMARC1; p=reject" to say "nothing legitimate ever comes from here".',
        )], []

    provider = detect_provider(real)
    label = provider or "an email provider we didn't recognize"
    return [Finding("mx.provider", AREA, Severity.INFO,
                    f"Email for this domain is handled by {label}.")], real


# --- SPF ----------------------------------------------------------------------

def _spf_records(txts: list[str]) -> list[str]:
    out = []
    for t in txts:
        low = t.strip().lower()
        if low == "v=spf1" or low.startswith("v=spf1 "):
            out.append(t.strip())
    return out


# Mechanisms that cost a DNS lookup when a receiver evaluates SPF.
# The SPF standard (RFC 7208, section 4.6.4) caps these at 10. Go over and
# the whole record fails, which quietly breaks your email authentication.
# Careful: "a" must match exactly (or as "a:"/"a/"), or "all" would count too.
_LOOKUP_EXACT = {"a", "mx", "ptr"}
_LOOKUP_PREFIX = ("include:", "a:", "a/", "mx:", "mx/", "ptr:", "exists:", "redirect=")


def _costs_lookup(term: str) -> bool:
    return term in _LOOKUP_EXACT or term.startswith(_LOOKUP_PREFIX)


def count_spf_lookups(record: str, resolver: Resolver, _seen: set[str] | None = None,
                      _depth: int = 0) -> int:
    """Count DNS lookups an SPF record needs, following include:/redirect=."""
    seen = _seen if _seen is not None else set()
    total = 0
    for term in record.split()[1:]:
        term = term.lstrip("+-~?").lower()
        if not _costs_lookup(term):
            continue
        total += 1
        target = None
        if term.startswith("include:"):
            target = term[len("include:"):]
        elif term.startswith("redirect="):
            target = term[len("redirect="):]
        # Follow nested records, guarding against loops and macros (%{...}).
        if target and "%" not in target and target not in seen and _depth < 10:
            seen.add(target)
            try:
                nested = _spf_records(resolver.txt(target))
            except LookupFailed:
                nested = []
            if nested:
                total += count_spf_lookups(nested[0], resolver, seen, _depth + 1)
    return total


def check_spf(domain: str, resolver: Resolver, uses_email: bool = True) -> list[Finding]:
    try:
        records = _spf_records(resolver.txt(domain))
    except LookupFailed:
        return [Finding("spf.error", AREA, Severity.UNKNOWN,
                        "Couldn't look up your SPF record.")]

    if not records and not uses_email:
        return [Finding(
            "spf.missing", AREA, Severity.WORTH_DOING,
            "No SPF record on a domain that doesn't use email.",
            fix='Add "v=spf1 -all" so receivers know no server may send as this domain.',
        )]
    if not records:
        return [Finding(
            "spf.missing", AREA, Severity.FIX_FIRST,
            "No SPF record: nothing says which servers may send your email.",
            why="Without it, your real email is more likely to land in spam, "
                "and fake email using your name is harder to catch.",
            fix="Ask whoever manages your domain to add the SPF record your "
                "email provider recommends (Google and Microsoft each document theirs).",
        )]
    if len(records) > 1:
        return [Finding(
            "spf.multiple", AREA, Severity.FIX_FIRST,
            f"You have {len(records)} SPF records; there must be exactly one.",
            why="With more than one, receivers treat SPF as broken.",
            fix="Merge them into a single record that lists every service that "
                "sends email for you (e.g. your email provider plus your newsletter tool).",
        )]

    record = records[0]
    findings: list[Finding] = []
    terms = [t.lower() for t in record.split()[1:]]
    all_term = next((t for t in terms if t.endswith("all") and t.lstrip("+-~?") == "all"), None)
    has_redirect = any(t.startswith("redirect=") for t in terms)

    if all_term in ("+all", "all"):
        findings.append(Finding(
            "spf.pass_all", AREA, Severity.FIX_FIRST,
            'Your SPF record ends in "+all", which allows ANY server to send as you.',
            fix='Change the ending to "~all" (or "-all" once you are sure the list is complete).',
        ))
    elif all_term == "?all" or (all_term is None and not has_redirect):
        findings.append(Finding(
            "spf.weak_all", AREA, Severity.WORTH_DOING,
            "Your SPF record doesn't say what to do with unlisted servers.",
            fix='End the record with "~all" (soft fail) or "-all" (hard fail).',
        ))
    else:
        findings.append(Finding("spf.ok", AREA, Severity.GOOD,
                                "You have one SPF record with a sensible ending.",
                                why=f"Record: {record}"))

    lookups = count_spf_lookups(record, resolver)
    if lookups > 10:
        findings.append(Finding(
            "spf.too_many_lookups", AREA, Severity.FIX_FIRST,
            f"Your SPF record needs {lookups} DNS lookups; the limit is 10.",
            why="Past 10, receivers treat SPF as broken, so it silently stops helping you.",
            fix="Remove services that no longer send email for you. If you still "
                "need them all, ask your provider about SPF 'flattening'.",
        ))
    return findings


# --- DMARC ----------------------------------------------------------------------

def parse_tags(record: str) -> dict[str, str]:
    """'v=DMARC1; p=none; rua=mailto:x' -> {'v': 'DMARC1', 'p': 'none', ...}"""
    tags = {}
    for part in record.split(";"):
        if "=" in part:
            k, v = part.split("=", 1)
            tags[k.strip().lower()] = v.strip()
    return tags


def check_dmarc(domain: str, resolver: Resolver) -> list[Finding]:
    try:
        txts = resolver.txt(f"_dmarc.{domain}")
    except LookupFailed:
        return [Finding("dmarc.error", AREA, Severity.UNKNOWN,
                        "Couldn't look up your DMARC record.")]

    records = [t.strip() for t in txts if t.strip().lower().startswith("v=dmarc1")]
    if not records:
        return [Finding(
            "dmarc.missing", AREA, Severity.FIX_FIRST,
            "No DMARC record: scammers can send email that appears to come from you.",
            why="This is how 'please update our bank details' and fake tuition "
                "invoices reach parents, staff and vendors looking like they came from you.",
            fix='Start with "v=DMARC1; p=none; rua=mailto:<an address you read>" '
                "at _dmarc.<your domain>, watch the reports for a few weeks, then "
                "move to p=quarantine and finally p=reject.",
        )]
    if len(records) > 1:
        return [Finding("dmarc.multiple", AREA, Severity.FIX_FIRST,
                        f"You have {len(records)} DMARC records; receivers ignore all of them.",
                        fix="Delete all but one.")]

    tags = parse_tags(records[0])
    policy = tags.get("p", "").lower()
    findings: list[Finding] = []

    if policy not in ("none", "quarantine", "reject"):
        return [Finding("dmarc.invalid", AREA, Severity.FIX_FIRST,
                        "Your DMARC record has no valid policy (p=), so it does nothing.",
                        why=f"Record: {records[0]}",
                        fix="Set p=none, p=quarantine or p=reject.")]
    if policy == "none":
        findings.append(Finding(
            "dmarc.p_none", AREA, Severity.WORTH_DOING,
            "DMARC is in monitoring mode (p=none): fake email is reported but still delivered.",
            why="p=none is the right first step, but it doesn't protect anyone yet.",
            fix="Once your reports show your real email passing, change to "
                "p=quarantine, then p=reject.",
        ))
    else:
        findings.append(Finding("dmarc.enforced", AREA, Severity.GOOD,
                                f"DMARC is enforced (p={policy}): fake email using your "
                                "domain gets blocked or sent to spam."))
        pct = tags.get("pct", "100")
        if pct.isdigit() and int(pct) < 100:
            findings.append(Finding(
                "dmarc.partial", AREA, Severity.INFO,
                f"DMARC applies to only {pct}% of failing email (pct={pct}).",
                fix="Raise pct to 100 when you're comfortable.",
            ))

    if "rua" not in tags:
        findings.append(Finding(
            "dmarc.no_reports", AREA, Severity.INFO,
            "DMARC reports aren't being sent anywhere (no rua=).",
            why="Reports show who is sending email as you, including services "
                "you forgot about and anyone impersonating you.",
            fix="Add rua=mailto:<address>. The raw reports are hard to read; "
                "free report-reading services exist and are worth using.",
        ))
    return findings


# --- DKIM -----------------------------------------------------------------------

def check_dkim(domain: str, resolver: Resolver, provider: str | None) -> list[Finding]:
    found, failures = [], 0
    selectors = DKIM_SELECTORS.get(provider, DKIM_SELECTORS[None])
    for sel in selectors:
        try:
            txts = resolver.txt(f"{sel}._domainkey.{domain}")
        except LookupFailed:
            failures += 1
            continue
        if any("p=" in t.lower() or "v=dkim1" in t.lower() for t in txts):
            found.append(sel)

    if found:
        return [Finding("dkim.found", AREA, Severity.GOOD,
                        f"DKIM signing is set up (selector: {', '.join(found)}).")]
    if failures == len(selectors):
        return [Finding("dkim.error", AREA, Severity.UNKNOWN, "Couldn't look up DKIM records.")]

    if provider in DKIM_HOWTO:
        # We know exactly which selector this provider uses, so absence is
        # meaningful: DKIM almost certainly isn't switched on.
        return [Finding(
            "dkim.missing", AREA, Severity.WORTH_DOING,
            f"DKIM signing doesn't appear to be switched on in {provider}.",
            why="DKIM is a digital signature on your email. DMARC can't be safely "
                "enforced without it, and big providers increasingly expect it.",
            fix=DKIM_HOWTO[provider],
        )]
    return [Finding(
        "dkim.unknown", AREA, Severity.INFO,
        "Couldn't confirm DKIM (this tool can only guess common record names).",
        fix="Ask your email provider whether DKIM signing is on for your domain.",
    )]


# --- All email checks -------------------------------------------------------------

def run_email_checks(domain: str, resolver: Resolver) -> list[Finding]:
    # Sanity check first. If DNS says the domain itself doesn't exist, every
    # record would look "missing". That happens with a typo, but also on
    # networks that intercept DNS (some captive portals, filters, sandboxes).
    # Reporting a page of false alarms would be worse than reporting nothing.
    try:
        exists = resolver.exists(domain)
    except LookupFailed:
        exists = True  # let the individual checks report what they can
    if not exists:
        return [Finding(
            "dns.no_domain", AREA, Severity.UNKNOWN,
            f"DNS says {domain} doesn't exist, so the email checks were skipped.",
            why="Either the domain is misspelled, or this network is blocking or "
                "rewriting DNS lookups.",
            fix="Check the spelling, or try again from a different network "
                "(for example, a phone hotspot).",
        )]

    findings, mx_hosts = check_mx(domain, resolver)
    # If the MX lookup failed (None) we assume the domain uses email, the safer default.
    findings += check_spf(domain, resolver, uses_email=mx_hosts is None or bool(mx_hosts))
    findings += check_dmarc(domain, resolver)
    if mx_hosts:  # DKIM only matters if the domain actually sends/receives mail
        findings += check_dkim(domain, resolver, detect_provider(mx_hosts))
    return findings
