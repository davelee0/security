# The attack surface follows the money

_Security in the new school-choice infrastructure. Research notes, November 22, 2026._

> Working notes, not a finished report. Facts are cited; analysis and
> legal interpretations are marked as such and should be checked by
> people with the relevant expertise before anyone acts on them.

## In five lines

1. Public money for private education now flows through a new layer of
   infrastructure: state education savings accounts (ESAs) and, from
   **January 1, 2027**, a national federal scholarship tax credit run
   through thousands of scholarship granting organizations (SGOs).
2. That layer is concentrated at a few platform vendors. At its edges are
   thousands of small actors (families, new schools, micro-schools,
   tutors, new nonprofits) with no security staff. Incidents have already
   happened in Arizona, South Carolina, Missouri and Florida.
3. The federal draft rules let SGOs verify family income with **tax
   returns, W-2s and pay stubs**, or through **credit agencies and
   commercial data sources**. Many SGOs will be brand-new small
   nonprofits. That's the original problem this project set out to
   solve, created at national scale, on a deadline.
4. **Public comments on those rules close December 1, 2026**, with a
   hearing on December 15. States must certify their SGO lists by
   **February 15, 2027**. The rules for this system are being written
   right now.
5. The highest-leverage defensive work is shaping **design defaults and
   contracts** (verify eligibility, don't collect evidence; phishing-proof
   payouts; privacy-preserving transparency), not chasing breaches one
   at a time.

---

## What's happening (facts)

**The federal scholarship tax credit (Section 25F).** Taxpayers can
redirect up to $1,700 of federal tax ($3,400 for married couples) to SGOs
in participating states, starting January 1, 2027. States opt in each
year and certify a list of SGOs to the IRS. As of November 13, 2026, the
IRS lists 30 participating states. Treasury published proposed and
temporary regulations on October 2, 2026 (REG-117199-25). Comments are due
**December 1, 2026**, and a public hearing is scheduled for
**December 15, 2026**. The 2027 SGO lists are due by **February 15, 2027**.
Treasury estimates about 95% of US children live in households under the
program's income cap (300% of area median gross income).
([IRS participating states](https://www.irs.gov/government-entities/federal-state-local-governments/federal-scholarship-tax-credit-fstc-participating-states),
[Federal Register](https://www.federalregister.gov/documents/2026/10/02/2026-20277/federal-scholarship-tax-credit),
[Journal of Accountancy](https://www.journalofaccountancy.com/news/2026/oct/treasury-irs-propose-regulations-for-education-tax-credit/),
[Bipartisan Policy Center](https://bipartisanpolicy.org/issue-brief/the-federal-scholarship-tax-credit-what-treasurys-proposed-and-temporary-rules-mean-for-states-sgos-and-students/))

**How SGOs verify income (draft rules).** Direct verification with pay
stubs, tax returns, IRS transcripts, W-2s and other income evidence; or
"categorical" eligibility when a household member is in a qualifying
program. Reporting also describes verification through credit agencies or
commercial data sources.
([AASA memo](https://www.aasa.org/docs/default-source/resources/position-statement/memo---what-the-new-federal-scholarship-tax-credit-regulations-mean-for-states-sgos-and-school-districts.pdf?sfvrsn=1b084e8e_1),
[Current Federal Tax Developments](https://www.currentfederaltaxdevelopments.com/blog/2026/6/11/treasury-previews-regulatory-framework-for-new-section-25f-education-freedom-tax-credit))

**ESA platforms are concentrated.** ProPublica describes a small group of
young companies as the middlemen: ClassWallet (the largest), Odyssey,
Student First and Merit. Texas chose Odyssey for its program; funding
reached more than 100,000 students by August 2026, with up to $50 million
payable to the administrator.
([ProPublica](https://www.propublica.org/article/school-voucher-management-classwallet-odyssey-merit-student-first),
[Texas Comptroller](https://comptroller.texas.gov/about/media-center/news/20260813-comptroller-don-huffines-announces-100000-students-receiving-texas-education-freedom-accounts-1786645098165),
[KSAT](https://www.ksat.com/news/texas/2025/10/31/texas-put-its-chief-financial-officer-in-charge-of-school-vouchers-here8217s-what-you-need-to-know/))

**Incidents so far:**

| Where | When | What happened | Lesson |
|---|---|---|---|
| Arizona | 2023 | ESA families' personal and disability data exposed; the state attributed it to a former Department of Education staffer, not a hack of the platform | Insiders and access control, not just outside attackers |
| South Carolina | Sept 2025 | Phishing posing as the state or ClassWallet stole **education service providers'** login credentials, aiming at their banking information; accounts locked for weeks | The small schools and vendors receiving funds are the soft target; payout redirection |
| Missouri | 2025–26 | The **treasurer's own website** posted spreadsheets exposing three years of student names, parent contacts, amounts and schools; the office called it "directory information" and blamed its contractor | Transparency reporting itself is a leak vector |
| Florida | May 2026 | Parents arrested for altering receipts and bank statements to claim reimbursements | Document-based reimbursement is forgeable, and AI makes forging cheap |

([The 74 on South Carolina](https://www.the74million.org/article/cyberattack-hits-south-carolina-school-choice-program/),
[Fox 10 on Arizona](https://www.fox10phoenix.com/news/data-breach-reported-in-arizonas-school-voucher-program),
[Missouri Independent, April](https://missouriindependent.com/2026/04/21/missouri-treasurers-office-posted-moscholars-student-data-on-its-website-for-nearly-a-year/),
[Missouri Independent, July](https://missouriindependent.com/2026/07/27/after-voucher-data-leak-missouri-treasurers-office-pointed-at-its-contractor/),
[Florida CFO](https://myfloridacfo.com/news/pressreleases/press-release-details/2026/05/28/chief-financial-officer-blaise-ingoglia-announces-arrests-following-school-choice-fraud-scheme))

**The schools on the receiving end are new and small.** Heritage counts
more than 1,000 classical schools, 250+ opened since 2020. A campaign by
ACCS, Turning Point Education and Heritage aims for 5,000 new or converted
classical Christian schools in a decade. AP reports this growth is
substantially funded by these programs.
([Heritage](https://www.heritage.org/node/25157509/print-display),
[AP via WCAX](https://www.wcax.com/2026/10/21/taxpayers-are-funding-private-school-tuition-its-helping-classical-christian-schools-expand/))

**A precedent worth remembering.** GAO estimates pandemic unemployment
insurance fraud at $100–135 billion (11–15% of benefits). The Labor
Department named stolen identities as the main cause. GAO highlighted the
risks of launching quickly and of new controls that skip already-approved
claims.
([GAO-23-106696](https://www.gao.gov/assets/gao-23-106696.pdf))

---

## Seven ideas

### 1. Topology: decentralizing the money scattered the defense

A district-run system has a few large, audited institutions with IT
staff. Money-follows-the-child replaces that with a mesh: families ↔
platforms ↔ thousands of schools, tutors and vendors ↔ SGOs ↔ states ↔
IRS. Risk concentrates at the **hubs** (a few platforms, single points of
failure) while defense capacity is thinnest at the **edges** (families,
micro-schools, new SGOs). You can't defend ten thousand edges one at a
time. You defend the hubs, and you set the **protocol defaults** that
every edge inherits.

### 2. This is a "pre-HIPAA" moment

_(Analysis; needs legal review.)_ Data in these flows seems to fall
between existing protections:
- **FERPA** mostly doesn't reach private schools without federal funds.
- **COPPA** covers online services aimed at children under 13, not an
  SGO's spreadsheet.
- **IRC §6103** protects tax return information held by the IRS. A
  family's 1040 uploaded directly to an SGO is, as far as I can tell,
  outside it.
- **The FTC Safeguards Rule** covers "financial institutions," including
  tax preparers. Whether it reaches an SGO is unclear.
- **State student privacy laws** mostly target public schools and edtech
  operators.

So a family's tax return held by a new two-person nonprofit may be
governed by little more than state breach-notification law. Healthcare
had this gap until HIPAA's Security Rule. Card payments had it until the
card brands imposed PCI DSS. School choice has no equivalent yet.

### 3. Verify eligibility, don't collect evidence

An SGO needs one bit of information: *is this household under the cap?*
It doesn't need the 1040 that proves it. Every stored tax return is a
liability with no benefit once the decision is made. Design patterns, from
best to worst:

1. **Categorical eligibility** confirmed by the program that already knows
   (for example, SNAP or Medicaid enrollment confirmed by a state agency
   match). The SGO learns "eligible," nothing more.
2. **Source-verified yes/no**: an IRS-direct or state-direct check that
   returns *eligible / not eligible*, not the underlying return.
3. **A reusable eligibility credential**: verified once, presented to any
   SGO, revealing only the result. Some ESA vendors already build on
   digital credentials ([Merit](https://www.businesswire.com/news/home/20240627510200/en/New-Merit-Platform-Opens-Door-for-the-Next-Wave-of-Digital-Transformation-in-Government)).
4. **Documents**, only as a fallback: verify, record the decision, then
   **delete the documents** on a fixed schedule.
5. **Commercial data brokers**: avoid. They're opaque, error-prone, and
   leave families no way to dispute an error.

The same logic explains the Florida fraud: reimbursement by uploaded
receipt asks the system to trust documents, and AI is making documents
free to fake. **Pay the provider directly, or verify with the source.**
"Upload a PDF" is the wrong primitive.

### 4. Payouts are the prize, and identity is the lock

South Carolina was a textbook payment-diversion attack. Attackers
phished small providers' platform logins to change where money goes.
Standard, cheap controls stop most of this, and they belong in every
platform contract:
- Phishing-resistant sign-in (passkeys or security keys) required for any
  account that receives funds.
- A hold on bank-account changes, out-of-band confirmation, and a notice
  to the *old* contact.
- DMARC at `p=reject` on platform domains, so emails "from ClassWallet"
  that aren't from ClassWallet get blocked.
- A single published rule: "We will never ask for your password or bank
  details by email."

### 5. The $1,700 lure

Starting with the 2027 tax year, every American taxpayer will hear "get
$1,700 back by donating." That's a perfect scam: fake SGOs, lookalike
domains, "claim your credit" phishing at tax time. The defense is an
**authoritative, checkable registry**. States' certified SGO lists could
include each SGO's official web domain. The IRS list could link to them.
SGOs could be expected to publish DMARC so impersonating them fails. It's
cheap, nobody seems to be asking for it, and the window is before
February 15.

### 6. Transparency and privacy are both legitimate, and both are failing

School choice is politically contested, so both supporters and critics
demand accountability data. Missouri shows what happens when that demand
is met by posting raw spreadsheets. Each side's legitimate goal produces
harm to children. For a child in a custody or domestic-violence
situation, "this student, this school, this parent contact" is location
data. **Statistical disclosure control is a well-understood answer:**
aggregate reporting, suppressing small cells, no row-level data.
Proposing a *privacy-preserving transparency standard* is the rare move
that lets both sides win, and it's mostly a matter of craft.

### 7. "Subsidium": who helps the small do what they can't alone

Catholic social teaching's principle of subsidiarity says decisions
belong at the lowest competent level, and school choice is often argued
on those grounds. Its other half is less quoted: the higher body owes
*subsidium*, help with what the smaller body can't do for itself.
Security is exactly that kind of help. A two-person SGO or a twelve-family
micro-school can't run a security program, but a state, a platform, an
association or a diocese can give it safe defaults. That frame may land
with the Catholic and classical communities driving much of this growth,
and it explains why the work belongs at the hubs.

---

## What could be done, by deadline

| When | Contribution | Leverage |
|---|---|---|
| **Dec 1, 2026** | **A public comment to Treasury** (REG-117199-25) asking for: source-verified and categorical eligibility as the preferred methods; document deletion after verification; limits on data brokers, with a way for families to dispute; no secondary use or sale; breach notice to families and the state; a basic security baseline for SGOs; official domains on SGO lists. Optionally, ask to speak at the Dec 15 hearing. | National rules, read by the people writing them |
| **Feb 15, 2027** | **An "SGO certification security baseline"**: one page that state officials can attach to their SGO certification, and that SGOs can follow. | 30 state processes being designed now |
| 2027 | **A contract security commons**: an open dataset of what each state's ESA/SGO contracts and RFPs (public records) require for security, plus model clauses. This is the vendor project, reframed: *grade the contracts, not the vendors*. | Every future procurement |
| 2027 | **A privacy-preserving transparency standard** for school-choice reporting. | Defuses a recurring political fight |
| Ongoing | **A founder's kit** for new classical schools and micro-schools, including how to secure ESA platform accounts. | Thousands of schools at the cheapest moment |

The Catholic network is unusually well placed for all of it. State
Catholic conferences are prominent school-choice advocates, and Catholic
organizations already run scholarship programs under existing state
tax-credit laws. _(To verify: which Catholic SGOs exist in which states.)_

---

## What I don't know yet

- Whether Treasury's draft rules already say anything about data
  security. The full text needs a careful read; I've only seen
  summaries.
- Whether ESA platforms hold GovRAMP or SOC 2 attestations. Nothing turned
  up in search, which proves nothing either way.
- The legal analysis in idea 2. It needs a privacy lawyer.
- Which other commenters are already raising data security, so a comment
  can add to theirs instead of repeating it. The Bush Institute and Modern
  States reportedly raised privacy; I couldn't confirm the details.
