"""Tests for the NYC Education Law 2-d disclosure parser and analysis.

Fixtures are short, made-up entries that copy the published questionnaire's
wording, so the rules can be checked without fetching anything.
"""

import importlib.util
import json
import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent.parent / "research" / "nyc-2d"


def load(name):
    spec = importlib.util.spec_from_file_location(f"nyc2d_{name}", HERE / f"{name}.py")
    mod = importlib.util.module_from_spec(spec)
    sys.modules[f"nyc2d_{name}"] = mod  # dataclasses look the module up while it loads
    spec.loader.exec_module(mod)
    return mod


parse = load("parse")
analyze = load("analyze")

PAGE = """Listed in Alphabetical Order:
Acme Learning
Type of Entity:
Commercial Enterprise
Contract / Agreement Term:
2/1/2022 - 2/1/2023
Describe briefly the project you are providing.
An AI-powered reading tutor.
Type of PII that the Entity will receive/access:
Student PII.
Subcontractor Written Agreement Requirement. In accordance with New York Education Law 2-d...
Vendor selected “The Entity will not share PII with subcontractors, outside persons, or third party entities.”
Security and Storage Protections. Describe where PII will be stored or hosted.
Using a cloud or infrastructure owned tool hosted by a subcontractor; i.e., AWS.
Describe the administrative, technical and/or physical safeguards to ensure PII will be protected.
We require multi-factor authentication for all staff.
Encryption. Pursuant to New York Education Law 2-d, PII must be encrypted while in motion and while at rest.
Vendor selected “Entity agrees that PII will be encrypted in motion and at rest using industry-standard data encryption technology.”
Small Therapy PLLC
Type of Organization:
Commercial Enterprise
Contract / Agreement Term:
The Agreement covers multiple products, services and/or DOE schools and offices.
Description of the exclusive purpose(s) for which you will access/receive PII:
Speech therapy.
Type of data that you will access/receive:
Student PII.
Subcontractor Written Agreement Requirement. In accordance with New York Education Law § 2-d...
No PII will be shared with subcontractors or third-party entities (including any cloud services providers).
Security and Storage Protections. Describe how PII will be stored or hosted.
On Organization servers or devices and in a physical format (e.g. paper records).
Summarize the administrative, technical and/or physical safeguards you use:
Locked file cabinet.
Encryption. Confirm that PII will be encrypted in motion and at rest in accordance with New York Education Law 2-D.
Organization selected “ PII will be encrypted in motion and at rest using industry-standard data encryption technology.”
Legacy Vendor
The exclusive purposes for which PISI will be used:
Products and services.
Where the PISI will be stored (described in such a manner as to protect data security):
Hosted with Amazon Web Services.
How the data will be encrypted (described in such a manner as to protect data security):
Data is encrypted at both rest and in transfer.
Was this page helpful?
"""


def entries():
    lines = [l.strip() for l in PAGE.splitlines() if l.strip()]
    return [parse.fill(e) for e in parse.split_entries(lines, "vendors-a-h")]


def test_splits_all_three_form_generations():
    es = entries()
    assert [e.name for e in es] == ["Acme Learning", "Small Therapy PLLC", "Legacy Vendor"]
    assert [e.form for e in es] == ["current", "current", "legacy"]


def test_extracts_fields():
    acme, therapy, legacy = entries()
    assert acme.entity_type == "Commercial Enterprise"
    assert acme.term == "2/1/2022 - 2/1/2023"
    assert acme.storage.endswith("i.e., AWS.")
    assert "multi-factor" in acme.safeguards
    assert therapy.safeguards == "Locked file cabinet."
    assert "Amazon Web Services" in legacy.storage
    assert "Was this page helpful" not in legacy.encryption  # footer trimmed


def test_findings(tmp_path, capsys):
    from dataclasses import asdict
    data = []
    for e in entries():
        d = asdict(e)
        d.pop("raw")
        data.append(d)
    path = tmp_path / "entries.json"
    path.write_text(json.dumps(data))
    analyze.main(str(path), "2026-11-22")
    f = json.loads(capsys.readouterr().out)

    assert f["entries"] == 3
    assert f["encryption"]["chose_identical_prewritten_sentence"] == 2  # legacy wrote its own
    c = f["contradictions"]
    assert c["paper_storage_but_affirm_encryption_at_rest"] == 1        # Small Therapy
    assert c["say_no_subcontractors_but_name_third_party_hosting"] == 1  # Acme: "no subcontractors" + AWS
    assert f["terms"]["end_date_already_passed"] == 1                   # Acme ended 2023
    assert f["ai"]["entries_mentioning_ai_anywhere"] == 1
    assert f["by_kind"]["commercial vendor"]["mentions_pct"]["multi_factor_auth"] > 0


def test_paper_rule_ignores_paperless():
    assert not analyze.stores_on_paper({"storage": "We are a paperless office using AWS."})
    assert analyze.stores_on_paper({"storage": "In physical format."})
