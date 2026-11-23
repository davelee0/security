# NYC Public Schools Student-Data Ecosystem Beyond Ed Law 2-d Disclosures

Research date: 2026-11-23. Method notes: www.schools.nyc.gov was fetched directly with curl. Three other hosts could not be fetched. www.nysed.gov failed TLS because the server does not send its GlobalSign intermediate certificate, and WebFetch could not resolve it. www.osc.ny.gov and chalkbeat.org were DNS-blocked. Claims from those sites come from search-result snippets or summaries, and are marked "(via search summary)". They should be checked against the primary PDF before publication.

## 1. NYSED Chief Privacy Officer annual reports: breach counts, complaints, enforcement, NYC incidents

### Takeaway
Statewide incident reports to NYSED rose fast: 384 in 2024 and 662 in 2025, up 72%. Roughly a third or more involve third-party contractors, and much of the rest is human error (paper records, misdirected emails, cloud-sharing permission errors). Enforcement takes the form of a small number of written complaint determinations, about 8 in 2024. I could not extract an NYC-specific breakdown because the PDFs were unreachable.

### Cited Findings
- 2024: 384 data incident reports from 100 educational agencies, up from 44 in 2020. About 152 involved third-party contractors. Paper records were a major source, roughly 40% (152 incidents). Phishing reports fell from 23 in 2023 to 10 in 2024. — [NYSED CPO 2024 Annual Report (via search summary)](https://www.nysed.gov/sites/default/files/programs/data-privacy-security/2024-data-privacy-and-security-annual-report_0.pdf)
  - Caution: the summary gives "152" for both the contractor count and the paper count. That may be a summarizer error, so verify against the PDF.
- 2024 complaints: 30 complaints, which produced 8 written determinations. — [NYSED CPO 2024 Annual Report (via search summary)](https://www.nysed.gov/sites/default/files/programs/data-privacy-security/2024-data-privacy-and-security-annual-report_0.pdf)
- 2025: 662 incident reports from 366 agencies, a 72.4% rise over 2024. 230 of the 662 involved unauthorized access or disclosure by a third-party contractor. Parent complaints more than doubled from 2024. Typical incidents included permission errors on cloud documents and emails that exposed multiple parents' addresses. — [NYSED CPO 2025 Annual Report (via search summary)](https://www.nysed.gov/sites/default/files/programs/data-privacy-security/2025-data-privacy-and-security-annual-report.pdf); [DataBreaches.net, Apr 6 2026](https://databreaches.net/2026/04/06/nys-school-data-incidents-rose-72-in-2025-with-44-reported-on-long-island/)
- The determinations page lists 2024 cases, for example a graduation photo posted without consent and a parent who received other students' test scores. At Success Academy's request (an NYC charter network), NYSED reviewed a December 2023 determination and issued a revised one in March 2024. — [NYSED Determinations of the CPO (via search summary)](https://www.nysed.gov/data-privacy-security/determinations-chief-privacy-officer)
- The annual reports index is at [NYSED Annual Reports page](https://www.nysed.gov/data-privacy-security/annual-reports-data-privacy-and-security). The 2023 report is at [2023 report PDF](https://www.nysed.gov/sites/default/files/programs/data-privacy-security/2023-data-privacy-and-security-annual-report__0.pdf).

### Inferences
- About 35% of 2025 statewide reports (230/662) were contractor incidents. That supports the project's focus on vendors, but most incidents are internal or human-error. A defense strategy should cover staff practices too: paper, email, Google Drive sharing. NYC's own 2021 Google Drive leak of about 3,000 students fits this pattern ([Chalkbeat 2021](https://chalkbeat.org/newyork/2021/8/5/22612388/data-breach-nyc-students-staff-google-drive)).
- Determinations are rare: 8 out of 30 complaints in 2024. NYSED enforcement is mostly advisory, with no fines.

### Gaps
- I could not open the PDFs, so I have no count of NYC DOE (or NYC charter) incidents per year and no list of NYC-specific determinations. Next step: open each PDF with a browser or a host that tolerates the incomplete certificate chain, then search for "New York City", "NYC", "Success Academy" and "DOE".
- I did not find the 2021 and 2022 report figures.

## 2. NYC DOE Data Security Incidents page (2022-2026)

### Takeaway
The DOE page lists only "incidents of note", which it defines as incidents where the DOE relied on a vendor for notifications. There are seven entries: Illuminate (2022, updated 2024), PETS (2023), MOVEit (2023), PowerSchool (2025), North Star Academy malware (2025) and Instructure Canvas (2026). The State Comptroller's audit counted 141 incidents from January 2023 to February 2025. The public page therefore shows only a small fraction of what happens.

### Cited Findings (all from the [DOE Data Security Incidents page](https://www.schools.nyc.gov/about-us/policies/data-privacy-and-security-policies/data-security-incidents), fetched 2026-11-23, unless noted)
- **The page's own definition:** "An incident of note is when the DOE relied on a vendor to assist with parental and student notifications."
- **Instructure Canvas (2026):**
  - Unauthorized activity on April 29, 2026, plus a related incident on May 7 in which the actor altered pages that logged-in users saw.
  - NYCPS suspended Canvas on May 8 and reinstated it on May 20 after working "closely with Instructure and NYC Cyber Command".
  - About 740 students and 48,000 staff were affected. Data exposed: name, school email, course enrollment, and for most students the student ID.
  - Instructure confirmed the scope on July 28. Letters went out the week of September 8, 2026. The Kroll monitoring enrollment deadline is December 7, 2026.
  - The system as a whole does not use Canvas, but "a small number of NYCPS schools and program offices" do.
- **PowerSchool SIS (2025):**
  - The breach was detected December 28, 2024. About 3,431 students and 317 staff were affected.
  - All affected students lost name, ID, date of birth, grade, graduation year, enrollment information and home address. Some also lost race/ethnicity, gender, parent contact details, emergency contact details and medical contact information.
  - Schools told their communities on February 10, 2025. Letters went out the week of April 1, 2025.
  - The system "does not use PowerSchool SIS", but some schools "independently chose" it.
- **North Star Academy MS/IS 340 malware (2025):**
  - Malware was discovered January 6, 2025. It copied about 10,000 files to an attacker server, about 250 of which held student data. 424 current and former students were affected.
  - Data included social-emotional learning (SEL) assessment scores, records of school social worker meetings, and compensatory special education service information.
  - NYCPS offered IDX monitoring, with a deadline of June 10, 2025.
- **Illuminate update (2024):**
  - In October 2023, Illuminate told NYCPS that more students and data elements were affected than first reported. About 387,000 additional students were newly notified, and about 94,000 received a second notice.
  - Data included GPA, reading level, test scores, disciplinary records, attendance and IEP status flag (yes/no only).
  - Illuminate still keeps the affected data because of "ongoing inquiries from government regulators, and class action lawsuits".
  - The original 2022 entry says about 800,000 students at about 700 schools were affected, the databases "were not encrypted", and the oldest data dates to 2016-17.
- **MOVEit (2023):**
  - About 19,000 files were copied on May 28, 2023. They included student evaluations, related-services progress reports and Medicaid reports for related services.
  - About 40,000 students were affected, plus about 170,000 staff and third-party evaluators. About 9,700 employee and evaluator SSNs were exposed. An earlier letter estimated about 45,000 students.
  - The DOE used MOVEit to transfer files "to and from vendors, including third-party special education service providers". The server remains offline.
  - The DOE says nothing could have prevented it (zero-day).
- **PETS (2023):**
  - A buggy update to the Personnel Eligibility Tracking System on February 7-8, 2023 let vendor users see and download other vendors' employee records. About 80,000 vendor employees were affected, and 8 vendor users accessed others' data.
  - The DOE said it was "considering enhancing PETS to restrict the personal information that a vendor can view and export."
- **Earlier incident not on the page:** In 2021, a Google Drive leak exposed data on about 3,000 students and 100 employees. — [Chalkbeat, Aug 5 2021](https://chalkbeat.org/newyork/2021/8/5/22612388/data-breach-nyc-students-staff-google-drive)

### Inferences
- The 2023 MOVEit breach and the PETS bug both expose a weakness in how DOE moves data between itself and its special-ed and related-services contractor ecosystem. The data involved was evaluations, Medicaid billing and provider credentials.
- Schools choosing tools on their own (PowerSchool, Canvas, and Illuminate before them) keeps producing breaches. The Comptroller found the same thing: the DOE does not know which schools use which systems (Section 5).
- The North Star case shows highly sensitive SEL and social-worker records sitting on local school computers.
- Illuminate-era data is still held by a vendor four years later because of litigation.

### Gaps
- The DOE does not publish its full incident log (the 141 incidents). A FOIL request for the log, by category and vendor, is a concrete research opportunity.

## 3. Data flows to small actors (Pre-K/3-K CBOs, DYCD after-school, related services, OPT/buses, food, SBHCs)

### Takeaway
DOE uses the same FERPA "school official" and Ed Law 2-d written-agreement framework for software vendors, community-based organizations (CBOs), researchers and related-services providers. Publicly funded Pre-K counts as a "school" under Part 121. The related-services disclosure page lists 43 providers, 40 of them commercial enterprises. Public material says almost nothing about DYCD (COMPASS/SONYC), school-based health centers (SBHCs) or OPT bus vendors.

### Cited Findings
- DOE discloses student data without consent to "software providers, community-based organizations, researchers, and related service providers" under written agreements. The page says its list is not "a comprehensive list of 'approved DOE vendors'", and parents must ask their principal which vendors their school uses. — [DOE Related Services Providers page](https://www.schools.nyc.gov/about-us/policies/data-privacy-and-security-policies/supplemental-information-for-parents-about-doe-agreements-with-outside-entities/related-services-providers)
- That page has 43 entries: 40 "Commercial Enterprise", 2 CBO/nonprofit and 1 LLC (my count, fetched 2026-11-23). Example: Ability OT/PT/SLP receives "age, educational goals, and medical history". — [same page](https://www.schools.nyc.gov/about-us/policies/data-privacy-and-security-policies/supplemental-information-for-parents-about-doe-agreements-with-outside-entities/related-services-providers)
- Under the regulations, "school" includes publicly funded pre-K programs. — [NYSED Parents' Bill of Rights / Part 121 (via search summary)](https://www.nysed.gov/data-privacy-security/bill-rights-data-privacy-and-security-parents-bill-rights)
- PETS holds personal data on vendor employees who serve students. About 80,000 such vendor employees were in the 2023 incident, which gives a sense of the contractor workforce's size. — [DOE incidents page](https://www.schools.nyc.gov/about-us/policies/data-privacy-and-security-policies/data-security-incidents)
- MOVEit carried related-services progress reports and Medicaid reports to and from special-ed providers. — [DOE incidents page](https://www.schools.nyc.gov/about-us/policies/data-privacy-and-security-policies/data-security-incidents)
- **Buses:**
  - A NYC Comptroller audit found the DOE "does not proactively or systematically use readily available global positioning system (GPS) or complaint data to oversee school bus vendors." That is an oversight finding, not a breach. — [NYC Comptroller bus services audit](https://comptroller.nyc.gov/reports/audit-report-of-the-new-york-city-department-of-educations-oversight-of-its-contracted-bus-services)
  - Coverage of the state audit notes that NYCPS manages data "from student addresses to bus routes". — [Route Fifty, May 2026](https://www.route-fifty.com/management/2026/05/state-audit-slams-nyc-schools-lack-student-data-privacy-oversight/413326/)
  - I found no reported OPT or bus-app breach.

### Inferences
- The related-services list (43) is much smaller than the actual universe of related-services and SETSS agencies and independent providers. Many small actors are likely covered by umbrella agreements or not listed at all. This needs verification.
- Small actors (Pre-K CBOs, SETSS agencies, bus companies) handle some of the most sensitive data (medical history, IEPs, home addresses, routes). They likely have the weakest security capacity, and NYSED's figures show that contractor and paper incidents dominate.

### Gaps
- I found nothing public on the data terms in DYCD COMPASS/SONYC/Summer Rising contracts or on whether DYCD signs Ed Law 2-d agreements. Summer Rising is a DOE-DYCD joint program, which makes this a likely seam.
- I found nothing on SBHC data governance (HIPAA vs FERPA split; NYC H+H and DOHMH operators), on school food data (CEP universal meals reduces free/reduced-price lunch data collection, not verified here), or on the OPT routing vendor and bus-company data rules.
- I did not find the number of Pre-K CBO sites (~1,129, per project context) or how NYCEECs access DOE systems.

## 4. Nonpublic schools: DOE ↔ nonpublic student data flows

### Takeaway
NYC DOE is the local education agency (LEA) for nonpublic students in special education and federal equitable services (Title I). That implies flows of evaluation, IEP and eligibility data. The city-funded security guard program (Local Law 2 of 2016, run by DCAS) verifies enrollment counts through BEDS and SIRS reports. I found no public documentation of data-sharing agreements between DOE and nonpublic schools.

### Cited Findings
- NYC DOE serves as the LEA for nonpublic students, "particularly in special education". Federal equitable services, including Title I, are delivered through DOE. DOE consults with private schools to gather information on parentally placed students. — [Bond Schoeneck & King, "Spotlight on NYC Private Schools"](https://www.bsk.com/uploads/Spotlight-on-New-York-City-Private-Schools.pdf)
- **Security guard reimbursement:** Local Law 2 of 2016, administered by DCAS (55 RCNY ch. 14).
  - Guard counts scale with enrollment, and enrollment is checked against the BEDS forms schools submit to NYSED.
  - A 2025 rule change requires the prior year's BEDS or SIRS reports. The rule was published May 30, 2025, with a hearing on June 30, 2025.
  - — [DCAS NPS FAQ](https://www.nyc.gov/site/dcas/business/non-public-schools-faq.page); [DCAS 2025 rule hearing](https://www.nyc.gov/assets/dcas/downloads/pdf/business/nps-reimbursement-program/public-hearing-2025-06-30-adoption-of-rules.pdf); [Council DCAS reimbursement report 2025](https://council.nyc.gov/budget/wp-content/uploads/sites/54/2025/12/Department-of-Citywide-Administrative-Services-School-Safety-Guard-Reimbursement-Report-PDF-1.pdf)
- NYSED's Nonpublic School Safety Equipment (NPSE) guidance, updated May 2024, is a related state funding stream. — [NYSED NPSE guidance](https://nysed.gov/sites/default/files/programs/nonpublic-schools/npse_guidance_yr10-updated-may-2024.pdf)

### Inferences
- Nonpublic schools are not "educational agencies" under Ed Law 2-d, so student data they hold falls outside NYSED CPO oversight. Data DOE generates about their students, such as CSE evaluations, IEPs, busing and Title I eligibility, is DOE data. This creates a jurisdictional gap worth mapping. It is an inference that needs legal confirmation.
- SIRS submissions contain incident data, though likely aggregate. Requiring them for guard reimbursement creates a new city data flow.

### Gaps
- No public source on the DOE-to-nonpublic data mechanics for CSE evaluations, nurse services, busing rosters, Title I eligibility or Mandated Services Reimbursement. FOIL and DOE Office of Nonpublic Schools guidance are the next sources.
- Nothing found on the Archdiocese of NY or Diocese of Brooklyn privacy policies or incidents.

## 5. NYC oversight bodies and advocates

### Takeaway
The strongest recent oversight came from the **State** Comptroller's April 2026 audit, not the NYC Comptroller. In 2026, the City Council (Education, Technology and Oversight committees) and the Panel for Educational Policy (PEP) became active on AI and privacy. The DOE Chief Privacy Officer, Dennis Doyle, admitted gaps in subcontractor visibility. Advocates Leonie Haimson (Parent Coalition for Student Privacy and Class Size Matters) and BetaNYC drive scrutiny. NYC Cyber Command plays an operational incident-response role for DOE.

### Cited Findings
- **NY State Comptroller audit, "Privacy and Security of Student Data" (NYCPS)**, issued April 23, 2026, covering 2020-2025 (via search summaries):
  - NYCPS policy does not fully align with NIST CSF.
  - 141 data security incidents involving student and staff information occurred from January 2023 to February 2025, from both vendors and internal systems.
  - About 25% of staff, nearly 43,000 employees, did not complete annual privacy training, and there is no system to cut off untrained users' access to sensitive data.
  - NYCPS does not know which schools use which systems or whether those systems hold sensitive data.
  - NYCPS agreed to update its data classification policy and track school-level technology use.
  - — [OSC audit page](https://www.osc.ny.gov/state-agencies/audits/2026/04/23/privacy-and-security-student-data); [OSC PDF sga-2026-23n6](https://www.osc.ny.gov/files/state-agencies/audits/pdf/sga-2026-23n6.pdf); [Chalkbeat May 4 2026](https://www.chalkbeat.org/newyork/2026/05/04/state-comptroller-audit-finds-student-data-privacy-gaps-in-nyc-schools/); [Route Fifty](https://www.route-fifty.com/management/2026/05/state-audit-slams-nyc-schools-lack-student-data-privacy-oversight/413326/); [GovTech](https://www.govtech.com/education/k-12/state-audit-finds-major-data-privacy-issues-at-nyc-schools)
  - Unclear: one summary says "the Education Department did not know about the breach until January 2025." This is garbled and possibly means NYSED was not notified of some incident until then. Verify in the PDF.
  - Chalkbeat's framing: auditors found no direct FERPA violation, but the gaps risk noncompliance.
- **Earlier State Comptroller audits of NYSED's own student-data security:** 2023 audit and September 2024 follow-up. — [OSC 2023](https://www.osc.ny.gov/state-agencies/audits/2023/05/16/privacy-and-security-student-data); [OSC 2024 follow-up](https://www.osc.ny.gov/state-agencies/audits/2024/09/26/privacy-and-security-student-data-follow)
- **NYC Comptroller:** I found no recent NYC Comptroller audit of DOE IT or data security. An advocate claimed in 2023 that apart from a 2013 SESIS audit, no independent assessment of DOE data security existed. This is an advocacy claim, not verified. — [DataBreaches.net](https://www.databreaches.net/nyc-parents-of-school-children-wake-up-and-speak-up-to-protect-your-childs-information)
- **City Council, June 24, 2026:** joint Education and Technology hearing, "Artificial Intelligence, Student Data, and Privacy in NYC Public Schools".
  - DOE agreed to publish the 6,491 public comments on the AI guidance and a written data classification policy "in coming months".
  - The chair requested data processing agreements (DPAs) for vendors including Amira.
  - Families have not been notified of the $17.25M Naviance data-breach settlement (Parent Coalition for Student Privacy claim).
  - Haimson testified that Google Gemini is enabled on thousands of elementary Chromebooks.
  - — [Legistar meeting 6/24/2026](https://legistar.council.nyc.gov/MeetingDetail.aspx?GUID=A5F0EBEC-3119-44ED-95B0-2027EDFDD22D&ID=1421969&Options=info%7C&Search=); [hearing summary (via search summary)](https://hearinghearings.nyc/hearings/committee-on-education-artificial-intelligence-student-data-and-privacy-in-nyc-public-schools-2026-06-24/); [News 12](https://brooklyn.news12.com/nyc-council-members-urge-pause-on-ai-rollout-in-schools-as-backlash-grows)
- **Int 0960-2026** would, among other things, require quarterly Chancellor reports on data breaches involving algorithmic tools used in schools. Status unknown. — [Legistar Int 0960-2026](https://legistar.council.nyc.gov/LegislationDetail.aspx?GUID=2CAE8FCE-0DBC-4C57-A2C0-38177CDF331B&ID=8073279&Options=&Search=)
- **Twenty-nine Council members called the draft AI guidance "flawed"**, and several, including both chairs, signed a letter seeking a two-year moratorium on student-facing AI. — [K-12 Dive](https://www.k12dive.com/news/nyc-schools-face-public-pressure-to-pause-ai-use-for-2-years/822673/); [Chalkbeat Mar 24 2026](https://www.chalkbeat.org/newyork/2026/03/24/preliminary-ai-policy-nyc-schools/)
- **Council Oversight and Investigations hearing on screen time and digital devices, September 15, 2026** (via search summaries):
  - DOE relies on the FERPA school-official exception rather than parental consent for vendor sharing.
  - CPO Dennis Doyle reportedly said he did not know which AI subcontractors are embedded in vendor products, and DOE does not demand to see vendor-subcontractor contracts.
  - — [hearing summary](https://hearinghearings.nyc/hearings/committee-on-oversight-and-investigations-screen-time-and-the-use-of-digital-devices-in-new-york-2026-09-15/); [Class Size Matters](https://classsizematters.org/nyc-council-hearing-on-screen-time-my-testimony-and-what-doe-did-and-did-not-reveal/)
  - Advocacy sources. Get the official transcript.
- **Panel for Educational Policy:**
  - Over 100 speakers demanded an AI moratorium at the PEP meeting on May 1, 2026. — [Chalkbeat May 1 2026](https://www.chalkbeat.org/newyork/2026/05/01/parents-demand-ai-moratorium-in-schools-during-marathon-panel-for-educational-policy-meeting/)
  - In August 2026, PEP rejected a $1.65M Oracle HR and enrollment-systems renewal (9-6-2, short of 13), citing data sensitivity and Oracle's AI business. It approved the extension in early October 2026. — [Chalkbeat Aug 28 2026](https://www.chalkbeat.org/newyork/2026/08/28/nyc-schools-ai-oracle-contract-hr-systems-board-pep-vote/); [Chalkbeat Oct 2 2026](https://www.chalkbeat.org/newyork/2026/10/02/nyc-schools-board-approves-oracle-contract-after-defeat/)
  - In December 2024, DOE withdrew a $1.9M AI reading-tutor (EPS Learning) contract after criticism. — [Chalkbeat Dec 18 2024](https://www.chalkbeat.org/newyork/2024/12/18/nyc-pulls-pep-contract-for-ai-reading-tutor-eps-learning/)
  - Haimson letter urging PEP to scrutinize contracts for privacy. — [Haimson Substack](https://leoniehaimson.substack.com/p/letter-to-the-members-of-the-panel)
- **Advocates' analyses:**
  - Class Size Matters analyzed privacy in the five AI high-school pilots and found that Intel AI-Ready Schools has no public privacy policy (Oct 13, 2026). — [CSM PDF](https://classsizematters.org/wp-content/uploads/2026/10/Privacy-concerns-with-AI-pilot-programs-10.13.26.pdf)
  - The Parent Coalition for Student Privacy says DOE declined to name AI products already in use, citing vendor NDAs. — [Chalkbeat Mar 2026 (via search summary)](https://www.chalkbeat.org/newyork/2026/03/24/preliminary-ai-policy-nyc-schools/)
  - BetaNYC explainer on the moratorium policy, Sept 4, 2026. — [BetaNYC](https://www.beta.nyc/2026/09/04/nyc-paused-ai-in-its-classrooms-here-is-what-the-policy-actually-says/)
- **NYC Cyber Command / OTI:**
  - DOE says it worked with NYC Cyber Command on MOVEit (2023) and Canvas (2026). Illuminate response coordination involved Cyber Command, the NYC Office of Information Privacy and the Law Department. — [DOE incidents page](https://www.schools.nyc.gov/about-us/policies/data-privacy-and-security-policies/data-security-incidents)
  - OTI held the T-Mobile laptop contract before Mayor Mamdani cancelled it. — [Chalkbeat Aug 27 2026](https://www.chalkbeat.org/newyork/2026/08/27/mamdani-cancels-adams-laptop-internet-plan-citing-waste/)
- **NY Attorney General** settlement with College Board over student data, a precedent for state enforcement. — [AG AOD PDF](https://ag.ny.gov/sites/default/files/settlements-agreements/college-board-student-privacy-aod.pdf)

### Inferences
- PEP has shown it will vote down data-heavy contracts. The monthly contracts agendas are the most direct public lever (Section 7).
- The CPO's admission that DOE cannot see subcontractors fits the project's finding that the encryption-checkbox disclosures are pro forma.

### Gaps
- Official Council hearing transcripts were not retrieved, and DOE testimony is reported secondhand.
- I did not confirm the status of Int 0960-2026 or of bills 684 and 853 mentioned in testimony.
- I did not find the formal MOU or scope of NYC Cyber Command's authority over DOE.

## 6. NYC Schools Account, device fleet, MySchools, AI tools: reported security issues

### Takeaway
I found no reported security vulnerability in the NYC Schools Account (NYCSA), MySchools or the iPad/Chromebook fleet. The live issues are governance ones: AI features on Chromebooks (Gemini), the cancelled 350,000-Chromebook plus T-Mobile plan, and the AI pilots.

### Cited Findings
- NYCSA is used as a password-reset channel for student accounts. The DOE told North Star families they could reset passwords via NYCSA or a self-service tool. — [DOE incidents page](https://www.schools.nyc.gov/about-us/policies/data-privacy-and-security-policies/data-security-incidents)
- Mayor Mamdani cancelled the Adams-era plan to buy 350,000 Chromebooks with T-Mobile internet in late August 2026, citing waste. PEP had approved it, but OTI held the contract. — [Chalkbeat Aug 27 2026](https://www.chalkbeat.org/newyork/2026/08/27/mamdani-cancels-adams-laptop-internet-plan-citing-waste/); [Route Fifty Dec 2025](https://www.route-fifty.com/digital-government/2025/12/inside-eric-adams-school-chromebook-spending-spree-new-york-city/410363)
- Haimson testified that Gemini is enabled on thousands of elementary Chromebooks, against DOE's characterization. — [hearing summary (via search summary)](https://hearinghearings.nyc/hearings/committee-on-education-artificial-intelligence-student-data-and-privacy-in-nyc-public-schools-2026-06-24/)
- **AI guidance, March 24, 2026:**
  - Tools that touch student data must pass the ERMA privacy and security review and sign a DPA. Unreviewed tools are barred from student or staff data.
  - Student data may not be used to train models.
  - — [DOE press release](https://www.schools.nyc.gov/home/2026/03/24/new-york-city-public-schools-announces-release-of-ai-guidance-for-educators-and-school-leaders); [DOE AI page](https://www.schools.nyc.gov/AI); [Chalkbeat](https://www.chalkbeat.org/newyork/2026/03/24/preliminary-ai-policy-nyc-schools/)
- ACLU (NYCLU) questioned student monitoring apps in NYC schools in 2021. — [Biometric Update 2021](https://www.biometricupdate.com/202111/aclu-chapter-wants-answers-on-student-monitoring-apps-in-nyc-schools)

### Inferences
- With no breach on record, the main risks for NYCSA and MySchools are concentration (one portal holding family contact, admissions, special-ed and lottery data) and the lack of any independent security assessment. I found no public penetration-test or audit result for either portal.

### Gaps
- I found no information on MySchools' vendor or hosting, the NYCSA authentication model, or the mobile device management (MDM) and telemetry settings on DOE iPads and Chromebooks. FOIL targets.

## 7. Upcoming decision points (late 2026-2027)

### Takeaway
Public input can matter at five points: (a) monthly PEP contract votes, including any return of Oracle and ed-tech renewals; (b) DOE's promised written data classification policy and publication of AI comments; (c) Council bills such as Int 0960-2026; (d) the scope and end of the 2026-27 AI moratorium plus the five high-school AI pilots; (e) NYCPS's corrective actions on the State Comptroller audit (OSC typically runs a follow-up audit). The device strategy is also open after the Chromebook plan was cancelled.

### Cited Findings
- PEP monthly contracts agendas are published as PDFs, for example the August 2026 final contracts agenda. — [Aug Panel Final Contracts Agenda](https://www.schools.nyc.gov/docs/default-source/data/final-contracts-agenda0cc94091-8c16-4349-89ed-1ecf23ba114d.pdf?sfvrsn=4d9368e_1)
- A PEP member said of Oracle: "if they put an Oracle contract in front of us a year from now, I'm not sure it would pass" (implying a renewal fight around fall 2027). — [Chalkbeat Oct 2 2026](https://www.chalkbeat.org/newyork/2026/10/02/nyc-schools-board-approves-oracle-contract-after-defeat/)
- DOE committed at the June 2026 hearing to publish the data classification policy and the 6,491 comments. — [hearing summary (via search summary)](https://hearinghearings.nyc/hearings/committee-on-education-artificial-intelligence-student-data-and-privacy-in-nyc-public-schools-2026-06-24/)
- In the audit response, NYCPS agreed to update data classification and build school-level technology-use tracking. — [Chalkbeat May 2026](https://www.chalkbeat.org/newyork/2026/05/04/state-comptroller-audit-finds-student-data-privacy-gaps-in-nyc-schools/)
- In March 2025, PEP held up $517M in instructional-technology spending after a losing bidder protested. Large IT contracts come back periodically. — [Chalkbeat Mar 27 2025](https://www.chalkbeat.org/newyork/2025/03/27/panel-for-educational-policy-votes-down-instructional-technology-contract)
- Canvas monitoring enrollment deadline: December 7, 2026. — [DOE incidents page](https://www.schools.nyc.gov/about-us/policies/data-privacy-and-security-policies/data-security-incidents)

### Inferences: concrete public-information research and help opportunities
1. **FOIL DOE's full incident log** (the 141 incidents from January 2023 to February 2025, plus later ones). Compare it with the seven "incidents of note" and with NYSED report counts.
2. **Pull NYC-specific data from the NYSED CPO 2023-2025 reports and the determinations index.** The PDFs are public but blocked in this environment.
3. **Track PEP contracts each month.** Cross-check every ed-tech or data vendor on the agenda against the project's 972-disclosure dataset (expired agreements, checkbox encryption claims). Publish a pre-vote brief for panel members.
4. **Track the commitments.** The data classification policy, 6,491 comments, Amira and other DPAs, and Naviance settlement notice were all promised in June 2026. Check whether they have been delivered.
5. **Check whether the 43 related-services disclosures cover the real provider universe.** Compare against PETS-registered vendors and SETSS agency lists. Look at the MOVEit and PETS lessons on file transfer to providers.
6. **Map gaps for small actors.** Request the data clauses in DYCD COMPASS/SONYC/Summer Rising contracts, Pre-K CBO (NYCEEC) contracts and SBHC MOUs via FOIL or the Checkbook NYC / PASSPort contract repositories.
7. **Map nonpublic-school data flows.** Cover CSE evaluations, Title I equitable services, busing and DCAS guard-program BEDS/SIRS data. Flag where Ed Law 2-d stops applying.
8. **Inventory AI features in existing tools** (Gemini on Chromebooks, AI inside approved vendors) against the 2026-27 moratorium. The CPO said DOE cannot see subcontractors.

### Gaps
- I did not find a calendar of 2027 RFPs (for example the next device procurement, NYCSA or MySchools vendor renewals, or OPT routing contracts).
- I did not confirm the dates of upcoming Council hearings or the OSC follow-up audit.
