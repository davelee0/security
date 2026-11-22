# What NYC's student-data disclosures actually tell parents

_A study of the 972 public disclosures NYC Public Schools publishes under
New York Education Law 2-d. Data as of November 22, 2026._

## Why this matters

New York has the strongest student-privacy law in the country. Under
Education Law 2-d and its regulations (8 NYCRR Part 121), every outside
party that receives student data must sign an agreement, follow the NIST
Cybersecurity Framework, encrypt data in motion and at rest, and file a
public "supplemental information" disclosure that the district posts for
parents. NYC posts these on five long web pages.

In January 2022, Illuminate Education, an NYC vendor under exactly this
regime, was breached. About 1.7 million New York students were affected,
more than a million of them in NYC. NYC said Illuminate had not encrypted
data as its agreement required. The FTC alleges Illuminate stored student
data in plain text until at least January 2022. New York, California and
Connecticut settled with Illuminate for $5.1 million in November 2025, and
the FTC announced a proposed consent order in December 2025.
([NY AG](https://ag.ny.gov/press-release/2025/attorney-general-james-and-multistate-coalition-secure-51-million-education),
[The 74](https://www.the74million.org/article/ftc-state-ags-crack-down-on-ed-tech-company-after-massive-student-data-breach/),
[THE Journal](https://thejournal.com/articles/2022/03/28/io-classroom-cyberattack-in-january-compromised-personal-data-of-over-800k-students.aspx))

So the question this study asks: **if you were a parent reading these
disclosures, could you tell a vendor like that apart from any other?**

## What we found

All figures come from NYC's published pages; methods are below.

**1. 971 distinct outside parties are listed as receiving NYC student data.**
They include 542 commercial vendors, 238 community organizations and
nonprofits, 95 related-services providers (therapy practices and similar)
and 81 research projects.

**2. The encryption answer carries no information.** 930 of 972 entries
(95.7%) chose the identical pre-written sentence: _"PII will be encrypted in
motion and at rest using industry-standard data encryption technology."_ A
question everyone answers the same way can't distinguish anyone.

**3. Illuminate's disclosure is still posted, unchanged.** It is the one
remaining entry in the oldest format. It still says _"Data is encrypted at
both rest and in transfer in accordance with NIST Cybersecurity Framework
requirements."_ Regulators' findings never flowed back into the page
parents read: no correction, no flag, nearly five years after the breach.

**4. Some disclosures contradict themselves.**
- 19 of the 21 entries that describe storing records on paper also affirm
  that *all* PII is encrypted at rest. Paper can't be encrypted.
- 26 entries say they share no PII with subcontractors, then name a
  third-party host (AWS, Microsoft 365, Google, DigitalOcean and others).
  A cloud host holding the data *is* a third party with the data.
- 40 entries that say they store no PII at all still tick the encryption
  box. That's harmless, but it shows the box gets ticked by reflex.

**5. Many agreements appear to have ended.** Of the 368 entries with a
parseable end date, 203 (55%) ended before November 22, 2026, and 87 of
those more than two years ago. Each one is either a renewed agreement with
a stale disclosure or an ended agreement whose data should have been
deleted. A parent can't tell which.

**6. The free-text answers rarely name the controls that matter.** In
describing their safeguards, 29.5% of commercial vendors mention
multi-factor authentication, 11.3% SOC 2, and 14.0% penetration testing.
Among related-services providers, the figures are 23.2%, 0% and 2.1%. Not
mentioning a control doesn't mean a party lacks it. It means the disclosure
doesn't tell a parent.

**7. AI is mostly invisible.** NYC's March 2026 AI guidance says vendors
must disclose AI capabilities and that responses are published under 2-d.
The published form has no AI question; 53 entries mention AI anywhere in
their free text. (The disclosures may be published elsewhere; we didn't
find them on these pages.)

## What it means

New York built the most complete student-privacy transparency system in
the US, and it works as **an attestation system with no verification and
no feedback loop**. Vendors describe themselves; nobody checks the
description against reality, and when regulators find that a description
was false, the description stays up.

That isn't a failure of effort. Everyone involved is filling in the form
they were given. It's a **design** problem, and design problems have cheap
fixes:

1. **Ask questions that can be false.** Replace "agree to encrypt" with
   questions whose answers differ and can be checked: _Is multi-factor
   authentication required for every account that can reach student data?
   Date of your last independent security assessment, or "none"? Do you
   use AI on student data, and for what?_
2. **Catch contradictions when the form is submitted.** The checks in
   `analyze.py` are a few lines each. A structured form could reject
   "paper storage + encrypted at rest" before it's ever published.
3. **Close the loop.** When a breach report, complaint determination or
   enforcement action concerns a listed party, annotate its entry.
4. **Show status.** For each entry: active or ended, and if ended, the date
   data deletion was confirmed.
5. **Verify a sample.** Ask a random handful of parties each year for
   evidence behind their answers, the way tax authorities audit a sample of
   returns. The possibility of being checked changes how everyone answers.
6. **Help the small parties tell the truth.** Community organizations and
   one-office therapy practices are held to the same NIST-aligned standard
   as large vendors. A plain-language guide that turns the legal
   requirements into ten concrete, free steps would make their answers
   true rather than aspirational.

**This generalizes beyond NYC.** The national Student Data Privacy
Consortium's registry holds over 100,000 signed data privacy agreements
built on the same attestation model. Reading thousands of disclosures for
contradictions and vagueness is tedious for people and cheap for
software, including AI. Oversight bodies drowning in paperwork may be
exactly where AI helps defenders most.

## Methods

- `fetch.sh` downloads the six public pages (after checking robots.txt,
  with a 3-second pause between requests), converts them to text, and runs
  the pipeline. Nothing else is contacted.
- `parse.py` splits the text into entries using the questionnaire's own
  labels. It handles all three generations of the form.
- `analyze.py` applies small, readable rules and prints aggregates
  (`findings-2026-11-22.json`).
- Every rule was spot-checked by reading matching entries. For example, the
  paper rule matches only real paper storage (no "paperless"), and each
  subcontractor contradiction was read by hand. A "boilerplate" metric was
  dropped after checking showed it mostly counted the city's own pre-filled
  text.
- Two fetches about ten minutes apart produced identical findings. The raw
  HTML differs between requests (it contains per-request tokens), so we
  don't publish page hashes.
- Tests: `tests/test_nyc2d.py`.

## What this study deliberately doesn't do

- **It names no small organization.** Most contradictions look like a
  confusing form, not bad faith, so the analysis reports aggregates only.
  The one named party, Illuminate, is already the subject of public
  enforcement actions.
- **It doesn't republish the dataset.** Anyone can regenerate it with
  `fetch.sh`; we didn't want to circulate a list of small businesses in a
  security context.
- **It doesn't test any system.** It reads what NYC publishes for parents.

A courtesy note to NYC Public Schools' privacy office
(studentprivacy@schools.nyc.gov) before any wider circulation would be
good practice, particularly about the Illuminate entry.
