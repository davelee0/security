"""The shape of a result.

Every check returns a list of Finding objects. Keeping one small, shared
shape means the checks don't care how results are shown, and the report
code doesn't care how a check worked. Later tools (for example a Google
Workspace audit) can return the same shape and reuse the same report.
"""

from __future__ import annotations

from dataclasses import dataclass
from enum import Enum


class Severity(Enum):
    # Order matters: the report lists findings in this order.
    FIX_FIRST = "Fix first"
    WORTH_DOING = "Worth doing"
    INFO = "Good to know"
    GOOD = "Looks good"
    # "We couldn't check" is NOT the same as "it's missing". Reporting a
    # failed lookup as a missing record would send a volunteer off to fix
    # something that isn't broken, and erode trust in the tool.
    UNKNOWN = "Couldn't check"


@dataclass
class Finding:
    check: str          # stable id, e.g. "dmarc.missing" (useful for JSON / tests)
    area: str           # "Email" or "Website"
    severity: Severity
    title: str          # one line, plain language
    why: str = ""       # why it matters, in the organization's terms
    fix: str = ""       # what to do, or who to ask

    def to_dict(self) -> dict:
        return {
            "check": self.check,
            "area": self.area,
            "severity": self.severity.name,
            "title": self.title,
            "why": self.why,
            "fix": self.fix,
        }
