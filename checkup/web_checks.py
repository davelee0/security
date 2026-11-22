"""Website checks: is your site served safely?

What this sends: at most a few ordinary page requests to your homepage,
exactly what a browser does when someone visits. No scanning, no probing
for admin pages, no guessing at files. That keeps it in the same category
as "visiting the website", which matters: we only look at what the site
openly shows every visitor.
"""

from __future__ import annotations

import re
import socket
import ssl
import urllib.error
import urllib.request
from dataclasses import dataclass, field
from datetime import datetime, timezone
from typing import Protocol

from .findings import Finding, Severity

AREA = "Website"
USER_AGENT = "checkup/0.1 (security self-check; https://github.com/davelee0/security)"


@dataclass
class Response:
    status: int
    url: str
    headers: dict[str, str] = field(default_factory=dict)  # keys lower-cased
    body: str = ""


class FetchFailed(Exception):
    def __init__(self, message: str, cert_problem: bool = False):
        super().__init__(message)
        self.cert_problem = cert_problem


class Fetcher(Protocol):
    def get(self, url: str, follow_redirects: bool = True) -> Response: ...
    def cert_expiry(self, host: str) -> datetime: ...


# --- Real implementation (standard library only) -----------------------------

class _NoRedirect(urllib.request.HTTPRedirectHandler):
    def redirect_request(self, *args, **kwargs):
        return None  # makes urllib hand us the 3xx response instead of following it


class UrllibFetcher:
    def __init__(self, timeout: float = 10.0):
        self.timeout = timeout

    def get(self, url: str, follow_redirects: bool = True) -> Response:
        handlers = [] if follow_redirects else [_NoRedirect()]
        opener = urllib.request.build_opener(*handlers)
        req = urllib.request.Request(url, headers={"User-Agent": USER_AGENT})
        try:
            with opener.open(req, timeout=self.timeout) as r:
                body = r.read(200_000).decode("utf-8", "replace")
                return Response(r.status, r.geturl(), _lower(r.headers), body)
        except urllib.error.HTTPError as e:  # 3xx (when not following), 4xx, 5xx
            return Response(e.code, url, _lower(e.headers))
        except urllib.error.URLError as e:
            cert = isinstance(e.reason, ssl.SSLCertVerificationError)
            raise FetchFailed(str(e.reason), cert_problem=cert) from e
        except (OSError, ValueError) as e:  # timeouts, resets, malformed URLs
            raise FetchFailed(str(e)) from e

    def cert_expiry(self, host: str) -> datetime:
        ctx = ssl.create_default_context()
        try:
            with socket.create_connection((host, 443), timeout=self.timeout) as sock:
                with ctx.wrap_socket(sock, server_hostname=host) as tls:
                    not_after = tls.getpeercert()["notAfter"]
        except ssl.SSLCertVerificationError as e:
            raise FetchFailed(str(e), cert_problem=True) from e
        except (OSError, KeyError) as e:
            raise FetchFailed(str(e)) from e
        return datetime.fromtimestamp(ssl.cert_time_to_seconds(not_after), tz=timezone.utc)


def _lower(headers) -> dict[str, str]:
    return {k.lower(): v for k, v in headers.items()} if headers else {}


# --- The checks ---------------------------------------------------------------

_GENERATOR = re.compile(
    r"""<meta[^>]+name=["']generator["'][^>]+content=["']([^"']+)["']""", re.I)


def run_web_checks(domain: str, fetcher: Fetcher, now: datetime | None = None) -> list[Finding]:
    now = now or datetime.now(timezone.utc)
    findings: list[Finding] = []

    # 1. Find the site over HTTPS. Many sites only answer on www.
    response, host = None, None
    for candidate in (domain, f"www.{domain}"):
        try:
            response = fetcher.get(f"https://{candidate}/")
            host = candidate
            break
        except FetchFailed as e:
            if e.cert_problem:
                return [Finding(
                    "https.bad_cert", AREA, Severity.FIX_FIRST,
                    f"Visitors to https://{candidate} get a security warning.",
                    why="The site's certificate isn't valid. Browsers warn visitors "
                        "away, and people learn to click through warnings, which "
                        "is exactly the habit scammers rely on.",
                    fix="Ask your website host to install a free, auto-renewing "
                        "certificate (nearly every host offers one).",
                )]
    if response is None:
        return [Finding("https.unreachable", AREA, Severity.UNKNOWN,
                        f"Couldn't reach a website at https://{domain} or https://www.{domain}.",
                        fix="If you do have a website at a different address, re-run "
                            "with --website <address>.")]

    findings.append(Finding("https.ok", AREA, Severity.GOOD,
                            f"Your website loads over HTTPS (https://{host})."))

    # 2. Certificate expiry. Certificates are getting shorter-lived every
    #    year, so the real question is "is renewal automatic?", not "how
    #    long is left?". Only alarm when it's genuinely close.
    try:
        days = (fetcher.cert_expiry(host) - now).days
        if days < 7:
            findings.append(Finding(
                "https.expiring", AREA, Severity.FIX_FIRST,
                f"Your website's certificate expires in {max(days, 0)} days.",
                fix="Contact your website host today and ask them to renew it "
                    "and turn on automatic renewal.",
            ))
        elif days < 21:
            findings.append(Finding(
                "https.expiring_soon", AREA, Severity.INFO,
                f"Your website's certificate expires in {days} days.",
                fix="Usually fine if renewal is automatic. If you're not sure it "
                    "is, ask your website host.",
            ))
    except FetchFailed:
        pass  # already confirmed HTTPS works; expiry is a bonus detail

    # 3. HSTS tells browsers "only ever use HTTPS for this site".
    if "strict-transport-security" in response.headers:
        findings.append(Finding("https.hsts", AREA, Severity.GOOD,
                                "Your site tells browsers to always use HTTPS (HSTS)."))
    else:
        findings.append(Finding(
            "https.no_hsts", AREA, Severity.WORTH_DOING,
            "Your site doesn't tell browsers to always use HTTPS (no HSTS header).",
            why="On public Wi-Fi, an attacker can sometimes intercept a visitor's "
                "first, unencrypted request. HSTS closes that gap.",
            fix='Ask your website host to enable "HSTS" (many have a one-click setting).',
        ))

    # 4. Does plain http:// send visitors to https://?
    try:
        plain = fetcher.get(f"http://{host}/", follow_redirects=False)
        location = plain.headers.get("location", "")
        if plain.status in (301, 302, 303, 307, 308) and location.startswith("https://"):
            findings.append(Finding("http.redirects", AREA, Severity.GOOD,
                                    "Typing your address without https:// still lands on the secure site."))
        elif 200 <= plain.status < 300:
            findings.append(Finding(
                "http.no_redirect", AREA, Severity.WORTH_DOING,
                "Your site also loads without encryption (http://), without "
                "redirecting to https://.",
                fix='Ask your website host to "force HTTPS" or "redirect HTTP to HTTPS".',
            ))
    except FetchFailed:
        pass  # many hosts simply don't listen on port 80; that's fine

    # 5. Sites often announce their software and version in the page.
    m = _GENERATOR.search(response.body or "")
    if m:
        software = m.group(1).strip()
        findings.append(Finding(
            "web.generator", AREA, Severity.INFO,
            f'Your site publicly says it runs "{software}".',
            why="Outdated website software and plugins are the most common way "
                "small-organization websites get hacked. Attackers search for "
                "sites announcing old versions.",
            fix="Check this is the newest version, turn on automatic updates, "
                "and delete plugins and themes you don't use.",
        ))
    return findings
