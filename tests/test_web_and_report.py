from datetime import date, datetime, timedelta, timezone

import pytest

from checkup.cli import normalize_domain
from checkup.findings import Finding, Severity
from checkup.report import to_json, to_markdown
from checkup.web_checks import FetchFailed, Response, run_web_checks

NOW = datetime(2026, 11, 22, tzinfo=timezone.utc)


class FakeFetcher:
    """Maps URL -> Response, or URL -> FetchFailed to simulate errors."""

    def __init__(self, pages, cert_days=60):
        self.pages = pages
        self.cert_days = cert_days

    def get(self, url, follow_redirects=True):
        result = self.pages.get(url, FetchFailed("connection refused"))
        if isinstance(result, Exception):
            raise result
        return result

    def cert_expiry(self, host):
        return NOW + timedelta(days=self.cert_days)


def ids(findings):
    return {f.check for f in findings}


def test_good_site():
    f = FakeFetcher({
        "https://stmarys.org/": Response(200, "https://stmarys.org/",
                                         {"strict-transport-security": "max-age=31536000"}),
        "http://stmarys.org/": Response(301, "http://stmarys.org/",
                                        {"location": "https://stmarys.org/"}),
    })
    assert ids(run_web_checks("stmarys.org", f, NOW)) == {"https.ok", "https.hsts", "http.redirects"}


def test_falls_back_to_www_and_spots_old_wordpress():
    body = '<head><meta name="generator" content="WordPress 5.8.1" /></head>'
    f = FakeFetcher({
        "https://www.stmarys.org/": Response(200, "https://www.stmarys.org/", {}, body),
        "http://www.stmarys.org/": Response(200, "http://www.stmarys.org/"),
    })
    findings = run_web_checks("stmarys.org", f, NOW)
    assert {"https.ok", "https.no_hsts", "http.no_redirect", "web.generator"} <= ids(findings)
    assert "WordPress 5.8.1" in next(x for x in findings if x.check == "web.generator").title


def test_bad_certificate_is_fix_first():
    f = FakeFetcher({"https://stmarys.org/": FetchFailed("expired", cert_problem=True)})
    [finding] = run_web_checks("stmarys.org", f, NOW)
    assert finding.check == "https.bad_cert" and finding.severity is Severity.FIX_FIRST


@pytest.mark.parametrize("days,expected", [(3, "https.expiring"), (15, "https.expiring_soon")])
def test_certificate_expiry(days, expected):
    f = FakeFetcher({"https://stmarys.org/": Response(200, "https://stmarys.org/")}, cert_days=days)
    assert expected in ids(run_web_checks("stmarys.org", f, NOW))


def test_no_website_is_unknown():
    assert ids(run_web_checks("stmarys.org", FakeFetcher({}), NOW)) == {"https.unreachable"}


def test_report_puts_fix_first_on_top():
    findings = [
        Finding("a", "Email", Severity.GOOD, "Fine thing"),
        Finding("b", "Email", Severity.FIX_FIRST, "Urgent thing", why="w", fix="f"),
    ]
    md = to_markdown("stmarys.org", findings, today=date(2026, 11, 22))
    assert md.index("Urgent thing") < md.index("Fine thing")
    assert "**1 to fix first, 0 worth doing, 1 looking good.**" in md
    assert '"severity": "FIX_FIRST"' in to_json("stmarys.org", findings)


@pytest.mark.parametrize("raw,expected", [
    ("stmarys.org", "stmarys.org"),
    ("https://www.StMarys.org/about-us", "stmarys.org"),
    ("school.stmarys.org.", "school.stmarys.org"),
])
def test_normalize_domain(raw, expected):
    assert normalize_domain(raw) == expected


@pytest.mark.parametrize("raw", ["", "not a domain", "localhost", "192.168.1.1"])
def test_normalize_domain_rejects_junk(raw):
    with pytest.raises(ValueError):
        normalize_domain(raw)
