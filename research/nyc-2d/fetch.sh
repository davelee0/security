#!/usr/bin/env bash
# Reproduce the dataset from NYC Public Schools' published 2-d disclosures.
#
# Politeness: checks robots.txt, identifies itself, waits between requests,
# and fetches only the six public pages NYC publishes for parents.
#
# Usage:  ./fetch.sh <output-dir>
set -euo pipefail
OUT=${1:?usage: fetch.sh <output-dir>}
HERE=$(cd "$(dirname "$0")" && pwd)
mkdir -p "$OUT"
UA="security-research (public-interest student data study; https://github.com/davelee0/security)"
BASE="https://www.schools.nyc.gov/about-us/policies/data-privacy-and-security-policies/supplemental-information-for-parents-about-doe-agreements-with-outside-entities"

# These pages sit under /about-us/, which robots.txt allows. Fail loudly if that changes.
if curl -fsS -A "$UA" https://www.schools.nyc.gov/robots.txt | grep -qi '^Disallow: /about-us'; then
  echo "robots.txt now disallows these pages; stopping." >&2; exit 1
fi

for page in index vendors-a-h vendors-i-q vendors-r-z related-services-providers research; do
  path=$([ "$page" = index ] && echo "" || echo "/$page")
  curl -fsS --max-time 60 -A "$UA" -o "$OUT/$page.html" "$BASE$path"
  python3 -I "$HERE/totext.py" "$OUT/$page.html" > "$OUT/$page.txt"
  sleep 3
done


python3 -I "$HERE/parse.py" "$OUT"/vendors-*.txt "$OUT/related-services-providers.txt" "$OUT/research.txt" > "$OUT/entries.json"
python3 -I "$HERE/analyze.py" "$OUT/entries.json" > "$OUT/findings.json"
echo "Wrote $OUT/entries.json and $OUT/findings.json"
