"""Turn findings into something a non-technical person can act on.

Design choices:
  * Lead with what to fix first, not with everything that was checked.
    A 20-line report where every item looks equally important gets
    closed and forgotten.
  * Plain Markdown, so it reads fine in a terminal, pastes into an email,
    and renders nicely if saved as a .md file.
"""

from __future__ import annotations

import json
from datetime import date

from .findings import Finding, Severity

INTRO = {
    Severity.FIX_FIRST: "These leave the door open to scams or warnings. Start here.",
    Severity.WORTH_DOING: "Real improvements, once the items above are done.",
    Severity.INFO: "No action required, but useful to know.",
    Severity.GOOD: "Already in good shape.",
    Severity.UNKNOWN: "These lookups didn't answer, so we can't say either way. Try again later.",
}


def to_markdown(domain: str, findings: list[Finding], today: date | None = None) -> str:
    today = today or date.today()
    counts = {s: sum(f.severity is s for f in findings) for s in Severity}
    lines = [
        f"# Security checkup: {domain}",
        "",
        f"_Checked {today.isoformat()} using only public information "
        "(DNS records and the public homepage)._",
        "",
        f"**{counts[Severity.FIX_FIRST]} to fix first, "
        f"{counts[Severity.WORTH_DOING]} worth doing, "
        f"{counts[Severity.GOOD]} looking good.**",
    ]
    for severity in Severity:  # enum order = priority order
        group = [f for f in findings if f.severity is severity]
        if not group:
            continue
        lines += ["", f"## {severity.value}", "", f"_{INTRO[severity]}_", ""]
        for f in group:
            lines.append(f"- **{f.area}:** {f.title}")
            if f.why:
                lines.append(f"  - Why it matters: {f.why}")
            if f.fix:
                lines.append(f"  - What to do: {f.fix}")
    lines += [
        "",
        "---",
        "This checks a few public settings only. It is not a full security "
        "assessment. The biggest protections (two-step sign-in for every "
        "account, updates, backups) can't be seen from outside; see the "
        "checklist at https://github.com/davelee0/security.",
    ]
    return "\n".join(lines) + "\n"


def to_json(domain: str, findings: list[Finding]) -> str:
    return json.dumps({"domain": domain, "findings": [f.to_dict() for f in findings]}, indent=2)
