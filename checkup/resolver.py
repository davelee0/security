"""The real DNS resolver, built on the dnspython library.

The only job here is to translate dnspython's answers and exceptions into
the two simple outcomes the checks understand:
  * a list of records (possibly empty: "the record doesn't exist"), or
  * LookupFailed ("we couldn't find out").
"""

from __future__ import annotations

import dns.exception
import dns.resolver

from .email_checks import LookupFailed


class DnsResolver:
    def __init__(self, timeout: float = 5.0):
        self._r = dns.resolver.Resolver()
        self._r.lifetime = timeout

    def _query(self, name: str, rtype: str):
        try:
            return self._r.resolve(name, rtype)
        except (dns.resolver.NXDOMAIN, dns.resolver.NoAnswer):
            return []  # a definite "no such record"
        except dns.exception.DNSException as e:  # timeout, SERVFAIL, no nameservers...
            raise LookupFailed(f"{rtype} {name}: {e}") from e

    def exists(self, name: str) -> bool:
        # NXDOMAIN means "this name doesn't exist at all". NoAnswer means the
        # name exists but has no record of this type, which is fine here.
        try:
            self._r.resolve(name, "SOA")
        except dns.resolver.NXDOMAIN:
            return False
        except dns.resolver.NoAnswer:
            pass
        except dns.exception.DNSException as e:
            raise LookupFailed(f"SOA {name}: {e}") from e
        return True

    def txt(self, name: str) -> list[str]:
        # One TXT record can be split into several 255-byte chunks; they must
        # be joined back together with no separator (RFC 7208 section 3.3).
        return [b"".join(r.strings).decode("utf-8", "replace") for r in self._query(name, "TXT")]

    def mx(self, name: str) -> list[str]:
        records = sorted(self._query(name, "MX"), key=lambda r: r.preference)
        return [r.exchange.to_text() for r in records]
