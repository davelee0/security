"""Command line: python -m checkup yourparish.org"""

from __future__ import annotations

import argparse
import re
import sys
from urllib.parse import urlparse

from .email_checks import run_email_checks
from .findings import Severity
from .report import to_json, to_markdown
from .web_checks import UrllibFetcher, run_web_checks

# Letters, digits and hyphens in dot-separated labels, ending in a letter TLD.
_DOMAIN = re.compile(r"^(?=.{1,253}$)([a-z0-9]([a-z0-9-]{0,61}[a-z0-9])?\.)+[a-z]{2,63}$")


def normalize_domain(raw: str) -> str:
    """Accept what people actually paste: 'https://www.Parish.org/about' -> 'parish.org'."""
    text = raw.strip().lower()
    if "://" in text:
        text = urlparse(text).hostname or ""
    text = text.split("/")[0].rstrip(".")
    if text.startswith("www."):
        text = text[4:]
    try:
        text = text.encode("idna").decode("ascii")  # handles non-ASCII domain names
    except UnicodeError:
        pass
    if not _DOMAIN.match(text):
        raise ValueError(f"'{raw}' doesn't look like a domain name (e.g. stmarys.org)")
    return text


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(
        prog="checkup",
        description="A plain-language check of a domain's public email and website "
                    "security settings. Reads public DNS and loads the homepage; "
                    "nothing more.",
        epilog="Exit code is 1 if anything is marked 'Fix first', so this can be "
               "run on a schedule to catch regressions.",
    )
    parser.add_argument("domain", help="your organization's domain, e.g. stmarys.org")
    parser.add_argument("--json", action="store_true", help="output JSON instead of a report")
    parser.add_argument("--no-web", action="store_true", help="skip the website checks")
    parser.add_argument("--website", metavar="DOMAIN",
                        help="check the website at a different domain than the email domain")
    args = parser.parse_args(argv)

    try:
        domain = normalize_domain(args.domain)
        website = normalize_domain(args.website) if args.website else domain
    except ValueError as e:
        parser.error(str(e))

    # Imported here so `--help` works even before dnspython is installed.
    from .resolver import DnsResolver

    findings = run_email_checks(domain, DnsResolver())
    if not args.no_web:
        findings += run_web_checks(website, UrllibFetcher())

    print(to_json(domain, findings) if args.json else to_markdown(domain, findings))
    return 1 if any(f.severity is Severity.FIX_FIRST for f in findings) else 0


if __name__ == "__main__":
    sys.exit(main())
