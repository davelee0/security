# checkup: a plain-language domain security check

Checks the public email and website settings of a domain and explains
the results in plain language, most important first.

```
python -m checkup stmarys.org
```

## What it checks

| Area | Check | Why it matters |
|---|---|---|
| Email | **DMARC** record and policy | Stops scammers sending email that looks like it's from you |
| Email | **SPF** record: exactly one, sensible ending, under 10 lookups | Lists who may send your email; broken SPF silently stops working |
| Email | **DKIM** signing (Google Workspace / Microsoft 365) | A digital signature on your email; off by default in Google Workspace |
| Email | Which **provider** handles your email | So the advice can give the exact steps for your provider |
| Website | Loads over **HTTPS** with a valid certificate | Otherwise visitors see a security warning |
| Website | **Certificate expiry** | Catches renewals that aren't automatic |
| Website | **HSTS** header and **http → https redirect** | Keeps visitors on the encrypted site |
| Website | Software **version** the site announces | Old WordPress/plugins are the top cause of small-site hacks |

## What it sends over the network (and doesn't)

- **DNS lookups** for the domain's public records (MX, TXT, SOA, and
  `_dmarc.` / `_domainkey.` names). Every mail server that receives your
  email makes these same lookups.
- **Up to four ordinary page requests** to the homepage
  (`https://domain/`, `https://www.domain/`, `http://` version) plus one
  TLS handshake to read the certificate dates. This is what a browser
  does when someone visits.
- **Nothing else.** No port scanning, no probing for admin pages, no
  login attempts, no data sent anywhere but the domain itself and your
  normal DNS resolver.

Even so, **run it on domains you're responsible for, or with the
owner's permission.** It's a matter of trust, not only of legality. And
don't commit reports about real organizations to a public repository.

## Install and run (Mac)

From the repository folder:

```bash
python3 -m venv .venv
```

```bash
source .venv/bin/activate
```

```bash
pip install -e '.[test]'
```

```bash
checkup yourdomain.org
```

Options: `--json` for machine-readable output, `--no-web` to skip the
website checks, `--website other.org` if your website lives on a
different domain from your email. The exit code is `1` if anything is
marked "Fix first", so it can run on a schedule.

Run the tests with `pytest`.

## How the code is organized

```
checkup/
  findings.py      Finding + Severity: the one shape every check returns
  email_checks.py  SPF / DMARC / DKIM / MX logic (pure, testable)
  resolver.py      The real DNS lookups (dnspython), kept separate
  web_checks.py    HTTPS / certificate / HSTS / redirect / version
  report.py        Findings -> plain-language Markdown, or JSON
  cli.py           Command-line entry point
tests/             Offline tests using fake DNS and fake web responses
```

The idea worth noticing: **the checks never talk to the network
directly.** They receive a `resolver` or `fetcher` object. The real
program passes in one that does real lookups; the tests pass in a fake
built from a dictionary. That's why the tests run in a fraction of a
second, need no internet, and can simulate situations that are hard to
find in the wild (a timeout, an SPF loop, a nearly-expired certificate).

## Honesty rules the code follows

- **"Couldn't check" is never reported as "missing."** A DNS timeout
  gets its own *Couldn't check* section. A domain DNS says doesn't exist
  stops the email checks instead of reporting every record as missing.
  (That came from a real bug found while building this: a network that
  answered "doesn't exist" for every name made a well-configured domain
  look completely unprotected.)
- **DKIM can only be guessed at.** There is no way to list a domain's
  DKIM keys, so for unrecognized providers a miss is reported as "couldn't
  confirm," not "missing."
- **No made-up scores.** A letter grade would feel precise and mean
  little. The report sorts by what to do next instead.

## Limits

It sees only what's public. The protections that matter most (MFA
on every account, who has admin access, what's shared publicly in
Drive/OneDrive, backups) are invisible from outside. See
[docs/DIRECTION.md](../docs/DIRECTION.md) for the planned tool that
checks those from the inside.
