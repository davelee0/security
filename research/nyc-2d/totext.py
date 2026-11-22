"""Convert a saved HTML page to plain text, one line per text node.

Usage:  python3 -I totext.py page.html > page.txt
"""

import html
import re
import sys

raw = open(sys.argv[1], encoding="utf-8", errors="replace").read()
raw = re.sub(r"(?is)<(script|style).*?</\1>", " ", raw)
raw = re.sub(r"(?i)<sup>(.*?)</sup>", r"\1", raw)  # "22<sup>nd</sup>" -> "22nd"
text = html.unescape(re.sub(r"(?s)<[^>]+>", "\n", raw))
for line in text.splitlines():
    line = " ".join(line.split())
    if line:
        print(line)
