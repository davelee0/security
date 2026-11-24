"""How often do NYC's Ed Law 2-d disclosures describe vendor support access?

Tests one assumption behind the access register (docs/kits/access-register.md):
that the way vendors' own staff reach student data is invisible to schools.

This script finds candidate passages; the classification of each passage
(support access to customer data vs. employees' remote access to the vendor's
own systems, and what controls are described) was done by reading them, and
is recorded in docs/research/access-register-assumptions.md. Regex rules for
"approval first" or "logged" proved unreliable, so they aren't scored here.

Prints counts and anonymized snippets only; no entity names.

Usage:  python3 -I support_access.py entries.json [--show]
"""

from __future__ import annotations

import json
import re
import sys

CANDIDATE = re.compile(
    r"support (staff|team|personnel|engineer|representative)s? (may|can|will|have|has|with) (access|view)"
    r"|access(ed)? (by|for) (our )?(customer )?support"
    r"|for (customer |technical )?support purposes"
    r"|remote (access|support|desktop|session)"
)


def text(e: dict) -> str:
    return " ".join([e.get("purpose", ""), e.get("safeguards", ""),
                     e.get("storage", ""), e.get("subcontractors", "")]).lower()


def main(path: str, show: bool) -> None:
    entries = [e for e in json.load(open(path, encoding="utf-8")) if e["page"] != "research"]
    hits = [e for e in entries if CANDIDATE.search(text(e))]
    print(json.dumps({"entries_excluding_research": len(entries),
                      "candidate_passages": len(hits)}, indent=1))
    if show:
        for i, e in enumerate(hits):
            t = text(e)
            m = CANDIDATE.search(t)
            print(f"\n[{i}] ...{t[max(0, m.start() - 160):m.end() + 160]}...")


if __name__ == "__main__":
    main(sys.argv[1], "--show" in sys.argv[2:])
