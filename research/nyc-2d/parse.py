"""Turn NYC Public Schools' Education Law 2-d disclosures into structured data.

New York Education Law 2-d requires every school district to publish
"supplemental information" about each outside party that receives student
data: what data, for how long, where it's stored, and how it's protected.
NYC publishes these as long web pages. This script reads the plain-text
version of those pages (see fetch.sh) and extracts one record per entity.

It reads only what NYC publishes for parents. It never contacts vendors.

Usage:  python3 -I parse.py <text files...>  > entries.json
"""

from __future__ import annotations

import json
import re
import sys
from dataclasses import asdict, dataclass, field

# Labels as they appear in the published questionnaire. There are three
# generations of the form; we accept all of them.
TYPE_LABELS = ("Type of Entity:", "Type of Organization:")
OLD_FORMAT_FIRST = "The exclusive purposes for which PISI will be used:"
STOP_LABELS = (
    "Type of PII", "Type of data", "Subcontractor Written Agreement", "Data Transition",
    "Challenges to Data Accuracy", "Security and Storage Protections", "Describe the administrative",
    "Summarize the administrative", "Data Privacy Safeguards", "Encryption.", "Describe briefly", "Description of the exclusive",
    "Contract / Agreement Term", "How you will ensure", "When the agreement expires",
    "If and how a parent", "Where the PISI", "How the data will be encrypted",
)


@dataclass
class Entry:
    name: str
    page: str
    form: str                      # "current" or "legacy"
    entity_type: str = ""
    purpose: str = ""
    term: str = ""
    pii: str = ""
    subcontractors: str = ""       # raw selected statement
    storage: str = ""
    safeguards: str = ""
    encryption: str = ""
    raw: list[str] = field(default_factory=list, repr=False)


def _value_after(lines: list[str], label_prefix: str) -> str:
    """Join the lines following a label, up to the next known label."""
    for i, line in enumerate(lines):
        if line.startswith(label_prefix):
            # Some labels carry their value on the same line after a period;
            # the questionnaire puts answers on the following lines.
            out = []
            for nxt in lines[i + 1:]:
                if nxt.startswith(STOP_LABELS):
                    break
                out.append(nxt)
            return " ".join(out).strip()
    return ""


def split_entries(lines: list[str], page: str) -> list[Entry]:
    starts = []
    for i in range(len(lines) - 1):
        nxt = lines[i + 1]
        if nxt.startswith(TYPE_LABELS):
            starts.append((i, "current"))
        elif nxt.startswith(OLD_FORMAT_FIRST):
            starts.append((i, "legacy"))
    entries = []
    for n, (i, form) in enumerate(starts):
        end = starts[n + 1][0] if n + 1 < len(starts) else len(lines)
        body = lines[i + 1:end]
        # Trim the site footer that follows the final entry.
        for j, line in enumerate(body):
            if line.startswith(("Was this page helpful", "Back to top", "Footer")):
                body = body[:j]
                break
        entries.append(Entry(name=lines[i], page=page, form=form, raw=body))
    return entries


def fill(e: Entry) -> Entry:
    b = e.raw
    if e.form == "current":
        e.entity_type = _value_after(b, TYPE_LABELS[0]) or _value_after(b, TYPE_LABELS[1])
        e.purpose = _value_after(b, "Describe briefly") or _value_after(b, "Description of the exclusive")
        e.term = _value_after(b, "Contract / Agreement Term")
        e.pii = _value_after(b, "Type of PII") or _value_after(b, "Type of data")
        e.subcontractors = _value_after(b, "Subcontractor Written Agreement")
        e.storage = _value_after(b, "Security and Storage Protections")
        e.safeguards = (_value_after(b, "Describe the administrative")
                        or _value_after(b, "Summarize the administrative")
                        or _value_after(b, "Data Privacy Safeguards"))
        e.encryption = _value_after(b, "Encryption.")
    else:
        e.purpose = _value_after(b, OLD_FORMAT_FIRST)
        e.subcontractors = _value_after(b, "How you will ensure")
        e.term = _value_after(b, "When the agreement expires")
        e.storage = _value_after(b, "Where the PISI")
        e.encryption = _value_after(b, "How the data will be encrypted")
    return e


def main(paths: list[str]) -> None:
    out = []
    for path in paths:
        page = re.sub(r".*/|\.txt$", "", path)
        lines = [l.strip() for l in open(path, encoding="utf-8") if l.strip()]
        for e in split_entries(lines, page):
            d = asdict(fill(e))
            d.pop("raw")
            out.append(d)
    json.dump(out, sys.stdout, indent=1, ensure_ascii=False)


if __name__ == "__main__":
    main(sys.argv[1:])
