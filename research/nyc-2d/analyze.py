"""Summarize what NYC's Education Law 2-d disclosures do and don't tell parents.

Input: entries.json from parse.py. Output: aggregate findings as JSON.

Deliberately reports aggregates only. Many entries are small businesses
and sole practitioners; a self-contradictory form usually means a
confusing questionnaire, not a bad actor, so this script never outputs a
list of named entities flagged as contradictory.

Usage:  python3 -I analyze.py entries.json [YYYY-MM-DD]
"""

from __future__ import annotations

import json
import re
import sys
from collections import Counter
from datetime import date, datetime
from statistics import median


def low(s: str) -> str:
    return s.lower()


# --- Classifiers. Each is a small, inspectable rule. ---------------------------

def encryption_is_checkbox(e) -> bool:
    """The pre-written sentence the form offers, chosen verbatim."""
    return "will be encrypted in motion and at rest using industry-standard" in low(e["encryption"])


def stores_on_paper(e) -> bool:
    return bool(re.search(r"physical format|\bpaper\b", low(e["storage"])))


def says_no_subcontractors(e) -> bool:
    s = low(e["subcontractors"])
    return ("will not share pii with subcontractors" in s
            or "no pii will be shared with subcontractors" in s)


def no_subcontractors_explicitly_incl_cloud(e) -> bool:
    return says_no_subcontractors(e) and "including any cloud" in low(e["subcontractors"])


CLOUD = re.compile(r"hosted by a subcontractor|\baws\b|amazon web services|azure|google cloud|"
                   r"microsoft ?365|office ?365|google workspace|g suite|dropbox|box\.com")


def hosted_by_third_party(e) -> bool:
    return bool(CLOUD.search(low(e["storage"])))


def stores_nothing(e) -> bool:
    s = low(e["storage"])
    return "no pii will be stored" in s or "will not store or host" in s or "will not electronically store" in s


MENTIONS = {
    "multi_factor_auth": r"multi[- ]?factor|\bmfa\b|two[- ]factor|2fa|two[- ]step",
    "soc2": r"soc ?2|soc ii",
    "iso27001": r"iso[ /]?(iec )?27001",
    "penetration_test": r"penetration|pen[- ]test",
    "nist": r"\bnist\b",
    "incident_response": r"incident response",
    "least_privilege_or_rbac": r"least privilege|role[- ]based|\brbac\b",
    "training": r"training",
    "ai": r"artificial intelligence|\bgenerative\b|machine learning|\bai\b",
}


def term_end(e) -> date | None:
    dates = re.findall(r"\b(\d{1,2})/(\d{1,2})/(\d{2,4})\b", e["term"])
    if not dates:
        return None
    m, d, y = dates[-1]
    y = int(y) + (2000 if len(y) == 2 else 0)
    try:
        return date(y, int(m), int(d))
    except ValueError:
        return None


def entity_kind(e) -> str:
    t = low(e["entity_type"])
    if e["page"] == "related-services-providers":
        return "related services provider"
    if "community" in t or "not-for" in t or "nonprofit" in t:
        return "community organization / nonprofit"
    if "research" in t or "universit" in t or e["page"] == "research":
        return "research"
    if "commercial" in t:
        return "commercial vendor"
    return "other"


def pct(n: int, d: int) -> float:
    return round(100 * n / d, 1) if d else 0.0


def main(path: str, as_of: str | None) -> None:
    today = datetime.strptime(as_of, "%Y-%m-%d").date() if as_of else date.today()
    entries = json.load(open(path, encoding="utf-8"))
    n = len(entries)

    checkbox = [e for e in entries if encryption_is_checkbox(e)]
    paper = [e for e in entries if stores_on_paper(e)]
    paper_and_checkbox = [e for e in paper if encryption_is_checkbox(e)]
    nosub = [e for e in entries if says_no_subcontractors(e)]
    nosub_cloud = [e for e in nosub if hosted_by_third_party(e)]
    strict = [e for e in entries if no_subcontractors_explicitly_incl_cloud(e) and hosted_by_third_party(e)]
    nothing_but_checkbox = [e for e in entries if stores_nothing(e) and encryption_is_checkbox(e)]

    ends = [(e, term_end(e)) for e in entries]
    dated = [(e, t) for e, t in ends if t]
    expired = [(e, t) for e, t in dated if t < today]

    by_kind = {}
    for kind in sorted({entity_kind(e) for e in entries}):
        group = [e for e in entries if entity_kind(e) == kind]
        lens = [len(e["safeguards"]) for e in group]
        by_kind[kind] = {
            "entries": len(group),
            "median_safeguards_chars": int(median(lens)) if lens else 0,
            "mentions_pct": {k: pct(sum(bool(re.search(rx, low(e["safeguards"]))) for e in group), len(group))
                             for k, rx in MENTIONS.items()},
        }

    result = {
        "as_of": today.isoformat(),
        "entries": n,
        "entries_by_kind": {k: v["entries"] for k, v in by_kind.items()},
        "encryption": {
            "chose_identical_prewritten_sentence": len(checkbox),
            "pct": pct(len(checkbox), n),
        },
        "contradictions": {
            "paper_storage": len(paper),
            "paper_storage_but_affirm_encryption_at_rest": len(paper_and_checkbox),
            "say_no_subcontractors": len(nosub),
            "say_no_subcontractors_but_name_third_party_hosting": len(nosub_cloud),
            "same_where_form_explicitly_counts_cloud_as_subcontractor": len(strict),
            "store_nothing_but_affirm_encryption_at_rest": len(nothing_but_checkbox),
        },
        "terms": {
            "with_parseable_end_date": len(dated),
            "end_date_already_passed": len(expired),
            "pct_of_dated": pct(len(expired), len(dated)),
            "passed_by_more_than_2_years": sum(1 for _, t in expired if (today - t).days > 730),
        },
        "ai": {
            "entries_mentioning_ai_anywhere": sum(1 for e in entries if re.search(MENTIONS["ai"], low(
                " ".join([e["purpose"], e["safeguards"], e["storage"]])))),
            "note": "The published form has no dedicated AI question; mentions come from free text.",
        },
        "notes": [
            "Mention rates measure what the free-text safeguards answer says, not what a vendor does.",
            "Research-page entries share DOE-prefilled safeguards text, which inflates their mention rates.",
            "An end date in the past may mean an ended agreement or a disclosure that was never updated.",
        ],
        "by_kind": by_kind,
    }
    print(json.dumps(result, indent=1))


if __name__ == "__main__":
    main(sys.argv[1], sys.argv[2] if len(sys.argv) > 2 else None)
