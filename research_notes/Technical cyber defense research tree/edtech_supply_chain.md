# Edtech and Vendor Supply Chain: Technical Attack Surface for Small Schools, Childcare and Youth Programs

Research date: 2026-11-23. This builds on `Kids data defense research tree/threat_landscape.md`, `ai_security.md`, `public_datasets.md` and `nyc_data_flows.md`. Those notes already cover the following, which this file does not repeat: PowerSchool's follow-on extortion, the LineLeader exposure, the NYC DOE incident page (Canvas, PowerSchool, MOVEit, Illuminate, PETS), the Utah DPA test and ISL's findings.

Method note: direct page fetching failed for most hosts in this session (Wikipedia, SecurityWeek and scotthelme.co.uk did not resolve). Most findings below therefore rest on search-result summaries of the cited URLs. Where a summary paraphrased a primary document I could not open, I say so. Dates are flagged in brackets.

---

## 1. Root causes of major edtech breaches, 2022-2026: what was the common failure?

### Takeaway
Almost every major incident was a failure of the vendor's trust boundary, not of the school. The recurring pattern was one of the following:
- a privileged support or maintenance path guarded by a password only (PowerSchool)
- a support or helpdesk workflow that let a low-trust tenant reach a high-trust staff session (Canvas 2026)
- unencrypted cloud storage or public buckets (Illuminate, Raptor, LineLeader)
- broken API authorization on a parent or self-signup portal (Edulog)
- a single internet-facing file-transfer or third-party component (MOVEit 2023, Frontline 2026)

The common thread: vendors aggregate many schools' data behind one support, API or storage plane. That plane had weaker controls than the customer-facing login, and schools could neither see nor restrict it.

### Cited Findings

**PowerSchool [Aug-Dec 2024; reports Mar 2025 and Nov 2025]**
- CrowdStrike's report, published by PowerSchool, says the attacker used a compromised support credential to run "Maintenance Remote Support" operations in PowerSource, the customer support portal, between Dec 19 and Dec 28, 2024. PowerSource lets technicians with the right permissions reach customer SIS database instances. — [PowerSchool-hosted CrowdStrike report](https://www1.powerschool.com/wp-content/uploads/2025/03/PowerSchool-CrowdStrike-Final-Report.pdf)
- The same credentials were used to access PowerSource from Aug 16 to Sep 17, 2024. CrowdStrike could not link that activity to the December attacker because PowerSchool's logs did not go back far enough. — [TechCrunch, Mar 10 2025](https://techcrunch.com/2025/03/10/hacker-accessed-powerschools-network-months-before-massive-december-breach/); [BleepingComputer](https://www.bleepingcomputer.com/news/security/powerschool-previously-hacked-in-august-months-before-data-breach/); [SecurityWeek](https://www.securityweek.com/powerschool-portal-compromised-months-before-massive-data-breach/)
- **Was MFA absent?** Yes, on the path that was used.
  - Alberta's privacy commissioner report F2025-IR-02 [Nov 2025] says PowerSchool implemented MFA for PowerSource and cloud SIS instances *after* the breach. — [Alberta OIPC report](https://oipc.ab.ca/wp-content/uploads/2025/11/FINAL-Investigation-Report-Regarding-PowerSchool-Breach-FOIP2025-IR-02.pdf)
  - Per a review of the Canadian commissioners' reports, the Ontario commissioner called the missing MFA on a *former subcontractor's* account a contributing factor, and PowerSource reportedly could not support MFA at the time. — [Substack review of the Canadian reports](https://solomonh.substack.com/p/reports-from-two-canadian-provincial?action=share) (secondary source)
  - Caveat: one analysis says the evidence supports password-only access on the path used, not a claim that all PowerSchool systems lacked MFA. — [Security Blueprints](https://securityblueprints.io/data-breaches/powerschool-student-information-system-data-breach-december-2024/)
- **Remediation reported:** VPN plus SSO and MFA in front of PowerSource, and maintenance access moved to a separate platform with mandatory MFA. — [TechTarget explainer](https://www.techtarget.com/whatis/feature/PowerSchool-data-breach-Explaining-how-it-happened); a GitHub student case study also repeats this (low-quality source).
- **District-side "remote support" toggle:**
  - District notes from PowerSchool's Jan 8, 2025 webinar tell on-premises districts to turn off maintenance access and contact their customer success manager to re-enable it. — [HCUSD2 webinar notes PDF](https://hcusd2.socs.net/vimages/shared/vnews/stories/677fe24aa9554/Notes%20taken%20from%20PowerSchool%20webinar%20on%20Jan%208th%202025.pdf)
  - Commentary claims PowerSchool switched remote support from default-on to default-off. A secondhand forum claim that the toggle was a "placebo" for on-premises instances is **unverified**. — [Datapath analysis](https://www.mydatapath.com/industry-news/powerschool-breach-k12-vendor-access-lessons/); [hexbear forum comment](https://hexbear.net/comment/5806733)
  - The Alberta report has a section titled "Remote support permissions", but I could not read it.

**Illuminate Education [breach Dec 2021-Jan 2022; FTC action Dec 2025; state AGs Nov 2025]**
- FTC complaint: Illuminate stored student data in plain text in AWS S3 until at least January 2022, and ignored a third-party vendor's warnings about vulnerabilities. — [FTC press release, Dec 2025](https://www.ftc.gov/news-events/news/press-releases/2025/12/ftc-takes-action-against-education-technology-provider-failing-secure-students-personal-data); [The Register, Dec 2 2025](https://www.theregister.com/security/2025/12/02/ftc-slaps-edtech-vendor-after-breach-exposes-10m-students/1958090) (about 10M students)
- The proposed order requires Illuminate to:
  - stop misrepresenting its security practices and breach-notification timing
  - delete unnecessary data
  - publish and follow a retention schedule
  - run an information security program for 10 years

  It imposes no fine. — [Covington Inside Privacy](https://www.insideprivacy.com/united-states/federal-trade-commission/ftc-announces-10-year-information-security-consent-orders-with-illuminate-education-and-illusory-systems/); [Hunton](https://www.hunton.com/privacy-and-cybersecurity-law-blog/ftc-reaches-settlement-with-ed-tech-provider-over-breach-of-student-data)
- A $5.1M settlement with the CA, CT and NY Attorneys General was announced Nov 6, 2025. One law-firm post says the FTC order was finalized Jun 5, 2026 with revised deletion and retention wording. I could not confirm the finalization directly. — [CommLaw Group](https://commlawgroup.com/2025/ftcs-proposed-consent-order-with-illuminate-education/); [Mondaq](https://www.mondaq.com/unitedstates/education/1717146/ftcs-proposed-consent-order-with-illuminate-education-a-tale-of-two-enforcement-approaches)
- **Note for small orgs:** NYC said Illuminate still held the affected data years later because of regulator inquiries and litigation. Retention by design means a breach keeps exposing data long after the contract ends. (See `nyc_data_flows.md`.)

**MOVEit Transfer [May-Jun 2023]**
- Cl0p mass-exploited CVE-2023-34362 (SQL injection, CVSS 9.8) in Progress MOVEit Transfer, an internet-facing managed file-transfer server. — [Help Net Security](https://www.helpnetsecurity.com/2023/09/25/clearinghouse-moveit-breach/); [Higher Ed Dive timeline](https://www.highereddive.com/news/moveit-breach-timeline/688058/); [K-12 Dive timeline](https://www.k12dive.com/news/moveit-breach-timeline/687963/)
- The National Student Clearinghouse was hit via MOVEit. About 900 institutions were affected; a Higher Ed Dive analysis counts 1,009 downstream institutions. Many schools learned of it from NSC or TIAA, not from their own monitoring. — [Security Affairs](https://securityaffairs.com/151281/data-breach/national-student-clearinghouse-data-breach.html); [Higher Ed Dive](https://www.highereddive.com/news/move-it-900-colleges-breach/694835/)
- NYC DOE used MOVEit to exchange special-education and related-services files with vendors. About 19,000 files were taken and about 40,000-45,000 students affected. — [BleepingComputer](https://www.bleepingcomputer.com/news/security/hackers-steal-data-of-45-000-new-york-city-students-in-moveit-breach/amp/); details in `nyc_data_flows.md`

**Raptor Technologies [found Dec 2023, reported Jan 2024]**
- Jeremiah Fowler (via vpnMentor) found three storage buckets with no password holding about 4M records, including:
  - school maps, camera locations and emergency and active-shooter plans
  - background-check details
  - student medical records

  Raptor says it serves about 40% of US districts. It fixed the exposure quickly. The exposure window and any third-party access are unknown. — [K-12 Dive](https://www.k12dive.com/news/raptor-technologies-school-safety-data-leak/704790/); [The 74](https://www.the74million.org/article/leaked-active-school-shooter-plans-revive-scrutiny-of-ed-tech-privacy-pledge-2/); [SC Media](https://scmagazine.com/brief/unsecured-raptor-technologies-web-buckets-expose-sensitive-us-school-records)
- Raptor had signed the Student Privacy Pledge, which revived criticism that pledges are not verified. — [The 74](https://www.the74million.org/article/leaked-active-school-shooter-plans-revive-scrutiny-of-ed-tech-privacy-pledge-2/)

**Edulog Parent Portal [disclosed Dec 2023, Tenable TRA-2023-41]**
- API authorization flaws let anyone who created a free parent account, *without* a school-issued code, see:
  - student names and bus routes
  - parent contact information and GPS data
  - configuration details, including usernames and encrypted passwords for *integrations*

  About 6M student riders. — [Tenable blog](https://www.tenable.com/blog/the-kids-arent-alright-vulnerabilities-in-edulog-portal-revealed-k-12-student-location-data); [Tenable advisory TRA-2023-41](https://tenable.com/security/research/tra-2023-41); [The Journal](https://thejournal.com/articles/2023/12/14/vulnerabilities-in-edulog-portal-revealed-bus-location-data-logins-for-6m-students.aspx)
- Edulog said it fixed the issue "in the next build". It told Tenable it had no plans to notify affected parties. — [JD Supra](https://www.jdsupra.com/legalnews/cybersecurity-company-discovers-1236551/); [The 74 on GPS bus trackers](https://www.the74million.org/article/relied-on-by-parents-hailed-by-schools-gps-bus-trackers-raise-security-risks/)

**Instructure Canvas [Apr 29 and May 7, 2026]**
- **Official root cause:** a vulnerability in Canvas "Free-for-Teacher" (FFT) accounts, exploited by a known criminal group (ShinyHunters claimed it). Instructure has permanently discontinued FFT. — summarized from Instructure's incident statement via [cubite.io timeline](https://cubite.io/blogs/canvas-data-breach-2026) and [cyberleveling](https://cyberleveling.com/blog/canvas-instructure-breach-2026); [Wikipedia: 2026 Canvas data breach](https://en.wikipedia.org/wiki/2026_Canvas_data_breach) (could not fetch)
- **Reported mechanics (secondary sources, not confirmed by Instructure):**
  - An FFT user filed a support ticket with a linked file carrying a stored XSS payload.
  - When a support representative opened it, the attacker obtained that representative's session.
  - The attacker then used Canvas APIs to pull data across tenants.
  - A second, separate stored XSS in Discussions was used to push malicious CSS through custom themes, which defaced login pages (the May 7 event).

  Sources: [Scott Helme](https://scotthelme.co.uk/the-instructure-canvas-breach-2026-how-xss-in-a-support-ticket-compromised-275-million-students/); [TheCyberSecGuru](https://thecybersecguru.com/analysis/instructure-canvas-breach-2026-stored-xss/); [Spartans Security](https://www.spartanssec.com/post/shinyhunters-canvas-breach-what-we-can-learn-from-it)
- **Scale:** commonly cited as about 275M users at about 8,809 institutions. That is not independently verified. Data reportedly included usernames, emails, course names, enrollments and messages. Instructure reportedly reached an agreement with the attacker around May 11 and says the data was returned and destroyed. — [Cloudskope](https://www.cloudskope.com/insights/post/instructure-canvas-ransomware-attack-hits-universities-2026); [cybershitty](https://cybershitty.com/breaches/instructure-2026)
- **NYC impact** (from the NYCPS incident page; see `nyc_data_flows.md`): about 740 students and 48,000 staff. Canvas was suspended May 8-20, 2026.

**Frontline Education [detected Aug 14, 2026; reported Oct 2026]** (note: 2026, not 2025)
- Frontline says a vulnerability in a *third-party software product* it uses allowed unauthorized access to part of its environment. Affected products were Frontline Central (HR) and School Health Management. Data included employee SSNs and student health data. About 1.3M people were notified, which is likely an undercount because some state AG filings are not public. The third-party product was not named in the results I saw. — [SecurityWeek](https://www.securityweek.com/frontline-education-data-breach-impacts-over-1-3-million/); [BleepingComputer, Oct 2 2026](https://www.bleepingcomputer.com/news/security/frontline-education-data-breach-impacts-school-district-employees/); [GovTech](https://www.govtech.com/education/k-12/frontline-education-data-breach-impacts-school-employees); [Infosecurity Magazine](https://www.infosecurity-magazine.com/news/frontline-education-breach-k12/)

**Sector trend**
- A Clever-sponsored survey [2025] says vendor-related incidents rose to 32% of district incidents in 2025, from 4% in 2023. This is a vendor-sponsored figure. — [AI Journal press release](https://aijourn.com/new-report-finds-one-in-two-u-s-school-districts-experienced-a-cybersecurity-incident-in-2025/)
- Moody's ranks education among the top sectors hit via third parties (cited in `threat_landscape.md`).

### Inferences
- **Root-cause taxonomy.** Grouping the incidents by the vendor plane that failed:

  | Vendor plane that failed | Incidents |
  |---|---|
  | Privileged vendor-staff access (support or maintenance) | PowerSchool, Canvas |
  | Storage hygiene (public or unencrypted buckets, open Elasticsearch) | Illuminate, Raptor, LineLeader |
  | Authorization on consumer-facing APIs | Edulog |
  | Internet-facing third-party components | MOVEit, Frontline |

  None of these is fixed by anything a small school does on its own network.
- **Support tooling is the crown jewel.** In both PowerSchool and Canvas, the attacker became "the vendor's support person". Support identities hold cross-tenant read and export power, and they were less hardened than admin logins: password-only in PowerSchool's case, and in Canvas's case exposed to untrusted ticket content.
- **Short log retention hides the problem.** PowerSchool's August 2024 access could not be attributed because logs had aged out. Vendors' own retention limits customers' ability to scope a breach.
- **Integration secrets sit in vendor apps.** Edulog stored credentials for integrations. Any vendor holding SIS or rostering credentials turns a single app bug into a pivot toward upstream systems.

### Gaps
- I could not read the Alberta report's "Remote support permissions" section to confirm whether districts could see vendor support sessions in their own logs.
- Instructure has not published a post-incident technical report, so the stored-XSS chain is from analysts.
- The third-party product in the Frontline 2026 breach was not named in the results I saw.
- I found no 2025 Frontline incident. The user's date may refer to the Aug 2026 event.
- Search returned no ClassLink or Clever breach or researcher-disclosed vulnerability for 2022-2026. That is absence of evidence, not proof.
- I did not research Edulog further, for example any later incidents or litigation.
- I found no reporting on how the PowerSchool attacker obtained the subcontractor's credential (infostealer, reuse or phishing) in sources I could access.

---

## 2. Integration plumbing: rostering, LTI, SSO, tokens, and how much data flows by default

### Takeaway
Child data moves from the SIS along a few pipes:
- rostering hubs (Clever, ClassLink, OneRoster APIs, Microsoft SDS, Google Classroom sync)
- LMS-to-tool launches (LTI 1.3 / Advantage)
- SSO assertions (SAML/OIDC)
- long-lived API credentials stored by vendors

Field-level minimization controls exist (Clever sharing rules, ClassLink DataGuard, Canvas LTI privacy levels, Google's under-18 app gating), but they are opt-in, scattered across consoles, and defaults tend toward sharing. Vendor-specific custom fields in OneRoster push data collection beyond the standard.

### Cited Findings

**Clever**
- District admins can set per-app sharing rules. Since 2017 these can be filtered by ELL, IEP and free/reduced-price lunch status, configured in each app's "Data Sharing" tab. — [Clever July 2017 release notes](https://www.clever.com/blog/2017/07/july-2017-product-release-notes)
- "Share by rules" is dynamic: new SIS records that match a rule are *automatically* shared with apps. Over-broad rules therefore keep pushing future students' data to vendors. — [Clever spring 2019 district updates](https://clever.com/blog/2019/05/spring-updates-for-districts); [Clever trust/privacy](https://clever.com/trust/privacy)
- Library apps (teacher-adopted) get "minimal" data (first name, last initial, class). Districts can block apps or turn this off. — [Clever privacy](https://clever.com/trust/privacy)
- Vendor help pages show per-field toggles (ELL, FRL, IEP) on the Clever sharing screen. Some vendors advise districts to share only the sections in rollout. — [ClassTag help](https://intercom.help/classtag-inc/en/articles/6326422-how-do-i-adjust-clever-sharing-rules-when-syncing-with-classtag); [Khan Academy help](https://support.khanacademy.org/hc/ka/articles/17100737312397); [Skill Struck](https://support.skillstruck.com/knowledge/clever-sharing-recommendations-with-skill-struck)
- Clever's developer docs warn that the email in its OAuth token is not verified by Clever. Apps must not treat it as proof of identity, a known account-linking pitfall. Clever runs a bug bounty. — [Clever dev docs: Security](https://dev.clever.com/docs/security); [Clever security practices](https://clever.com/trust/security/practices)

**ClassLink**
- DataGuard masks or replaces selected roster fields (names, email, role, class title, birth date) before they reach vendors. The product page notes that some vendor-required fields (middle name, user ID, email, birth date) are *outside* the OneRoster standard. This is a vendor product page. — [ClassLink DataGuard](https://classlink.com/dataguard)

**OneRoster / 1EdTech**
- A 1EdTech working-group deck says that in field work "many custom metadata fields are being added to OneRoster", creating ad hoc vendor-specific extensions. — [1EdTech Rostering Pre-Conference Working Group, 2025](https://www.1edtech.org/sites/default/files/media/docs/2025/Rostering%20Pre-Conference%20Working%20Group.pdf)
- SIS vendors expose OneRoster 1.2 APIs using OAuth 2 client credentials. Infinite Campus is one example. — [Infinite Campus OneRoster 1.2 API docs](https://kb.infinitecampus.com/help/oneroster-12-api-documentation); [OneRoster 1.2 Best Practices Guide](https://www.imsglobal.org/node/204056)
- The 2025-2026 work with Ed-Fi focuses on operational rostering. I saw no minimization controls in those materials. — [1EdTech/Ed-Fi blog](https://www.1edtech.org/blog/ed-fi-alliance-and-1edtech-simplifying-rostering-to-unlock-actionable-data); [Ed-Fi OneRoster endpoint mapping](https://docs.ed-fi.org/reference/oneroster/data-model/endpoint-source-mapping)

**LTI 1.3 / Advantage**
- LTI Advantage adds three services on top of the LTI 1.3 security model: Names and Role Provisioning (NRPS), Assignment and Grade Services, and Deep Linking. NRPS gives a tool the full membership list and roles for a course. — [Edlink LTI Advantage overview](https://ed.link/community/lti-advantage/); [Blackboard NRPS docs](https://docs.blackboard.com/lti/tutorials/names-and-roles); [1EdTech LTI Advantage Implementation Guide](https://www.imsglobal.org/node/177591)
- In Canvas, a tool's privacy level determines PII in launches. "Public" or "name_only" sends names and SIS ID; more restrictive levels send only opaque LTI IDs and roles. Instructure publishes guidance on the privacy implications of installing an LTI 1.3 tool. — [Canvas: Privacy implications of installing an LTI 1.3 tool](https://community.canvaslms.com/t5/Canvas-Resource-Documents/Privacy-implications-of-installing-an-LTI-1-3-tool-in-Canvas/ta-p/637141); [Canvas developer forum on claims and privacy](https://community.canvaslms.com/t5/Developers-Group/LTI-1-3-Configuration-Claims-Course-Placement-Privacy/m-p/229255)
- 1EdTech promotes LTI 1.3 (OAuth2/OIDC with signed JWTs) as fixing LTI 1.1's shared-secret weaknesses. — [1EdTech: Why adopt LTI 1.3](https://www.1edtech.org/standards/lti/why-adopt-lti-1p3)

**Google Workspace for Education**
- Since Oct 23, 2023, users designated under 18 are blocked from third-party apps the admin has not configured, and must request access. Admins can allow "basic sign-in info only" apps. The school, not Google, must obtain parental consent. — [Google Workspace Updates, Aug 2023](https://workspaceupdates.googleblog.com/2023/08/third-party-app-access-enhancements-for-google-workspace-edu.html); [Google Admin Help 13288950](https://support.google.com/a/answer/13288950); [Admin Help 16484119](https://support.google.com/a/answer/16484119)
- Compromised-account response must include revoking OAuth grants and sessions even when MFA is on. — K12 SIX/WSIPC guidance, cited in `threat_landscape.md`

### Inferences
- **Defaults favor breadth.** Clever's dynamic rules, NRPS course rosters, Canvas "public" privacy and teacher-adopted apps all mean a vendor typically receives the whole section or school, not the students who use the tool. Minimizing takes deliberate admin work in each console.
- **Long-lived credentials are the quiet risk.** OneRoster client-credential secrets, Clever district tokens and SIS API keys held by vendors (as Edulog showed) rarely expire or get rotated. A breach at any downstream vendor can expose upstream SIS access. Small orgs almost never keep an inventory of which vendors hold such keys.
- **Very small orgs often lack a hub entirely.** Tiny schools and childcare centers often export CSVs or type data into each app by hand, so the "integration" is a spreadsheet emailed to a vendor. Minimization there means choosing which CSV columns to send.
- **Potential volunteer deliverable.** A one-page minimization guide covering:
  - Clever: restrict sharing rules to sections in use; untick ELL/IEP/FRL fields
  - ClassLink: DataGuard where licensed
  - Canvas: LTI privacy set to anonymous unless names are needed
  - Google: keep under-18 unconfigured apps blocked
  - SIS: rotate OneRoster secrets annually and at vendor offboarding

### Gaps
- I found no public measurement of how many fields typical K-12 apps request through Clever or ClassLink versus what they need. That would be a novel study, perhaps using SDPC registry data from `public_datasets.md`.
- I could not confirm current Clever defaults for new app connections (all students vs. none).
- I did not verify whether SAML/OIDC SSO assertions from Google, Microsoft or ClassLink to vendors include grade or other attributes by default.
- I found no standard token-expiry or rotation guidance from 1EdTech for OneRoster client secrets.

---

## 3. Vendor "support access": how support staff reach school data and whether schools can see or restrict it

### Takeaway
Major SIS and LMS vendors keep privileged support paths that can read or export customer data across tenants: PowerSource "Maintenance Remote Support" at PowerSchool, and Canvas support staff sessions. Before Dec 2024 these were, at least at PowerSchool, single-factor. Customer-side visibility and control were limited: an on-premises toggle, requests to the customer success manager, and audit logs whose coverage of vendor sessions is unclear. Unlike the big cloud providers' "customer approval" features (e.g., Microsoft Customer Lockbox, Google Access Approval), I found no evidence that K-12 SaaS vendors offer just-in-time, customer-approved, logged support access.

### Cited Findings
- **PowerSchool's PowerSource maintenance function** gives technicians database-level access to customer SIS instances. Post-breach, PowerSchool added VPN/SSO/MFA and separated maintenance access. — [CrowdStrike report](https://www1.powerschool.com/wp-content/uploads/2025/03/PowerSchool-CrowdStrike-Final-Report.pdf); [Alberta OIPC](https://oipc.ab.ca/wp-content/uploads/2025/11/FINAL-Investigation-Report-Regarding-PowerSchool-Breach-FOIP2025-IR-02.pdf)
- **What districts were told [Jan 2025 webinar notes]:**
  - Logs showed which data was accessed and when.
  - On-premises districts can disable maintenance access via documentation from their customer success manager.

  — [HCUSD2 webinar notes](https://hcusd2.socs.net/vimages/shared/vnews/stories/677fe24aa9554/Notes%20taken%20from%20PowerSchool%20webinar%20on%20Jan%208th%202025.pdf)
- PowerSchool SIS and SMS have a Database Audit Log and user-activity review for district admins. The docs do not say whether vendor support sessions appear. — [PowerSchool Reviewing User Access](https://support.powerschool.com/help/sms/843/SchoolUser/Content/Topics/Reviewing_user_access.htm); [User Activity Review](https://support.powerschool.com/help/sms/843/SchoolUser/Content/Topics/User-Activity-Review.htm)
- **Canvas 2026 (reported):** the attacker obtained a *support representative's* session through a malicious ticket attachment. — [Scott Helme](https://scotthelme.co.uk/the-instructure-canvas-breach-2026-how-xss-in-a-support-ticket-compromised-275-million-students/) (analyst inference)
- **NYC PETS [Feb 2023]:** a buggy update let vendor users view and export other vendors' employee records. The DOE then considered restricting what vendors can "view and export". — `nyc_data_flows.md`

### Inferences
- **Four contract questions** a small school, diocese or childcare center can ask any vendor:
  1. Can your staff access our data without our approval, and how is that access authenticated (phishing-resistant MFA, managed devices)?
  2. Is support access logged, and can we see those logs?
  3. Can we disable standing support access and grant it per ticket and time-boxed?
  4. Are contractors or subcontractors included, and are their accounts removed when they leave?

  PowerSchool's credential belonged to a former subcontractor, per the Ontario finding.
- **Ticket content is untrusted.** Support desks that render customer-uploaded content inside privileged staff sessions are a design flaw class worth naming in procurement questionnaires.
- **Potential model clause.** A support-access policy template modeled on Lockbox and Access Approval patterns could be offered to SDPC for its DPA exhibits.

### Gaps
- No primary source confirms whether PowerSchool districts could see vendor maintenance sessions in their own audit logs before Dec 2024.
- I did not search for Clever, ClassLink, Infinite Campus, Skyward, brightwheel or Procare support-access controls specifically.
- The Microsoft and Google lockbox comparison is from my background knowledge, not cited in this session.

---

## 4. MSPs and RMM tools serving schools, childcare and parishes

### Takeaway
Remote monitoring and management (RMM) and remote-access tools are a one-to-many attack path: compromising the MSP's tool reaches every client.
- **Kaseya VSA [Jul 2021]:** fewer than 70 direct customers were hit, but they were MSPs, and roughly 800-1,500 downstream businesses were affected. These included more than 100 New Zealand kindergartens and several schools.
- **ConnectWise ScreenConnect CVE-2024-1709 [Feb 2024]:** a CVSS 10 authentication bypass, exploited by LockBit, Play, Black Basta and others. Education was among the affected sectors, including at least one documented MSP supply-chain case.

Tiny organizations that rely on a single local IT person or small MSP inherit that provider's patch speed and remote-tool exposure.

### Cited Findings
- **Kaseya:** fewer than 70 of 37,000 customers were directly affected, mostly MSPs, with an estimated 800-1,500 downstream victims. Attackers abused on-prem VSA servers run by MSPs to push malicious updates to MSP clients. — [Wikipedia: Kaseya VSA ransomware attack](https://en.wikipedia.org/wiki/Kaseya_VSA_ransomware_attack); [WatchGuard](https://www.watchguard.com/it/wgrd-news/blog/msps-main-victims-kaseya-ransomware-attack); [Silicon Republic](https://siliconrepublic.com/enterprise/kaseya-cyberattack-ransomware)
- **New Zealand impact [Jul 2021]:** more than 100 North Island kindergartens reverted to pen and paper. The Ministry first flagged 11 schools; a later report said 9, so the count is unsettled. St Peter's College was among them. — [RNZ, Jul 5 2021](https://www.rnz.co.nz/news/national/446225/kaseya-ransomware-attack-hits-new-zealand-kindergartens); [NZ Herald](https://www.nzherald.co.nz/nz/worldwide-ransomware-attack-st-peters-college-hit-by-us-cyber-attack/JACHAD3OPGUOF7ZIF4PJXDPICA/); [NBR](https://www.nbr.co.nz/tech/two-kiwi-schools-victim-of-kaseya-ransomware-attack); [NZ Herald commentary "When leaving it to the pros went sideways"](https://nzherald.co.nz/business/juha-saarinen-when-leaving-it-to-the-pros-went-sideways/ZXR22VFW6U63YLH4Z3U5AD3MNI)
- **ScreenConnect:** CVE-2024-1709 (authentication bypass, CVSS 10) and CVE-2024-1708 (path traversal). Proof-of-concept exploits were public quickly, and the flaw was added to CISA KEV. — [Unit 42](https://unit42.paloaltonetworks.com/connectwise-threat-brief-cve-2024-1708-cve-2024-1709/)
- **ScreenConnect exploitation:** Kroll says cases hit multiple sectors including education. At-Bay documented an MSP being targeted so that its customers were affected; the MSP's SOC stopped it before encryption. Ransomware families involved included Play, LockBit 3.0, Bl00dy and Black Basta. — [Kroll](https://www.kroll.com/en/publications/cyber/screenconnect-vulnerability-exploitation); [At-Bay](https://www.at-bay.com/articles/lockbit-play-ransomware-screenconnect-flaws/); [SC World](https://scworld.com/news/connectwise-screenconnect-bug-used-in-play-ransomware-breach-msp-attack); [Sophos](https://www.sophos.com/en-us/blog/connectwise-screenconnect-attacks-deliver-malware); [The Record](https://therecord.media/connectwise-screenconnect-bug-cybercrime-exploitation)
  - Note: TechTarget swapped the two CVE numbers; the sources above agree that 1709 is the authentication bypass.

### Inferences
- **Highest-leverage controls for a parish school or childcare center using a local IT person:**
  1. Know which remote-access and RMM agents are installed on your machines.
  2. Require the provider to use MFA on the RMM console and to patch it promptly. ScreenConnect on-prem servers were exploited within days of disclosure.
  3. Prefer vendor-hosted (cloud) RMM, which the vendor patches centrally, over self-hosted servers. Kaseya and ScreenConnect on-prem were the exploited variants. (Inference.)
  4. Remove orphaned remote-access tools left by former helpers.
  5. Ask whether the MSP's own staff accounts are protected with phishing-resistant MFA.
- **Dioceses are a natural aggregation point.** A diocesan IT office that standardizes on one RMM has the same one-to-many property as an MSP, for better (central patching) or worse (single blast radius).

### Gaps
- I found no US school or childcare victim publicly named in the ScreenConnect 2024 wave.
- I found no data on how many small US schools or parishes use MSPs, or which RMM tools.
- I did not cover the 2025-2026 RMM incidents (e.g., SimpleHelp, or later ScreenConnect advisories).

---

## 5. Childcare and parish software: public security posture signals

### Takeaway
Public signals are uneven.
- Procare and brightwheel advertise MFA. Procare claims SOC 2 Type 2; brightwheel cites TX-RAMP and AWS.
- ParishSOFT (Ministry Brands) rolled out 2FA/MFA only in 2024.
- Flocknote advertises TLS and backups but makes no SOC 2 claim I could find.
- I found no public security claims for Kangarootime or Lillio (formerly HiMama).
- LineLeader (ChildcareCRM) had an open Elasticsearch database in 2025.

EFF's 2022 audit found daycare apps broadly lacking 2FA. The big two have fixed that, but MFA is often *available* rather than *enforced*.

### Cited Findings
- **Procare:** says all platforms offer MFA, and claims SOC 2 Type 2 for the Procare and ChildPlus brands [press release Apr 15, 2025]. It has a trust/security page and a Feb 2024 data-security guide. — [Procare press release](https://www.procaresoftware.com/about-us/press-room/procare-solutions-continues-to-deliver-secure-compliant-software/); [Procare trust/security page](https://www.procaresoftware.com/trust-security-compliance/security/); [Procare data security guide, Feb 2024 (PDF)](https://www.procaresoftware.com/wp-content/uploads/2024/03/PC_Guide_DataSecurity2_Feb24.pdf)
- **brightwheel:**
  - Offers 2FA at sign-in and claims it was first in early education to do so.
  - Its security page cites AWS hosting and TX-RAMP-certified controls.
  - A third-party profile lists SOC 2, which I could not verify from brightwheel directly.

  — [brightwheel security](https://mybrightwheel.com/security/); [brightwheel 2FA help](https://intercom.help/brightwheel/en/articles/5918580-2fa-at-sign-in-overview); [brightwheel security FAQs](https://intercom.help/brightwheel/en/articles/6363539-brightwheel-security-faqs); [Nudge Security profile](https://security-profiles.nudgesecurity.com/app/mybrightwheel-com)
- **EFF [Jun 2022]:** daycare apps were "dangerously insecure", with 2FA missing and trackers present. brightwheel lacked 2FA at the time. — [EFF](https://www.eff.org/deeplinks/2022/06/daycare-apps-are-dangerously-insecure)
- **Kangarootime, Lillio:** no security, SOC 2 or MFA claims surfaced in search. — (absence; see Gaps)
- **LineLeader:** an open Elasticsearch database exposed about 140K records, closed Dec 2025. — `threat_landscape.md`; [Cybernews](https://cybernews.com/security/childcare-crm-database-leak-lineleader/)
- **ParishSOFT (Ministry Brands):**
  - 2FA for the Giving Manager portal from Feb 13, 2024.
  - Family Suite and Accounting were slated for Q2 2024.
  - A diocesan notice says MFA for ParishSOFT Accounting rolled out in Oct 2024.
  - ParishSOFT's security marketing cites Microsoft Azure's certifications (ISO 27001, SOC 2 and others), which belong to the *host*, not to ParishSOFT itself (post circa 2019).

  — [Archdiocese of St Paul & Minneapolis: ParishSOFT 2FA](https://missionsupport.archspm.org/news/parishsoft-two-factor-authentication); [ArchSPM: secure access](https://missionsupport.archspm.org/news/ensuring-secure-access-to-parishsoft-systems/); [Archdiocese of Atlanta MFA instructions](https://help.archatl.com/hc/en-us/articles/31682358403988-ParishSOFT-Multi-Factor-Authentication-MFA-Instructions); [ParishSOFT Azure post](https://parishsoft.com/news/security-privacy-compliance-the-benefits-of-microsoft-azure)
- **Flocknote:** TLS in transit and geo-redundant backups; no SOC 2 claim found. — [Flocknote Canada page](https://flocknote.com/?p=25831)
- **Parish context [May 2023]:** America Magazine reported that parish cybersecurity is at risk and experts see hope. — [America Magazine](https://www.americamagazine.org/politics-society/2023/05/08/parish-cybersecurity-risk-hope-experts-245247)

### Inferences
- **Hosting-provider halo.** Citing Azure or AWS certifications (ParishSOFT, partly brightwheel) is a weak signal. It says nothing about the vendor's own application or support-access controls. Small buyers should ask for the *vendor's own* SOC 2 Type II report and its scope.
- **Available is not enforced.** "MFA available" matters less than "MFA enforced for admin and staff roles". Childcare apps hold pickup authorizations and custody notes, so admin MFA enforcement should be the minimum ask.
- **Potential volunteer deliverable.** A small "posture card" table per vendor, with checkable fields:
  - MFA available and enforced
  - SSO
  - own SOC 2 Type II
  - security.txt and VDP
  - subprocessor list
  - DMARC policy
  - known incidents

  This is feasible and appears not to exist for childcare and parish software.

### Gaps
- I did not check security.txt, VDP, DMARC or subprocessor lists for any of these vendors, because live fetching was blocked. This is a straightforward follow-up with `dig` and `curl` in an environment with network access.
- I found nothing on Kangarootime, Lillio, Flocknote breaches, or LineLeader's current posture.
- I did not confirm whether Procare's SOC 2 covers all its products. Procare acquired several companies, which may include Kangarootime; unverified.

---

## 6. Publicly observable signals that predict vendor security quality

### Takeaway
Outside-in signals (patch cadence, exposed services, TLS and email-authentication hygiene, open ports) correlate with incidents in insurer-backed but vendor-affiliated studies (Marsh McLennan with Bitsight; Marsh McLennan with SecurityScorecard). I found no independent, peer-reviewed study tying security.txt, VDP or bug bounty presence, SOC 2 Type II, or subprocessor transparency to lower breach rates, and none at all for edtech.

The breaches in Q1 suggest the most predictive signals for edtech are often *not* visible from outside: support-access design, storage configuration, log retention. Public signals are a floor, not a ceiling. Raptor had signed the Student Privacy Pledge, and Illuminate presumably had DPAs with NYC.

### Cited Findings
- **Marsh McLennan Cyber Risk Analytics Center and Bitsight [2022]:**
  - Analyzed Bitsight data on about 365,000 organizations.
  - Found 14 Bitsight analytics, including the overall rating and 13 risk vectors, statistically significantly correlated with Marsh clients' reported incidents.
  - Marsh says Bitsight had no access to Marsh's claims data.
  - Patching cadence was a highlighted factor.

  — [Bitsight news](https://www.bitsight.com/news/new-marsh-study-finds-link-between-cybersecurity-incidents-and-ratings); [Dark Reading](https://www.darkreading.com/cyber-risk/study-finds-significant-correlation-between-bitsight-analytics-and-cybersecurity-incidents); [Reinsurance News](https://www.reinsurancene.ws/bitsight-mmc-study-correlates-cyber-ratings-and-security-incidents/)
- **Bitsight's own claim:** organizations rated 400 or below were about 5 times more likely to have a publicly disclosed breach than those rated 700 or above. This is a vendor marketing claim. — [Bitsight datasheet](https://www.bitsight.com/resources/datasheets/security-ratings-correlate-to-breaches); [Bitsight help article](https://help.bitsighttech.com/hc/en-us/articles/360011652613-Bitsight-Security-Ratings-Correlate-to-Breaches)
- **Marsh McLennan and SecurityScorecard:** found seven predictive factors, with endpoint security strongest. — [SecurityScorecard report page](https://securityscorecard.com/reports/reduce-cyber-risk-with-the-predictive-power-of-security-ratings)
- **1EdTech TrustEd Apps Data Privacy certification:** reviews a supplier's public privacy policy and ToS against a rubric (newer versions also cover ad and AI policies). The rubric is a policy review, not a technical security test. Certification is limited to members. More than 11,000 apps have been vetted (undated figure). — [1EdTech certification FAQ](https://www.1edtech.org/certification/data-privacy/faq); [TrustEd Apps rubric](https://1edtech.org/trustedapps/rubric); [webinar page](https://www.1edtech.org/events/webinar-building-trust-through-transparency-with-1edtechs-trusted-apps-rubrics)
- **Student Privacy Pledge:** Raptor was a signatory when its buckets were open. — [The 74](https://www.the74million.org/article/leaked-active-school-shooter-plans-revive-scrutiny-of-ed-tech-privacy-pledge-2/)
- **Bug bounties:** Clever advertises an active bug bounty. — [Clever security practices](https://clever.com/trust/security/practices)
- **Disclosure outcomes:** Edulog declined to notify users after Tenable's disclosure, which shows that disclosure-handling behavior can be observed. — [JD Supra](https://www.jdsupra.com/legalnews/cybersecurity-company-discovers-1236551/)

### Inferences
- **A practical scoring tier for small buyers** (my proposal, not validated):

  | Tier | Signals |
  |---|---|
  | **Hygiene** (cheap to check) | HTTPS with HSTS; DMARC at p=quarantine or p=reject; security.txt (RFC 9116); no exposed admin panels |
  | **Process** | VDP or bug bounty; vendor's own SOC 2 Type II with application and support systems in scope; published subprocessor list; published breach-notification SLA |
  | **Architecture** (asked, not observed) | MFA enforced for staff and support; customer-visible support-access logs; field-level sharing controls; retention schedule and deletion at offboarding |

- **Weighting.** The Marsh studies support weighting patch cadence and exposed services. The edtech breaches support weighting the Architecture tier, which needs questionnaires or SDPC DPA exhibits rather than scanning.

### Gaps
- I found no independent academic study correlating security.txt, VDP or SOC 2 status with breach likelihood.
- I found no edtech-specific outside-in security survey (e.g., DMARC adoption among K-12 vendors). This is a feasible and novel volunteer measurement: scan domains of vendors in the SDPC registry.
- I found no CVE-history analysis for K-12 SaaS. Most are SaaS without CVEs. Recent CVEs exist (e.g., [CVE-2026-10168](https://nvd.nist.gov/vuln/detail/CVE-2026-10168), whose product I did not verify).
- Related 2026 items surfaced but were not read:
  - a TechCrunch report on a student-admissions website bug — [TechCrunch, Feb 19 2026](https://techcrunch.com/2026/02/19/bug-in-student-admissions-website-exposed-childrens-personal-information)
  - an EdWeek piece on a possible tip-app breach — [EdWeek, Mar 2026](https://www.edweek.org/technology/a-potential-breach-of-an-anonymous-tip-app-could-have-exposed-sensitive-student-data/2026/03)
  - a Ravenna Hub exposure fix — [SC World](https://www.scworld.com/brief/ravenna-hub-fixes-data-exposure-vulnerability-affecting-student-information)

  Ravenna serves private and independent school admissions, which is relevant to Catholic and classical schools.

---

## 7. Ideas for scalable defenses (synthesis; inferences grounded in Sections 1-6)

### Takeaway
The highest-leverage scalable defenses target the vendor planes that actually failed: support access, storage hygiene, integration scope and long-lived credentials. They also give small orgs checklists and aggregated public signals instead of expecting them to audit vendors.

### Cited Findings
- FTC-ordered remedies for Illuminate (data minimization, a published retention schedule, honest breach-notification timing) are a ready-made checklist of what regulators now expect. — [FTC](https://www.ftc.gov/news-events/news/press-releases/2025/12/ftc-takes-action-against-education-technology-provider-failing-secure-students-personal-data)
- PowerSchool's post-breach controls (MFA and VPN in front of support, separate maintenance platform, remote support default-off) show the vendor-side fix pattern. — [Alberta OIPC](https://oipc.ab.ca/wp-content/uploads/2025/11/FINAL-Investigation-Report-Regarding-PowerSchool-Breach-FOIP2025-IR-02.pdf); [Datapath](https://www.mydatapath.com/industry-news/powerschool-breach-k12-vendor-access-lessons/)
- Existing minimization controls: Clever field and rule filters, ClassLink DataGuard, Canvas LTI privacy levels, Google under-18 app gating. — Section 2 sources
- Moving NYC DOE off MOVEit left the server offline. Nobody knew vendor file exchange was a risk until a zero-day hit. — `nyc_data_flows.md`

### Inferences (proposals)
1. **Integration-scope minimization guide** (one page per hub: Clever, ClassLink, Google, Canvas/Schoology LTI, Microsoft SDS). Covers:
   - restrict sharing to sections in use
   - turn off ELL/IEP/FRL/DOB fields unless justified
   - set LTI privacy to anonymous by default
   - keep under-18 unconfigured apps blocked
   - review teacher-adopted Library apps each term
   - rotate OneRoster and SIS API secrets annually and at offboarding
2. **"Data export alarm" checklist.** Small orgs should know where bulk exports can happen and get notified when they do: SIS export tools, the vendor maintenance path, rostering syncs, Google Takeout and Drive sharing. Ask vendors: "Will you alert us when any account, including your support staff, exports more than N records?" PowerSchool's attacker ran bulk operations over nine days; an export alert would have shortened that.
3. **Vendor support-access policy template** (contract or DPA exhibit):
   - support access disabled by default
   - access granted per ticket and time-boxed
   - phishing-resistant MFA and managed devices for support staff and subcontractors
   - offboarding of contractors within 24 hours
   - customer-visible access logs kept at least 12 months (the PowerSchool logs could not scope the August access)
   - untrusted ticket attachments sandboxed away from privileged sessions (Canvas)
4. **Trust-page aggregator / posture cards.** An open dataset per vendor recording:
   - MFA available vs. enforced; SSO
   - vendor's own SOC 2 Type II (not the host's)
   - security.txt; VDP or bounty
   - subprocessor list; DMARC policy
   - incident history with dates and links

   Seed it from the SDPC registry and the childcare and parish vendors above. Re-scan the hygiene signals monthly.
5. **Credential inventory worksheet for tiny orgs.** List every vendor holding a key, token or support login to your systems, plus every RMM or remote-access agent on your machines (Kaseya, ScreenConnect lessons). Review it each term and when an IT helper leaves.
6. **Retention and deletion asks.** Require a deletion certificate at contract end. Illuminate kept NYC data for years, and Kido and PowerSchool showed that "deleted" claims after ransom are unreliable.

### Gaps
- None of these proposals has been validated with school or childcare administrators.
- I did not check whether SDPC's National DPA already includes support-access or export-alerting language. That should be checked before drafting new clauses.
