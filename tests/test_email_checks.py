"""Email checks, tested against a fake DNS so no network is needed.

Each test builds a tiny DNS "zone" as a dict and asserts which finding ids
come out. Reading these is also a quick way to learn what each check does.
"""

import pytest

from checkup.email_checks import (
    LookupFailed,
    count_spf_lookups,
    detect_provider,
    run_email_checks,
)
from checkup.findings import Severity


class FakeResolver:
    def __init__(self, txt=None, mx=None, failing=(), nonexistent=()):
        self._txt = txt or {}
        self._mx = mx or {}
        self._failing = set(failing)  # names whose lookup should time out
        self._nonexistent = set(nonexistent)  # names DNS says don't exist

    def exists(self, name):
        return name not in self._nonexistent

    def txt(self, name):
        if name in self._failing:
            raise LookupFailed(name)
        return self._txt.get(name, [])

    def mx(self, name):
        if name in self._failing:
            raise LookupFailed(name)
        return self._mx.get(name, [])


D = "stmarys.org"
GOOGLE_MX = {D: ["aspmx.l.google.com."]}


def ids(findings):
    return {f.check for f in findings}


def by_id(findings, check):
    return next(f for f in findings if f.check == check)


def test_well_configured_google_domain_is_all_good():
    r = FakeResolver(
        mx=GOOGLE_MX,
        txt={
            D: ["v=spf1 include:_spf.google.com ~all"],
            f"_dmarc.{D}": ["v=DMARC1; p=reject; rua=mailto:dmarc@stmarys.org"],
            f"google._domainkey.{D}": ["v=DKIM1; k=rsa; p=MIIBIjAN..."],
        },
    )
    findings = run_email_checks(D, r)
    assert {"spf.ok", "dmarc.enforced", "dkim.found"} <= ids(findings)
    assert not [f for f in findings if f.severity in (Severity.FIX_FIRST, Severity.WORTH_DOING)]


def test_typical_unprotected_parish():
    # The most common real-world picture: Google Workspace, nothing configured.
    findings = run_email_checks(D, FakeResolver(mx=GOOGLE_MX))
    assert by_id(findings, "spf.missing").severity is Severity.FIX_FIRST
    assert by_id(findings, "dmarc.missing").severity is Severity.FIX_FIRST
    dkim = by_id(findings, "dkim.missing")
    assert dkim.severity is Severity.WORTH_DOING
    assert "Google Admin console" in dkim.fix  # provider-specific instructions


def test_dmarc_monitoring_only_and_no_reports():
    r = FakeResolver(mx=GOOGLE_MX, txt={f"_dmarc.{D}": ["v=DMARC1; p=none"]})
    found = ids(run_email_checks(D, r))
    assert {"dmarc.p_none", "dmarc.no_reports"} <= found


def test_dmarc_without_policy_is_invalid():
    r = FakeResolver(txt={f"_dmarc.{D}": ["v=DMARC1; rua=mailto:x@y.org"]})
    assert "dmarc.invalid" in ids(run_email_checks(D, r))


def test_dmarc_partial_pct():
    r = FakeResolver(txt={f"_dmarc.{D}": ["v=DMARC1; p=quarantine; pct=25; rua=mailto:a@b.org"]})
    assert {"dmarc.enforced", "dmarc.partial"} <= ids(run_email_checks(D, r))


def test_two_spf_records_is_broken():
    r = FakeResolver(mx=GOOGLE_MX, txt={D: ["v=spf1 include:_spf.google.com ~all",
                                            "v=spf1 include:mailchimp.com ~all"]})
    assert "spf.multiple" in ids(run_email_checks(D, r))


def test_spf_ignores_unrelated_txt_records():
    r = FakeResolver(mx=GOOGLE_MX, txt={D: ["google-site-verification=abc",
                                            "v=spf1 include:_spf.google.com -all"]})
    assert "spf.ok" in ids(run_email_checks(D, r))


@pytest.mark.parametrize("record,expected", [
    ("v=spf1 include:_spf.google.com +all", "spf.pass_all"),
    ("v=spf1 include:_spf.google.com all", "spf.pass_all"),
    ("v=spf1 include:_spf.google.com ?all", "spf.weak_all"),
    ("v=spf1 include:_spf.google.com", "spf.weak_all"),
    ("v=spf1 redirect=_spf.example.net", "spf.ok"),
])
def test_spf_all_mechanism(record, expected):
    r = FakeResolver(mx=GOOGLE_MX, txt={D: [record]})
    assert expected in ids(run_email_checks(D, r))


def test_spf_lookup_count_follows_includes_and_ignores_all():
    r = FakeResolver(txt={
        "a.example": ["v=spf1 include:b.example mx ~all"],  # 2 lookups
        "b.example": ["v=spf1 ip4:192.0.2.0/24 a -all"],     # 1 lookup
    })
    # include:a.example (1) + a.example's 2 + b.example's 1 = 4. "~all" costs nothing.
    assert count_spf_lookups("v=spf1 include:a.example ~all", r) == 4


def test_spf_lookup_count_survives_include_loops():
    r = FakeResolver(txt={"loop.example": ["v=spf1 include:loop.example ~all"]})
    assert count_spf_lookups("v=spf1 include:loop.example ~all", r) == 2


def test_spf_over_ten_lookups():
    includes = " ".join(f"include:s{i}.example" for i in range(11))
    r = FakeResolver(mx=GOOGLE_MX, txt={D: [f"v=spf1 {includes} ~all"]})
    assert by_id(run_email_checks(D, r), "spf.too_many_lookups").severity is Severity.FIX_FIRST


def test_domain_without_email_gets_lockdown_advice():
    findings = run_email_checks(D, FakeResolver(mx={D: ["."]}))  # null MX
    assert "mx.none" in ids(findings)
    assert by_id(findings, "spf.missing").severity is Severity.WORTH_DOING
    assert "dkim.missing" not in ids(findings)


def test_failed_lookups_are_unknown_not_missing():
    # The key honesty property: a timeout must never be reported as "missing".
    r = FakeResolver(failing={D, f"_dmarc.{D}"})
    findings = run_email_checks(D, r)
    assert {"mx.error", "spf.error", "dmarc.error"} <= ids(findings)
    assert "dmarc.missing" not in ids(findings)
    assert "spf.missing" not in ids(findings)


def test_unknown_provider_dkim_is_only_info():
    r = FakeResolver(mx={D: ["mx1.smallhost.net."]})
    assert by_id(run_email_checks(D, r), "dkim.unknown").severity is Severity.INFO


@pytest.mark.parametrize("mx,expected", [
    (["aspmx.l.google.com."], "Google Workspace"),
    (["stmarys-org.mail.protection.outlook.com."], "Microsoft 365"),
    (["mx.zoho.com."], None),
])
def test_detect_provider(mx, expected):
    assert detect_provider(mx) == expected


def test_nonexistent_domain_stops_instead_of_false_alarms():
    # Seen for real: a network that answers "no such domain" for everything
    # made every record look missing. We must not report that as findings.
    findings = run_email_checks(D, FakeResolver(nonexistent={D}))
    assert ids(findings) == {"dns.no_domain"}
    assert findings[0].severity is Severity.UNKNOWN


def test_subdomain_inherits_parent_dmarc():
    sub = "school.stmarys.org"
    r = FakeResolver(txt={f"_dmarc.{D}": ["v=DMARC1; p=reject; rua=mailto:a@stmarys.org"]})
    assert "dmarc.enforced" in ids(run_email_checks(sub, r))
    assert "dmarc.missing" not in ids(run_email_checks(sub, r))


def test_subdomain_own_dmarc_wins_over_parent():
    sub = "school.stmarys.org"
    r = FakeResolver(txt={f"_dmarc.{sub}": ["v=DMARC1; p=none; rua=mailto:a@stmarys.org"],
                          f"_dmarc.{D}": ["v=DMARC1; p=reject"]})
    assert "dmarc.p_none" in ids(run_email_checks(sub, r))


def test_open_subdomain_policy_is_flagged():
    r = FakeResolver(mx=GOOGLE_MX,
                     txt={f"_dmarc.{D}": ["v=DMARC1; p=reject; sp=none; rua=mailto:a@stmarys.org"]})
    f = by_id(run_email_checks(D, r), "dmarc.subdomains_open")
    assert f.severity is Severity.WORTH_DOING
    assert "sp=reject" in f.fix


def test_matching_subdomain_policy_is_fine():
    r = FakeResolver(mx=GOOGLE_MX,
                     txt={f"_dmarc.{D}": ["v=DMARC1; p=quarantine; sp=quarantine; rua=mailto:a@stmarys.org"]})
    assert "dmarc.subdomains_open" not in ids(run_email_checks(D, r))
