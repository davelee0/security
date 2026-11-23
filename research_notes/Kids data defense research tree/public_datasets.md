# Public Datasets and Transparency Mechanisms for Defensive Measurement of Children's Data Protection

Researcher notes, compiled 2026-11-23. Method: web search only. Direct fetches of sdpc.a4l.org and www.nysed.gov failed (hosts not on this session's network allowlist), so the SDPC live counters and the NYSED 2023/2024 report figures were NOT read directly. Those hosts must be allowed before anyone verifies them. Items marked "[prior knowledge, not re-verified]" come from the researcher's background knowledge, not from a source fetched in this session. Treat them as leads.

## 1. SDPC Resource Registry and state DPA registries: what is public, how big, can it be analyzed in aggregate?

### Takeaway
The SDPC Resource Registry is the largest public corpus of signed K-12 data privacy agreements in the US. It has reportedly 130,000+ signed DPAs between 12,000+ districts and about 6,700 vendors, with signed agreement PDFs served at predictable public URLs, and a documented API. That makes it the single most promising dataset for a "2-d-style" aggregate study across states. The catch is that per-district public display is configurable by alliance admins, and the registry's own notice disclaims that it warrants legal compliance.

### Cited Findings
- Size: "the freely accessible SDPC Resource Registry hosts 130,000+ signed Data Privacy Agreements (DPAs) between more than 12,000 schools/districts and 6674 education application providers". The article is undated, so the figure may be from 2023-2024. — [WSIPC, NDPA v2 article](https://wsipc.org/news/version-two-of-sdpcs-national-data-privacy-agreement-is-available)
- The SDPC homepage shows live counters for agreements, districts and applications. The search did not capture the numbers. — [privacy.a4l.org](https://privacy.a4l.org/)
- Signed agreements and Exhibit E addenda are served as public PDFs at patterned URLs, e.g. `sdpc.a4l.org/agreements/2025-02-05_2948_1863_signed_agreement_file.pdf` and `sdpc.a4l.org/addendums/542140_10718_444.pdf`. That suggests the filenames encode date, district ID and vendor/resource ID. — [example agreement](https://sdpc.a4l.org/agreements/2025-02-05_2948_1863_signed_agreement_file.pdf); [example addendum](https://sdpc.a4l.org/addendums/542140_10718_444.pdf)
- SDPC publishes a "Resource Registry API developers guide". It suggests structured, machine-readable access exists, but the access terms (key required? members only?) were not verified. — [SDPC Resource Registry API developers guide (PDF)](https://files.a4l.org/privacy/SDPC-API/SDPC_Resource_Registry_API_developers_guide.pdf)
- State-specific login and search views exist (e.g. `login.php?state=MA`). The registry describes itself as a "Registry of executed agreements using the Standard Student Data Privacy Agreement" and says neither A4L nor SDPC warrants that stored agreements comply with every state law. — [sdpc.a4l.org MA view](https://sdpc.a4l.org/login.php?state=MA)
- Exhibit E mechanics: an originating district uploads its signed agreement, and other districts "subscribe" via an Exhibit E (General Offer of Terms) through an "Auto Exhibit E Creator". Admins can control whether Originating/Subscribing Exhibit Es are publicly displayed for specific districts, and can restrict access to non-members outside the alliance. — [SDPC Exhibit E training guide](https://files.a4l.org/privacy/SDPC_Training_Guides/TRAINING_GUIDE_Exhibit-Es.pdf); [Registry user role definitions](https://files.a4l.org/privacy/SDPC_Training_Guides/TRAINING_GUIDE_Registry_User_Role_Definitions.pdf); [Exhibit E technical guide](https://sdpc.a4l.org/exhibit_e_technical_guide.pdf)
- NDPA v2 (National Data Privacy Agreement version 2) exists, with a usage guide. A study could compare v1 and v2 clause adoption. — [NDPAv2 Usage Guide (PDF)](https://files.a4l.org/privacy/NDPA/NDPAv2_Usage_Guide_and_Development_Process.pdf)
- Regional cooperatives sign statewide or consortium DPAs. For example, ClassDojo signed with Texas's TEC (The Education Cooperative) in August 2025 so member districts can adopt it. This shows that one agreement can cover many districts. — [K-12 Dive press release, 2025-08-14](https://www.k12dive.com/press-release/20250814-classdojo-fast-tracks-districtwide-adoption-through-new-privacy-agreement-w/)
- Utah runs its DPA process through SDPC (the Utah Student Privacy Alliance). — [Utah USPA "the DPA process"](https://sites.google.com/schools.utah.gov/uspa/what-resources-are-available/the-dpa-process)
- Illinois (LTC Illinois) offers an SDPC add-on service for districts, which shows the registry is used for compliance with Illinois SOPPA. — [LTC Illinois SDPC](https://www.ltcillinois.org/services/sdpc/)
- Connecticut has no single statewide contract registry. Districts post contracts on their own websites (e.g. Hartford, North Canaan, Sterling), and vendors sign a state Student Data Privacy Pledge on the Connecticut Educational Software Hub (LearnPlatform). The state FAQ warns that signing the pledge without complying may be a violation. — [CT DAS Student Data Privacy](https://portal.ct.gov/das/ctedtech/commission-for-educational-technology/initiatives/student-data-privacy); [CT DAS SDP FAQ 2022 (PDF)](https://portal.ct.gov/-/media/DAS/CTEdTech/publications/2022/2-22-22_DAS_SDP_FAQ.pdf); [Hartford Public Schools](https://hartfordschools.org/o/hps/page/student-data-privacy); [North Canaan](https://northcanaanesct.schoolinsites.com/studentdataprivacy); [Sterling](https://www.sterlingpsct.gov/it/privacy); [CT Student Privacy Pledge](https://portal.ct.gov/-/media/das/ctedtech/documents/pa_16-189_ct_student_data_privacy_pledge.pdf)
- Connecticut statute: Conn. Gen. Stat. §10-234bb requires a written contract before sharing student data, and a 2018 report says the law requires districts to post contracts online. In 2018, districts struggled to comply. — [Justia §10-234bb](https://law.justia.com/codes/connecticut/title-10/chapter-170/section-10-234bb/); [CT Public 2018](https://www.ctpublic.org/education/2018-06-04/school-districts-struggle-to-comply-with-new-student-data-privacy-law)
- Some Florida districts (e.g. St. Johns) publish "Student Data Collected by Online Providers" pages. — [St. Johns County SD](https://www.stjohns.k12.fl.us/it/sdpa/)

### Inferences
- SDPC is effectively a national, cross-state analogue of the NYC 2-d dataset. Possible aggregate measures:
  - the share of agreements with modified (non-standard) clauses
  - vendor "subscribe-ability" (whether Exhibit E is offered)
  - the median time from originating to subscribing agreement
  - the number of distinct vendors per district, by state
  - the concentration of agreements among a few large vendors
  - stale agreements (vendors renamed or acquired)
- Patterned public PDF URLs make enumeration technically easy. Enumerating IDs that are not linked from public search pages, though, risks looking like "accessing what wasn't offered" and could expose districts that admins chose not to display. The responsible path is: (a) use only public search and listing pages or the documented API, (b) contact SDPC/A4L first to ask about terms and possibly get a sanctioned export, (c) publish only aggregates.
- Connecticut's district-by-district posting mandate creates a natural "compliance-with-posting-law" audit. You could measure, as a public-records presence check, what fraction of the roughly 200 CT districts have a reachable contracts page, and how current it is. Report only state-level rates.

### Gaps
- Current live SDPC totals, per-state breakdowns, and the registry's terms of use or robots policy could not be read (fetch blocked). Verify directly.
- Whether the SDPC API needs a member key.
- Washington, Massachusetts and Texas (TEC) registries: they appear to be SDPC state alliances (MA view confirmed; WSIPC is the WA alliance partner), but separate state-run registries were not confirmed.
- California AB 1584 (Ed Code 49073.1) sets contract requirements but, as far as was found, no public-posting mandate. Not verified in this session.
- No source was found that already analyzes the SDPC corpus in aggregate. That suggests the gap is real, but it is not proof.

## 2. Breach-notification datasets: can education and childcare breaches be identified?

### Takeaway
Several state AG portals are public and filterable enough to build a multi-state "education-sector breach" panel. Maine is the best of them because it has an explicit "Entity Type: Education" field and a total-affected count. California has a CSV export and also shows vendor-on-behalf-of-district filings (e.g. Illuminate). Washington lists data types and resident counts. Texas has a legally mandated public list, but entries are purged after one year, so it has to be archived continuously. NYSED's statutory annual reports give 2-d incident counts by year (44 in 2020, 71 in 2021, 38 in 2022). The K12 SIX incident map is historical only (2016-2022).

### Cited Findings
- **California AG**: a searchable breach list built from sample notices (required when more than 500 CA residents are affected). It includes school districts, county offices of education, charter operators, and vendor filings on behalf of districts. For example, "Illuminate Education, Inc. (on behalf of Orange Unified School District)" appears repeatedly with the same breach dates. The list can be filtered by name and is described as having a downloadable CSV. — [CA OAG breach list](https://oag.ca.gov/privacy/databreach/list); [example vendor-filtered page](https://oag.ca.gov/privacy/databreach/list?combine=DISA)
- **Washington AG**: an "interactive list of all notices submitted to our office since our state's notification laws took effect on July 24, 2015". Fields are organization, breach date, number of Washingtonians affected, and data types compromised. Applies when 500+ WA residents are affected. — [WA AG data breach notifications](https://www.atg.wa.gov/data-breach-notifications); [WA breach laws](https://www.atg.wa.gov/washington-s-data-breach-notification-laws)
- **Maine AG**: individual filing pages carry "Entity Type: Education", total persons affected, Maine residents affected, breach type and notice dates. Examples: Portland Public Schools (5,183 Maine residents, hacking, notices January 30, 2026); Charleston County SD, SC (20,653 total, 9 Maine); Prince George's County Public Schools, MD (99,543 total, notices February 2024); Edmonds SD (WA), Toledo Public Schools (OH), Indian Springs SD (IL). Because Maine requires notice even when only one Maine resident is affected, out-of-state districts appear in its data, which makes it a national dragnet. The search also surfaced at least one malformed or test entry, so data cleaning is needed. — [Maine AG example filing](https://www.maine.gov/agviewer/content/ag/985235c7-cb95-4be2-8792-a1252b4f8318/ba471657-be17-411d-a052-4855948d499c.html); [another](https://www.maine.gov/agviewer/content/ag/985235c7-cb95-4be2-8792-a1252b4f8318/e47f6a57-7231-4455-ba59-d66ac2769c8c.html)
- **Texas OAG**: HB 3746 (2021) requires the AG to keep a publicly accessible list, updated within 30 days of a notice. It shows entity name, information types, number of Texans affected, and whether consumers were notified. The reporting threshold is 250+ Texans within 30 days (amended effective 2023-09-01). The AG must remove an entity after one year if there are no further notices. Full reports may be obtained by open-records request. — [Texas OAG data breach reporting](https://texasattorneygeneral.gov/consumer-protection/data-breach-reporting); [Hunton on public listing amendment](https://www.hunton.com/privacy-and-cybersecurity-law-blog/texas-amends-breach-notification-law-to-require-public-reporting-of-breach-notices); [HB 3746 text](https://capitol.texas.gov/tlodocs/87R/billtext/html/HB03746F.htm)
- **Rhode Island AG**: publishes a yearly list of breach notices (2025 entries through September 2025). Applies when 500+ RI residents are affected, within 45 days. — [RI AG data breach notifications](https://riag.ri.gov/news-events/data-breach-notifications)
- Vermont is listed among the states requiring AG notice regardless of the number affected (2019 source, may be outdated). Vermont's portal itself was not surfaced. — [IRMI 2019](https://irmi.com/articles/expert-commentary/breach-notification-laws-state-attorney-general-or-regulator-notice)
- **NYSED CPO annual reports** (statutory under Ed Law 2-d) must cover activities, "the number and disposition of reported breaches", and complaints. Reports are posted for 2016-17 through 2024. Data incident reports: 44 (2020), 71 (2021), 38 (2022). The 2022 figure includes 11 noted on behalf of mostly charter schools after the Illuminate Education breach. The 2023 and 2024 counts were not retrieved. — [NYSED 2024 report (PDF)](https://www.nysed.gov/sites/default/files/programs/data-privacy-security/2024-data-privacy-and-security-annual-report_0.pdf); [2023](https://www.nysed.gov/sites/default/files/programs/data-privacy-security/2023-data-privacy-and-security-annual-report__0.pdf); [2022](https://www.nysed.gov/sites/default/files/programs/data-privacy-security/annual-report-on-data-privacy-and-security-2022_0.pdf); [2021](https://www.nysed.gov/sites/default/files/programs/data-privacy-security/nysed_data-privacy-and-security-annual-report_2021_0.pdf)
- **NYSED CPO determinations** on parent complaints are published. For example, a June 2025 determination found that a teacher's class-wide message disclosing PII was a reportable 2-d breach. These are a codable corpus of complaint outcomes. — [NYSED Determinations of the CPO](https://nysed.gov/data-privacy-security/determinations-chief-privacy-officer)
- **K12 SIX K-12 Cyber Incident Map** is archived. It covered 1,619 incidents from 2016-2022, based on voluntary public disclosures, and K12 SIX itself said it "dramatically understates" the problem. — [K12 SIX map page](https://www.k12six.org/52133ded-1103-4afc-a02e-e83b1e580384)
- **Successor data: CIS/MS-ISAC K-12 reports.** The 2025 report covers 5,000+ K-12 organizations from July 2023 to December 2024, with 82% experiencing cyber-threat impacts. The 2026 report (with CoSN, released November 2026) found 51% of schools and districts reported an incident in the past 12 months, and 34% reported operational impacts. These are survey and telemetry aggregates, not incident-level open data. — [CIS 2025 report](https://www.cisecurity.org/insights/white-papers/2025-k12-cybersecurity-report); [CIS State of K-12 Cybersecurity 2026](https://www.cisecurity.org/insights/white-papers/state-k-12-cybersecurity-report-2026); [EdTech Magazine, 2026-11-19](https://edtechmagazine.com/k12/article/2026/11/new-report-reveals-half-k-12-schools-had-cybersecurity-incident-last-year)

### Inferences
- Since the K12 SIX map stopped in 2022, there has been no open, incident-level, multi-state K-12 breach dataset. A reproducible "K-12 breach panel" fills that gap: Maine (Entity Type = Education), plus CA, WA, TX (archived weekly to beat the one-year purge), RI and NYSED annual totals. Classify each entry as district versus vendor-on-behalf-of-district. The vendor share of student-record exposure (Illuminate 2022, PowerSchool 2024-25) is the systemic story.
- Maine's "notify even one resident" rule turns its portal into a national sampling frame for large district and vendor breaches.
- Childcare and youth-program breaches would need keyword classification (e.g. "child care", "daycare", "camp", "YMCA", "Boys & Girls"). No portal has a childcare category, as far as was found.

### Gaps
- The Vermont, Massachusetts (OCABR breach reports), Oregon, Indiana, Montana and New Hampshire portals were not checked in this session.
- Whether California's CSV includes industry codes (it appears not to). Classification would be manual or by keyword.
- Exact NYSED 2023 and 2024 incident counts and cause breakdowns (fetch blocked).
- Terms of use for each AG portal were not reviewed. They are generally public records, but rate limits apply.

## 3. Federal datasets: SGO list, Form 990s, ESA vendor contracts and audits, USASpending and E-Rate

### Takeaway
The Federal Scholarship Tax Credit (FSTC) starts January 1, 2027. The IRS already lists participating states (as of 2026-10-22), and SGOs will become a new, enumerable universe of organizations holding children's application data. Their Form 990s, available via ProPublica Nonprofit Explorer, show size and governance but not privacy practices. No sources were found on ESA vendor (e.g. ClassWallet) privacy audits. This area is mostly unexplored.

### Cited Findings
- FSTC: starting 2027-01-01, individuals can claim a credit of up to $1,700 for contributions to Scholarship Granting Organizations. Students in non-participating states are ineligible. The IRS maintains an FSTC page and a participating-states page (as of October 22, 2026: Alabama, Alaska, Arkansas, Colorado, Florida, Georgia, ...). — [IRS FSTC](https://www.irs.gov/charities-non-profits/federal-scholarship-tax-credit-fstc); [IRS participating states](https://www.irs.gov/ru/government-entities/federal-state-local-governments/federal-scholarship-tax-credit-fstc-participating-states)
- State opt-in counts vary by date and source: "over two dozen" (Bloomberg Government, May 2026) and 31 states (EdWeek tracker). Minnesota and Wisconsin governors declined. — [Bloomberg Government](https://news.bgov.com/daily-tax-report/dozens-of-states-opt-into-new-private-school-tax-credit-program); [EdWeek tracker](https://www.edweek.org/policy-politics/federal-private-school-choice-which-states-are-opting-in/2025/08); [K-12 Dive](https://www.k12dive.com/news/27-states-opting-into-federal-school-choice-program-IRS-Congress/818087/); [Ballotpedia](https://ballotpedia.org/State_participation_in_the_federal_K-12_education_tax_credit_program)
- [prior knowledge, not re-verified] ProPublica Nonprofit Explorer offers free search and a JSON API for IRS Form 990 data, including e-filed 990 XML. USAC's E-Rate Open Data portal (opendata.usac.org) publishes Form 470/471 applications and funding commitments by school and district, including the service and vendor (SPIN) for internet access and internal connections. The FCC's Schools and Libraries Cybersecurity Pilot Program (approved 2024) funds cybersecurity services for selected applicants, and its participant lists may be public.

### Inferences
- SGO analysis could start once the IRS publishes the SGO list (2027+). For each SGO, check public, non-intrusive signals: whether a privacy policy exists and what it says about data sale and retention, whether the application portal is operated by a third party, and whether the 990 discloses a technology vendor. Report only aggregates. Small SGOs should not be named, per the project boundary.
- E-Rate data could support a "what share of districts buy any cybersecurity service" analysis. That speaks to protection of children's data indirectly.
- ESA programs (AZ, FL, etc.) use payment-platform vendors that hold family PII. Public-records requests for vendor contracts, DPAs, and audit or SOC reports are a likely route, but nothing on this was found in this session.

### Gaps
- Whether the IRS will publish SGO lists with contact or URL fields, and when.
- ESA vendor contracts and audits (ClassWallet, Odyssey, Student First Technologies): no search results. Needs targeted searches or records requests.
- USASpending relevance was not researched.

## 4. App and privacy measurement datasets

### Takeaway
Three strong datasets exist:
- Internet Safety Labs' 2022 K-12 EdTech Safety Benchmark: about 1,300-1,700 apps from 663 schools, with open data under CC BY-NC-SA 4.0.
- The Utah State Board of Education/BYU/ISL 2023-25 investigation, the first state-run test of DPA promises against observed app behavior.
- Common Sense Privacy ratings.

Academic work shows Google Play Data Safety labels are frequently inaccurate. The biggest open gap is a repeat measurement: no 2025-26 national refresh of ISL's benchmark was found.

### Cited Findings
- ISL 2022 benchmark: sample of 663 K-12 schools (13 per state plus DC). The first findings report says 1,357 apps were tested with 88,000+ data points. Other ISL materials say 1,700+ apps and 120,000+ data points (the PEPR '24 slides say 1,722). 96% of apps shared children's data with third parties, and 23% included ads. — [ISL national findings part 1 (PDF, Dec 2022)](https://internetsafetylabs.org/wp-content/uploads/2022/12/2022-k12-edtech-safety-benchmark-national-findings-part-1.pdf); [THE Journal 2022-12-13](https://thejournal.com/articles/2022/12/13/report-nearly-all-school-apps-send-kids-data-to-third-parties.aspx); [PEPR '24 slides](https://usenix.org/system/files/pepr24_slides-levasseur_0.pdf)
- ISL data is published, with a Tableau dashboard and the ISOC Foundation-funded "findings data publication". The licence is CC BY-NC-SA 4.0. — [ISOC Foundation project](https://www.isocfoundation.org/project/us-k12-edtech-safety-benchmark-findings-data-publication/); [ISL 2022 benchmark page](https://internetsafetylabs.org/resources/reports/2022-us-k12-edtech-benchmark/)
- ISL report 3 (February 2024) analyzes app safety, school website safety and school technology practices across demographic lenses. A 2023 analysis found most school apps advertise to kids even in SOPIPA states. A 2025 ISL post found that unvetted off-the-shelf apps outnumber licensed apps about 2 to 1. — [ISL Findings Report 3 (PDF)](https://internetsafetylabs.org/wp-content/uploads/2024/02/2022-K-12-EdTech-Safety-Benchmark-Findings-Report-3.pdf); [THE Journal 2023-07-29](https://thejournal.com/articles/2023/07/29/majority-of-school-apps-advertising-to-kids-even-in-sopipa-states.aspx); [ISL blog, unvetted apps 2:1](https://internetsafetylabs.org/blog/research/2022-k-12-edtech-benchmark-revisited-unvetted-off-the-shelf-apps-outnumber-licensed-apps-2-to-1/)
- Utah investigation (USBE with BYU and ISL, dated August 2025): network-traffic analysis of 100 EdTech apps from 2023-2025, compared against DPAs.
  - GovTech: of 85 apps with standard DPAs, 44 (52%) collected at least one data type not permitted by the agreement, and 11 (13%) shared an unpermitted element with a third party.
  - KSL reports "36% ... sharing data with advertisers". This conflicts with GovTech's 13%, so check the primary PDF.
  - The findings led to Utah H.B. 55 (amending §53E-9-309, effective July 1, 2026) and a study mandate (§53E-3-527).
  - [USBE report (PDF)](https://www.schools.utah.gov/studentdataprivacy/files/Utah%20EdTech%20App%20Data%20Collection%20and%20Sharing%20-%202023-25%20Investigation.pdf); [GovTech](https://www.govtech.com/education/k-12/what-happened-when-utah-put-ed-tech-privacy-promises-to-the-test); [KSL](https://www.ksl.com/article/51611276/how-a-byu-study-led-utah-lawmakers-to-pass-a-student-data-privacy-law); [Malwarebytes, Aug 2026](https://www.malwarebytes.com/blog/privacy/2026/08/popular-school-apps-may-be-sharing-student-data-with-advertisers); [Utah Code 53E-3-527](https://le.utah.gov/xcode/Title53E/Chapter3/C53E-3-S527_2026050620260701.rtf)
- ISL presented to the Vermont legislature (H.650, February 2026). This indicates policy demand for measurement in other states. — [LeVasseur testimony slides](https://legislature.vermont.gov/Documents/2026/Workgroups/House%20Commerce/Bills/H.650/Witness%20Documents/H.650~Lisa%20LeVasseur~Testimony%20slides~2-6-2026.pdf)
- Common Sense: the 2023 State of Kids' Privacy report covered 200+ apps and platforms and found 73% monetize kids' or families' data. Ratings are Pass, Warning or Fail and were integrated into app reviews in September 2023. They are free for parents and educators. Earlier State of EdTech Privacy reports (2018, 2019) found most edtech failed minimum criteria. — [Common Sense 2023 State of Kids' Privacy](https://www.commonsensemedia.org/research/2023-state-of-kids-privacy); [press release](https://www.commonsensemedia.org/press-releases/most-apps-used-by-kids-are-likely-sharing-and-selling-their-data); [EdWeek 2023-07](https://edweek.org/technology/most-tech-companies-profit-off-student-data-even-if-they-say-otherwise-report-finds/2023/07); [privacy.commonsense.org publications](https://privacy.commonsense.org/resource/publications)
- Google Play Data Safety labels (in effect since July 2022, self-reported by developers):
  - USENIX Security 2024: of about 5,000 apps, 81% misrepresent their data collection, and 59% of discrepancies come from third-party libraries. — [Arkalakis et al., USENIX Sec '24](https://usenix.org/system/files/sec24fall-prepub-399-arkalakis.pdf)
  - A study of 7,377 child-directed Android apps found potential COPPA violations, SDK misconfigurations, and label disclosure mistakes. — [NSF PAR](https://par.nsf.gov/servlets/purl/10591795)
  - Mozilla (2023) found labels false or misleading in about 80% of 40 top apps. — [Mozilla Foundation](https://www.mozillafoundation.org/ca/blog/mozilla-study-data-privacy-labels-for-most-top-apps-in-google-play-store-are-false-or-misleading/)
  - A 2026 arXiv study of children's games found location disclosures had the highest inconsistency (56.1%). — [arXiv 2603.23935](https://arxiv.org/abs/2603.23935)
- Learn21's "Scary Apps" list flags vendors that refuse to sign DPAs. — [GovTech](https://www.govtech.com/education/k-12/scary-apps-list-calls-out-poor-student-data-privacy-policies)

### Inferences
- Combining datasets is the novel move. Join SDPC DPA presence (which vendors signed what) with Play/App Store label claims and with ISL or Utah observed behavior, at the vendor level. Then report the share of DPA-covered apps whose public store labels contradict the DPA's data-sale and advertising clauses. This uses only public documents (labels and DPAs) and no traffic interception.
- Observed-traffic testing (ISL/Utah style) means running apps on your own devices. That is allowed under the project boundary ("systems you own"), but it raises the ethical bar. Partnering with ISL or a university is advisable.

### Gaps
- Whether ISL has published a 2024-2026 national refresh.
- Bulk-access terms for Common Sense ratings (no API or terms found).
- No public dataset of edtech Play/App Store labels specifically. It would have to be assembled.

## 5. Ethics and methods: precedents for responsible aggregate measurement; disclosure; legality of scraping government sites

### Takeaway
The Menlo Report remains the baseline framework. A January 2026 IETF/IRTF draft on safe Internet measurement and a 2025 interview study add current guidance. US case law (Van Buren 2021; hiQ v. LinkedIn, 9th Cir. 2022) makes CFAA liability unlikely for scraping pages that are publicly accessible without authentication. Terms-of-use (contract) claims and the boundary against touching non-public URLs still matter.

### Cited Findings
- The Menlo Report is the most widely cited measurement-ethics framework, adapted from the Belmont Report. A 2025 study of 16 researchers found most rely on personal reasoning and informal norms, and IRBs often mark measurement research "exempt". — [arXiv 2511.10408 (2025)](https://arxiv.org/html/2511.10408v1); [McDaniel et al. ethics paper (2023)](https://patrickmcdaniel.org/pubs/ethics23.pdf)
- The IRTF PEARG draft "Safe Internet Measurement" (rev. 14, about January 2026) is meant to help equip review boards to evaluate measurement methods. It is not a substitute for ethics review. — [IETF datatracker](https://datatracker.ietf.org/doc/html/draft-irtf-pearg-safe-internet-measurement-14)
- hiQ v. LinkedIn: after the Supreme Court GVR'd the case in light of Van Buren, the 9th Circuit (April 2022) held that scraping publicly available data likely is not "without authorization" under the CFAA. Commentary says CFAA claims are doubtful unless access barriers such as authentication are circumvented. — [9th Cir. opinion](https://govinfo.gov/content/pkg/USCOURTS-ca9-17-16783/pdf/USCOURTS-ca9-17-16783-1.pdf); [Proskauer](https://www.proskauer.com/blog/taking-cue-from-the-supreme-courts-van-buren-decision-ninth-circuit-releases-new-opinion-holding-scraping-of-publicly-available-website-data-falls-outside-of-cfaa); [EFF](https://www.eff.org/deeplinks/2021/07/eff-ninth-circuit-recent-supreme-court-decision-van-buren-does-not-criminalize-web)
- [prior knowledge, not re-verified] Precedent measurement studies that published aggregates and notified operators:
  - the Princeton Web Transparency and Accountability Project's 1-million-site tracking census (Englehardt and Narayanan, CCS 2016, OpenWPM)
  - Internet-wide HTTPS and TLS adoption studies (e.g. Felt et al., USENIX Security 2017)
  - academic DMARC/SPF adoption measurements
  - ZMap/Censys scanning norms (opt-out lists, rate limits, identifying scan hosts)
  The common norms are: rate limits, identification of the researcher, opt-out paths, aggregate publication, and private notification before naming.

### Inferences
- For this project: stick to pages linked from public navigation or documented APIs; never enumerate unlinked IDs (e.g. SDPC PDF numbers); rate-limit; identify the crawler with a generic contact; keep only aggregates; give agencies such as NYSED or SDPC advance notice of systemic findings.
- Government sites carry no contract-based terms-of-use risk comparable to LinkedIn's, but some (e.g. SDPC, a private nonprofit) do. Read and record the terms before scraping.

### Gaps
- No primary-source search on coordinated vulnerability disclosure norms (ISO 29147, CISA CVD) as applied to systemic, non-vulnerability findings.
- State-specific computer-crime statutes and government-site terms of use were not reviewed.
- 2023-2026 developments in scraping case law (e.g. Meta v. Bright Data, 2024) were not searched.

## 6. Parent-facing transparency: what exists and what is missing

### Takeaway
Parents today depend on district-by-district app lists of very uneven quality (CT-posted contracts, SFUSD's core-suite list, Adams 14's list, NYC's 2-d supplemental pages) and on advocacy spreadsheets such as Student Privacy Matters' NYC approved-products sheet. Nothing found lets a parent enter a school and see every vendor, its DPA, its breach history, and its observed behavior. That cross-referenced "vendor passport" is the main missing piece.

### Cited Findings
- Student Privacy Matters, co-sponsored by the Parent Coalition for Student Privacy, published a spreadsheet of edtech products approved for NYC schools that flags products lacking privacy agreements on the NYC DOE page and raises concerns about PowerSchool. The search snippet dates it November 2026. — [studentprivacymatters.org](https://studentprivacymatters.org/?author=1)
- The 2017 Parent Toolkit for Student Privacy (Parent Coalition and CCFC/Fairplay) includes an app-inventory template and questions for parents. — [Parent Toolkit (PDF)](https://fairplayforkids.org/wp-content/uploads/archive/PTSP_Complete_English.pdf)
- District examples: SFUSD "Core Suite of Apps" (apps not on the list should not be used); Adams 14 (CO) app list; Connecticut district contract postings (see Section 1). — [SFUSD](https://www.sfusd.edu/es/node/6634); [Adams 14](https://sites.google.com/adams14schools.org/applist/student-data-privacy)
- ISL found that schools' actual app usage far exceeds what manual counts suggested, and that unvetted apps outnumber licensed ones about 2:1. This implies official app lists undercount the vendors that actually touch student data. — [ISL blog](https://internetsafetylabs.org/blog/research/2022-k-12-edtech-benchmark-revisited-unvetted-off-the-shelf-apps-outnumber-licensed-apps-2-to-1/)

### Inferences
- Missing pieces:
  1. a cross-district, normalized vendor-to-DPA-to-breach lookup
  2. a "freshness" signal showing when the district list was last updated
  3. flags for vendors that appear in AG breach portals
  4. discrepancy flags where store labels conflict with DPA terms
- A volunteer project could build (1)-(3) entirely from public data (SDPC, district pages, AG portals). It could publish state or district aggregates and let parents look up vendors, which are companies, not small organizations.

### Gaps
- No survey found of how many US districts publish an app or vendor list at all. This would itself be a measurable, aggregate statistic.
- NYC/DOE's own parent-facing tooling beyond 2-d pages was not re-checked here.

---

## Most promising analyses nobody appears to have done (synthesized from above; to be verified)
1. **SDPC national DPA census**: clause modification rates, Exhibit E availability, vendor concentration, and state coverage, using public search and the documented API only, with A4L consulted first. (Section 1)
2. **Post-2022 open K-12 breach panel**: Maine (Education entity type), CA, WA, TX (weekly archiving to beat the one-year purge), RI and NYSED annual totals. Headline metric: the vendor-caused share of student records exposed. (Section 2)
3. **Connecticut posting-compliance audit**: the share of districts with a reachable, current contracts page, about 8 years after the mandate. Report state rates only. (Section 1)
4. **DPA-versus-store-label consistency**: for vendors in SDPC, do Play/App Store data-safety claims contradict their DPAs on ads, sale and sharing? Public documents only. (Section 4)
5. **NYSED CPO determinations corpus**: code all published determinations by violation type and outcome, and pair them with annual-report counts. (Section 2)
6. **Pre-launch SGO privacy baseline (2027)**: once the IRS lists SGOs, measure privacy-policy presence and terms in aggregate. (Section 3)
