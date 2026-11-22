"""Live smoke test, run by CI on a machine with real internet access.

Runs checkup against example.com, a domain reserved for documentation and
testing (RFC 2606), so no one else's systems are involved. It fails if any
lookup comes back "couldn't check", which would mean the real DNS and web
code paths are broken in a way the offline tests can't catch.
"""

import json
import subprocess
import sys

result = subprocess.run(
    [sys.executable, "-m", "checkup", "example.com", "--json"],
    capture_output=True, text=True, timeout=120,
)
print(result.stdout)
print(result.stderr, file=sys.stderr)
if result.returncode not in (0, 1):  # 1 just means "something to fix first"
    sys.exit(f"checkup crashed (exit {result.returncode})")

findings = json.loads(result.stdout)["findings"]
unknown = [f for f in findings if f["severity"] == "UNKNOWN"]
if unknown:
    sys.exit(f"lookups failed on a live network: {[f['check'] for f in unknown]}")

checks = {f["check"] for f in findings}
# example.com publishes a null MX, an SPF record and an enforced DMARC policy.
for expected in ("mx.none", "dmarc.enforced", "https.ok"):
    if expected not in checks:
        sys.exit(f"expected '{expected}' for example.com, got {sorted(checks)}")
print("live smoke test passed")
