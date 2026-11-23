# Incident Response, Logging, Backup and Recovery for Tiny Child-Serving Organizations (No IT Staff)

Lens: a DFIR responder who has worked small-organization cases. Research date: 2026-11-23. Method: web search only. Direct fetches of support.google.com, learn.microsoft.com and ic3.gov were blocked by this session's network policy, so every claim below rests on search-result excerpts from those pages, not the full pages. Wherever that matters, I flag the gap.

Builds on the earlier notes in `research_notes/Kids data defense research tree/`, chiefly threat_landscape.md and economics_insurance_funding.md. Those notes established:
- Attackers now contact and extort parents directly (Kido, Sep 2025; PowerSchool follow-on extortion, May 2025).
- Paying does not guarantee the data is deleted.
- Safeguarding and child-protection records are the most harmful data to leak.
- A free child credit freeze (under 16) has existed since 2018.
- The NYU Cybersecurity Clinic launched in 2026 and works with NYC Cyber Command.

This file does not repeat those findings. It concentrates on the technical and procedural side of the response.

---

## 1. Logging by license tier: what evidence exists after an email compromise, and should a tiny org export logs proactively?

### Takeaway
On the cheap tiers tiny orgs actually use, evidence runs out fast:
- **Microsoft:** Entra ID sign-in and audit logs last only **7 days on the Free tier** (30 days with P1, which comes in Business Premium). The Purview unified audit log (UAL) lasts **180 days on Audit (Standard)** for records created on or after Oct 17, 2023.
- **Google:** most Workspace audit logs last about **6 months** regardless of edition. The better investigation tooling is reserved for premium editions (Education Standard/Plus, Enterprise).

Tiny orgs typically find a compromise weeks later, after a parent or vendor complains. A responder arriving then often finds the identity logs already gone. Proactive export, or at minimum an "export first" step in the playbook, is the single highest-value logging action.

### Cited Findings
**Microsoft Purview (unified audit log)**
- Default Audit (Standard) retention changed from 90 to 180 days. Records generated before Oct 17, 2023 keep 90 days; records on or after that date keep 180 days. — [Microsoft Learn: Audit (Premium)](https://learn.microsoft.com/en-us/purview/audit-premium); [Audit solutions overview](https://learn.microsoft.com/purview/audit-solutions-overview)
- Audit (Premium) keeps Exchange, SharePoint and Entra audit records for 1 year by default. Custom retention policies can reach 1 year, or 10 years with a per-user add-on license. — [Microsoft Learn: Audit (Premium)](https://learn.microsoft.com/en-us/purview/audit-premium)

**The 2023 free-logging expansion after Storm-0558**
- In July 2023, CISA and Microsoft announced expanded default logging for Purview Audit (Standard) customers, starting September 2023. It included detailed mail-access events (MailItemsAccessed) and 30+ other log types. Before the change, MailItemsAccessed, the event that exposed Storm-0558, was effectively limited to E5/G5 and Audit Premium. — [TechTarget](https://www.techtarget.com/cybersecurity/news/366545163/Microsoft-to-expand-free-cloud-logging-following-recent-hacks); [Help Net Security](https://www.helpnetsecurity.com/?p=270614); [CISA AA23-193A](https://www.cisa.gov/news-events/cybersecurity-advisories/aa23-193a)
- Reporting on which licenses are covered is inconsistent:
  - Some outlets say "E3/G3 and above."
  - BleepingComputer updated its story to say "all Audit Standard customers."
  - The February 2024 rollout coverage focused on government tenants.
  — [BleepingComputer: govt-only rollout](https://www.bleepingcomputer.com/news/security/microsoft-finally-expands-free-logging-but-only-for-govt-agencies/); [The Hacker News, Feb 2024](https://thehackernews.com/2024/02/microsoft-expands-free-logging.html)
- CISA published a "Microsoft Expanded Cloud Logs Implementation Playbook" in January 2025. — [CISA PDF](https://cisa.gov/sites/default/files/2025-01/microsoft-expanded-cloud-logs-implementation-playbook-508c.pdf)

**Microsoft Entra ID sign-in and audit logs**
- Retention is 7 days on Entra ID Free and 30 days on P1/P2. Microsoft says a license upgrade is not retroactive: moving from Free to P1 only preserves what is still inside the 7-day window. — [Microsoft Learn: Entra data retention](https://learn.microsoft.com/en-us/entra/identity/monitoring-health/reference-reports-data-retention)
- Q&A answers report that sign-in logs past retention cannot be recovered even with E5 and Global Admin, unless they were exported or streamed beforehand (to a storage account or Log Analytics). — [Microsoft Q&A](https://learn.microsoft.com/en-us/answers/questions/5744078/retrieving-sign-in-logs-or-similar-evidence-beyond); [Microsoft Q&A, 7-day limit](https://learn.microsoft.com/en-us/answers/questions/2134287/how-to-retrieve-a-users-sign-in-logs-longer-than-7)
- Business Premium includes Entra ID P1. — [Microsoft Q&A](https://learn.microsoft.com/en-nz/answers/questions/5849700/entra-sign-in-logs-not-exporting-to-log-analytics)
- Business Premium for nonprofits is listed at $5.50/user/month (annual). — [Microsoft nonprofit plans](https://www.microsoft.com/en-us/nonprofits/microsoft-365-plans-pricing-grants)

**Google Workspace**
- Google's "Data retention and lag times" page:
  - Unlisted reports and log events are retained for "generally 6 months."
  - Admins cannot delete log data or change how long it is kept.
  - Vault log events are kept indefinitely.
  - Admin log events appear in near real time; other log types can lag hours to days.
  — [Google Workspace: Data retention and lag times](https://knowledge.workspace.google.com/admin/reports/data-retention-and-lag-times); [support.google.com/a/answer/7061566](https://support.google.com/a/answer/7061566?hl=en)
- Google help pages describe the **security investigation tool** (search, bulk actions, Security Center) as a premium feature: Enterprise Standard, Enterprise Plus, Education Standard and Education Plus. Non-premium editions get the **basic audit and investigation tool** to view log data. — [Google Admin Help 11482175](https://support.google.com/a/answer/11482175?hl=en); [About the audit and investigation tool](https://support.google.com/a/answer/9725452?authuser=0)
- Google's own Education Standard one-pager lists the security investigation tool as a Standard feature, which is the main upgrade over Fundamentals. — [Google Education Standard one-pager](https://services.google.com/fh/files/misc/education_standard_onepager.pdf); [Education Standard page](https://edu.google.com/intl/ALL_uk/workspace-for-education/editions/education-standard/)
- Some log sources (e.g., Devices) depend on the subscription. — [Data retention and lag times](https://knowledge.workspace.google.com/admin/reports/data-retention-and-lag-times)

### Inferences
**What evidence a responder can realistically recover after a BEC in a tiny tenant**

These points are drawn from the cited retention rules plus common DFIR practice. They are inference, not a vendor statement.
- **Microsoft Business Basic/Standard (Entra Free):**
  - The UAL holds about 180 days of mailbox and admin activity, including inbox-rule creation (New-InboxRule/Set-InboxRule), mail forwarding changes, OAuth consent grants, and, since the 2023 expansion, likely MailItemsAccessed.
  - Interactive sign-in detail with IPs and user agents in the Entra portal disappears after 7 days.
  - The UAL carries some login events, but less conveniently.
- **Microsoft Business Premium (P1):** 30 days of sign-ins, plus Conditional Access, which can prevent many BEC cases outright.
- **Google (all editions):** about 6 months of admin, login, Gmail, Drive and OAuth token logs in the basic audit and investigation tool. On Education Fundamentals and Business Starter, the lack of the security investigation tool mainly costs bulk remediation (e.g., deleting a phishing message from every inbox at once), not the evidence itself.
- **The DFIR reality:** tiny orgs typically notice a compromise 2-8 weeks in, when a vendor reports an unpaid invoice or a parent forwards something odd. By then the Microsoft Free-tier Entra sign-ins are gone.

**What to export, and when**
- **Before an incident:** a quarterly or monthly export of the UAL and Google login/admin logs to an offline encrypted drive costs nothing and preserves the baseline.
- **At first suspicion, within the first hour and before resetting anything:** export
  - Entra sign-ins (CSV), or the Google login audit
  - the UAL search for the user over 90-180 days
  - inbox rules and forwarding
  - OAuth app grants
- **Upgrade decision:** for a Microsoft shop, Business Premium at nonprofit pricing is the best value. It adds P1 (30-day sign-ins plus Conditional Access) and Defender for Business.
- **Which Microsoft licenses get the 2023 expanded logging:** treat it as "verify in your own tenant." Run an audit search for MailItemsAccessed rather than relying on press reports.

### Gaps
- I could not fetch the full Microsoft Learn licensing table to confirm Audit (Standard) inclusion and expanded-log availability for Business Basic, Standard and Premium specifically. Press accounts conflict.
- I could not confirm from Google's own documentation whether Education Fundamentals and Business Starter differ from Business Standard in which Gmail log events appear in the basic audit tool. One Google page lists "Audit and investigation" ambiguously across tiers.
- I found no source on whether Google Workspace for Nonprofits (free tier) has the same 6-month retention. It probably does, since retention is described as edition-independent, but this is unverified.

---

## 2. Backups: do Workspace and M365 need third-party backup? Ransomware via sync, version-history limits, Vault and retention as substitutes, cheap options

### Takeaway
Both vendors run a shared-responsibility model, and their native recovery windows are short:
- **Microsoft:** "Restore your OneDrive" covers the last 30 days. The work/school recycle bin keeps items for 93 days.
- **Google:** Drive file versions can be purged after 30 days or once 100 newer versions exist.

For a tiny org the main threats are a slow-discovered compromise, a malicious insider or departing admin, an account deletion, or ransomware on a PC syncing encrypted files. Native features cover most fast-discovered events. A cheap third-party SaaS backup, or Microsoft 365 Backup at about $0.15/GB/month, covers the rest.

Vault and Purview retention are legal-hold and compliance tools, not restore tools. They preserve data but do not give point-in-time restore of a folder tree.

### Cited Findings
**Microsoft 365**
- "Restore your OneDrive" (Files Restore) rolls a whole OneDrive back to any point in the last 30 days. It suggests a restore date after automatic ransomware detection. — [Microsoft Support: Restore your OneDrive](https://support.microsoft.com/onedrive/restore-your-onedrive)
- For work or school accounts, deleted files can be restored from the recycle bin within 93 days, unless an admin changed the setting. Permanently deleted items cannot be recovered. — [Microsoft Support: Restore deleted files](https://support.microsoft.com/en-us/onedrive/restore-your-onedrive-files)
- Files Restore depends on version history and the recycle bin. Reducing the default number of versions reduces its effectiveness. — [Microsoft Learn: Ransomware protection in Microsoft 365](https://learn.microsoft.com/en-us/compliance/assurance/assurance-shared-ransomware-protection)
- A Barracuda e-book claims the OneDrive recycle bin keeps only 30 days by default, which contradicts Microsoft's 93 days. Microsoft's documentation is the more authoritative source. — [Barracuda](https://blog.barracuda.com/2023/08/01/e-book-protect-data-microsoft-365-ransomware)
- SharePoint keeps 14 days of metadata backups on the service side. These are not customer self-service. — [Microsoft Learn: SharePoint/OneDrive data resiliency](https://learn.microsoft.com/sv-se/compliance/assurance/assurance-sharepoint-onedrive-data-resiliency)
- Microsoft 365 Backup is a pay-as-you-go add-on at $0.15/GB/month covering OneDrive, SharePoint and Exchange. Microsoft frames protecting content as the customer's responsibility. I found no nonprofit discount for it. — [Microsoft Learn: Backup pricing](https://learn.microsoft.com/en-us/microsoft-365/backup/backup-pricing); [Redress Compliance](https://redresscompliance.com/microsoft-365-backup-licensing-pricing.html)
- Third-party price claims conflict:
  - One comparison lists Veeam Data Cloud Premium at $7/user/month.
  - Another says about $18-22/user/year.
  - CloudAlly, CrashPlan and IDrive advertise per-user M365/Workspace backup, and IDrive has a nonprofit page.
  — [Nakivo cost guide](https://www.nakivo.com/blog/microsoft-365-backup-costs-guide/); [CloudAlly](https://www.cloudally.com/pricing-for-saas-backup/microsoft-office-365-backup-pricing/); [IDrive nonprofit](https://cloud.idrive.com/microsoft-office-365-backup-for-non-profit)

**Google Workspace**
- Google Drive help: "A version might be permanently deleted after 30 days or if there are 100 newer versions." Native Docs, Sheets and Slides version history works differently from uploaded-file versions. — [Google Drive Help 2409045](https://support.google.com/drive/answer/2409045?hl=en)
- Vendors stress that encryption or deletion discovered after 30 days can mean permanent loss. Spin says it keeps 365 or 100 versions depending on plan; these are vendor claims. — [NinjaOne: retention vs backup](https://www.ninjaone.com/blog/google-workspace-retention-vs-backup/); [Spin.ai](https://spin.ai/?p=64319); [CubeBackup: revert Drive folder](https://www.cubebackup.com/docs/tutorials/revert-google-drive-folder-to-previous-version/)

### Inferences
**Do they need third-party backup?**
- **Minimum for a tiny org:**
  - Keep native defaults (do not lower version limits).
  - Set Google Vault or Purview retention for staff mail and Drive, so deleted mail and files survive account deletion. Vault comes with Business Plus and Education Fundamentals and up.
  - Document the restore steps.
- **Third-party backup is justified when:**
  - The org holds irreplaceable records (safeguarding, custody and pickup authorizations, IEPs) in Drive or OneDrive.
  - Staff turnover leads to account deletions.
  - No one checks files regularly.

  At 10-30 users and typical $2-4/user/month SaaS-backup pricing, that is roughly $250-1,400 a year. This is my inference from the vendor ranges above, not a quoted price.

**Sync-client ransomware: the practical DFIR picture**
- A desktop sync client faithfully uploads the encrypted versions. Recovery means:
  1. isolating the PC
  2. using OneDrive Restore or Google's per-file version history
  3. confirming the encryption happened within the 30-day / 100-version windows
- Google has no one-click "restore entire Drive to a date" equivalent in native tools, which is why tools like CubeBackup document folder-revert procedures. Treat this as inference and verify it.

**The local PC is a separate problem**
- Files saved only locally, and line-of-business apps such as QuickBooks Desktop or a local childcare database, are not protected by cloud sync.
- These need an offline or immutable copy: an external drive rotated and disconnected, or a backup service with versioning.

**Vault and Purview as substitutes**
- They are good for preserving evidence and records.
- They are poor for restoring operations quickly: export is slow and loses folder structure and sharing.

### Gaps
- I did not find authoritative Google documentation on Drive for desktop behavior during a ransomware event (e.g., mass-edit detection or a restore tool comparable to OneDrive's).
- I found no independent, current price comparison of SaaS backup with nonprofit discounts. TechSoup offers were not checked.
- No source confirms Microsoft 365 Backup availability or pricing for nonprofit or Business-tier tenants specifically.

---

## 3. First-hour playbooks: email compromise, payment diversion, ransomware on an office PC, extortion emails to parents. What CISA, NCSC and ACSC recommend, and the gaps

### Takeaway
Government small-org guidance is solid on structure (prepare, identify, resolve, report, learn) but generic:
- NCSC's Small Business Response & Recovery guide (v1.0, Oct 2020)
- ACSC's IR plan template and Email Attacks Emergency Response Guide
- CISA's reporting pages

None of them gives a tiny org cloud-tenant-specific first-hour steps (export logs before resetting, kill sessions, check OAuth grants and forwarding rules). None addresses the child-specific extortion scenario: attackers emailing or phoning parents. The most time-critical playbook is payment diversion. The FBI IC3 Recovery Asset Team (RAT) freezes most funds when contacted fast. The kill chain is widely described as a 48-72-hour window, and some practitioners say it is shrinking toward 12-24 hours.

### Cited Findings
**NCSC (UK)**
- The Small Business Guide: Response & Recovery has five steps: prepare, identify what's happening, resolve, report to wider stakeholders, learn. It is for SMEs; larger organizations are told to use "10 Steps." The PDF is dated October 2020 (v1.0), and I found no 2024+ revision. — [NCSC Step 1](https://www.ncsc.gov.uk/collection/small-business-guidance--response-and-recovery/step-1-prepare-for-incidents); [NCSC Step 2](https://www.ncsc.gov.uk/collection/small-business-guidance--response-and-recovery/step-2-identify-what-s-happening); [PDF](https://www.ncsc.gov.uk/sites/default/files/documents/NCSC%5FA5%20Response%20and%20Recovery%20Guide_v3_OCT20.pdf)
- NCSC published new recovery material in July 2026: "What to do when cyber attacks disrupt your organisation" and "When cyber attacks happen: helping organisations recover." I saw only titles, not contents. — [NCSC PDF 2026-07](https://www.ncsc.gov.uk/sites/default/files/2026-07/NCSC-What-to-do-when-cyber-attacks-disrupt-your-organisation.pdf); [NCSC blog](https://www.ncsc.gov.uk/blogs/when-cyber-attacks-happen-helping-organisations-recover)
- NCSC has separate BEC guidance, and a 24/7 live-incident line (0300 123 2040) that charities can use. — [NCSC BEC PDF](https://www.ncsc.gov.uk/pdfs/guidance/business-email-compromise-defending-your-organisation.pdf); [Report Fraud](https://www.reportfraud.police.uk/business-protection/)
- The NCSC Small Charity Guide covers prevention only, not response. — [NCSC responding to a cyber attack](https://www.ncsc.gov.uk/information/responding-to-a-cyber-attack)

**ACSC (Australia)**
- The Cyber Incident Response Plan template includes appendices for an incident log, an evidence register, situation reports and role cards. It is meant as a starting point. — [ACSC IRP Guidance PDF](https://www.cyber.gov.au/sites/default/files/2023-03/ACSC%20Cyber%20Incident%20Response%20Plan%20Guidance_A4.pdf); [Template .docx](https://soc.cyber.wa.gov.au/pdfs/ACSC-Cyber-Incident-Response-Plan-Template.docx)
- The ACSC Email Attacks Emergency Response Guide includes a "Check account security" step linking to Outlook and Gmail step-by-step guides. — [ACSC Email Emergency Response Guide](https://www.cyber.gov.au/sites/default/files/2023-03/ACSC%20-%20Email%20Security_Emergency-Response-Guide%20-%2020210622.pdf)
- The ACSC Small Business Cyber Security Guide was updated in January 2025 and names BEC via compromised accounts as a common attack. — [ACSC Small business guide Jan 2025](https://cyber.gov.au/sites/default/files/2025-01/ACSC_Small_business_cyber_security_guide_January_2025.pdf)

**FBI IC3 Recovery Asset Team and the Financial Fraud Kill Chain**
- 2024: the RAT froze about $561M with a 66% success rate (per a TRM Labs summary of the 2024 IC3 report; not verified against the primary report). — [TRM Labs](https://www.trmlabs.com/resources/blog/a-record-breaking-year-for-cybercrime-key-findings-from-the-fbis-2024-ic3-report-k1c94)
- 2022: 2,838 incidents, $590.6M in losses, $433.3M frozen, a 73% rate. — [RAT slick sheet CY2022](https://www.IPA.org/uploads/1/3/1/4/131403368/rat_slick_sheet_cy2022.pdf)
- The kill chain applies to domestic transfers. FNF Fraud Insights (undated) describes the window as 48-72 hours, "tending to shrink to 12-24 hours." — [IC3 FFKC Domestic brochure](https://www.ic3.gov/Outreach/Brochures/IC3-FFKC_Domestic.pdf); [FNF Fraud Insights](https://fraudinsights.fnf.com/vol17iss11/article3.htm); [CRS IF13094](https://www.everycrsreport.com/reports/IF13094.html)
- FBI warning (2025): scammers impersonate law enforcement and recovery services to target crime victims a second time. — [Malwarebytes](https://www.malwarebytes.com/blog/news/2025/05/fbi-issues-warning-as-scammers-target-victims-of-crime)

**CISA**
- CISA asks all organizations to report incidents. Reports can be partial and updated later. Channels: report@cisa.gov or (888) 282-0870, per a 2023 contacts sheet; verify the number. — [CISA: Report a cyber incident](https://www.cisa.gov/report-cyber-incident-information-cisa); [CISA reporting](https://www.cisa.gov/reporting-cyber-incident)

### Inferences
These first-hour playbooks are a DFIR practitioner synthesis. Each step should be checked against vendor docs before publication.

**A. Compromised email account (M365 or Google)**
1. Do not delete the account or the mailbox.
2. Export evidence, about 10 minutes:
   - sign-in log for the user (Entra or Google login audit)
   - UAL/audit search for the user over 90-180 days
   - inbox rules
   - forwarding settings
   - OAuth app grants
   - sent items and deleted items
3. Contain:
   - reset the password
   - revoke sessions and refresh tokens (Entra "Revoke sessions"; Google "Sign out" plus reset sign-in cookies)
   - remove attacker MFA methods
   - remove malicious inbox rules, forwarding and OAuth apps
4. Search sent mail for phishing sent to parents and vendors, and warn those recipients.
5. Decide whether this is a reportable breach. Mailbox contents with child data likely qualify; see Q5.

**B. Payment or payroll diversion discovered**
1. Within minutes, call the bank's fraud line and ask for a recall or SWIFT/ACH reversal.
2. File at ic3.gov with the transaction details.
3. Call the local FBI field office.

Speed beats completeness. The 48-72-hour figure is a ceiling, not a target. Then treat it as playbook A, because a payment diversion is almost always an email compromise (the org's own or the vendor's).

**C. Ransomware on an office PC**
1. Pull the network cable or turn off Wi-Fi. Do not power off, so memory survives if a responder wants it.
2. Photograph the ransom note.
3. Pause sync clients on other machines.
4. From a clean device, check OneDrive or Drive for mass changes and start the restore.
5. Call the insurer hotline before hiring anyone. Most cyber policies require the panel vendors.

**D. Extortion emails or calls to parents**

The earlier notes document this from Kido and PowerSchool.
1. Send a pre-approved family message within hours: do not reply, do not pay, preserve the email, forward headers to a designated address, report to IC3.
2. Give child credit-freeze steps.
3. Name one spokesperson.
4. Do not confirm or deny the specific data claims until verified.

**Gaps in government guidance**
- No cloud-tenant evidence-preservation steps.
- No "attacker contacts parents" scenario.
- No safeguarding-data triage, i.e., asking first whether child-protection files were in scope.
- Nothing on insurer-first sequencing.
- NCSC's small-business guide is 6 years old.

### Gaps
- I could not fetch the IC3 FFKC brochure to quote its exact current criteria. Historically: domestic wire, BEC-related, reported within 72 hours, above a dollar threshold (often cited as $50K). Verify before use.
- I did not find a CISA small-org-specific first-hour playbook. CISA's Ransomware Guide (#StopRansomware) exists but was not retrieved in this pass.
- I found no government playbook addressing extortion contact with parents.

---

## 4. Free help in the US: who serves private, religious and childcare organizations?

### Takeaway
The free incident-response capacity that exists in the US is overwhelmingly built for **public** entities:
- NY State's CIRT and Shared Services serve local governments and public authorities.
- National Guard cyber teams have mostly served public school districts.
- State programs generally follow the same pattern.

For a parish school, private classical school, childcare center or youth nonprofit, the realistic free help is:
1. CISA (reporting, regional Cybersecurity Advisors, free Cyber Hygiene scanning)
2. FBI (IC3 and field office, for fund recovery and extortion)
3. University cyber clinics (NYU, the Consortium)
4. The insurer's breach coach, if the org has a cyber policy or a diocesan or master policy

These are mostly pre-incident or advisory help. Hands-on IR for a private nonprofit typically comes through an insurer, or is paid for.

### Cited Findings
**CISA**
- Each CISA region has Cybersecurity Advisors (CSAs). CISA's recommended first three services are: connect with a CSA, sign up for Cyber Hygiene scanning, take the CPG assessment. CISA keeps a list of free services and tools. — [CISA Regions](https://www.cisa.gov/regions); [CISA Services Fact Sheet](https://cisa.gov/resources-tools/resources/cisa-services-fact-sheet-regions)

**New York State**
- NY State CIRT (DHSES): free IR and proactive services for **local governments, non-Executive agencies and public authorities**, with a 24/7 line, 1-844-OCT-CIRT. — [DHSES CIRT](https://www.dhses.ny.gov/cyber-incident-response-team); [DHSES cybersecurity services](https://www.dhses.ny.gov/cybersecurity-services)
- The NY Joint Security Operations Center (JSOC, Brooklyn, 2022) coordinates federal, state and local governments and critical infrastructure. The governor's office said K-12 schools are among the institutions covered, but the reporting does not distinguish public from private schools. — [Governor's announcement Feb 2022](https://www.governor.ny.gov/news/governor-hochul-announces-formation-joint-security-operations-center-oversee-cybersecurity); [K-12 Dive](https://www.k12dive.com/news/new-york-rolls-out-statewide-cyber-command-center-amid-russian-attacks-in-u/619698/)
- A 2026 NASCIO document refers to a "NYSOC" ecosystem that includes schools. — [NASCIO NY Cybersecurity 2026](https://www.nascio.org/wp-content/uploads/2026/08/NY_Cybersecurity.pdf)
- The NY Cyber Shared Services Program (2022, $30M) offers free tools to eligible local governments. — [Governor, Jul 2022](https://www.governor.ny.gov/news/governor-hochul-announces-launch-30-million-shared-services-program-enhance-cyber-defenses)

**National Guard**
- Of 41 recorded state cyber-support cases since 2018, 23 were ransomware, and 7 of those targeted public school systems. Examples: Louisiana, 2019 (school districts); Arizona's blanket agreement covering school districts. — [ExecutiveGov](https://www.executivegov.com/articles/think-tank-finds-governors-mostly-use-national-guard-cyber-response-for-ransomware-cases); [National Guard](https://www.nationalguard.mil/News/Article/1941732/guard-cyber-teams-called-in-to-get-schools-agencies-back-online); [Arizona agreement](https://reservenationalguard.com/civilian-employers/cyber-joint-task-force-agreement-allows-guardsmen-to-protect-school-networks/)
- Pennsylvania Guard Task Force CYBER (2025) serves local governments, schools and infrastructure partners, and tells organizations to call to check eligibility. — [PA DMVA](https://www.pa.gov/agencies/dmva/about-dmva/newsroom/pang-s-task-force-cyber-saves-nearly--600k-from-online-threats-i)

**Clinics**
- CISA publishes resources specifically for cyber clinics (Feb 2024). The Consortium has about 61 clinics. NYU's clinic (2026) serves organizations without significant IT staff, including schools. — via earlier notes: [CISA clinic resources](https://www.cisa.gov/sites/default/files/2024-02/Resources-for-Cybersecurity-Clinics-508c%20%281%29%20%281%29.pdf); see economics_insurance_funding.md section 6

**Insurer response**
- In the 2024 Castilleja School (private) incident, the school contacted its insurer, hired third-party attorneys and reported to the FBI. This is the typical insurer-led path. — [Huntress cost guide / reporting](https://www.huntress.com/cybersecurity-for-education-guide/cost-of-a-school-cyberattack)

### Inferences
- **Eligibility:** private, religious and childcare organizations fall outside most state IR programs by their eligibility language ("local governments, public authorities"). Calling anyway costs nothing. JSOC and NYC Cyber Command may give advice or referrals, especially in a mass event like PowerSchool.
- **University clinics:** they are not incident responders. Typical engagements are semester-long assessments. Their value is preparing the breach-day kit before an incident.
- **The insurer:** for most tiny orgs, the insurer's 24/7 hotline is the de facto free IR team (breach coach, plus panel forensics and notification vendors). Check the parish or diocesan master policy: earlier notes mention Catholic Mutual and Church Mutual. The project should help orgs find out whether they have cyber coverage and what the hotline number is.
- **FBI:** the field office (for NYC, FBI New York) is the right call for extortion and payment fraud. The FBI does not do remediation.

### Gaps
- I found no explicit statement on whether NY CIRT, JSOC or NYC Cyber Command will assist a private or religious school or a childcare center. This should be asked directly.
- I found no National Guard program that explicitly covers private schools.
- I did not verify the current status of CISA's CSA program after 2025 federal staffing changes.
- I did not research NYC-specific contacts (NYC Cyber Command's public-facing services, the NYPD Computer Crimes Squad).

---

## 5. Breach notification obligations, templates, communicating with parents during extortion, and child credit freezes

### Takeaway
In New York, a private school, childcare center or youth nonprofit is most clearly bound by the **SHIELD Act**, GBL § 899-aa. As amended in December 2024 (S2659B), it requires notice to affected NY residents **within 30 days of discovery**, and notice to the AG, Department of State and State Police (with DFS added) when residents are notified.

**Education Law 2-d** binds "educational agencies": school districts, BOCES, charter schools (per a secondary source), the State Education Department, and "school" under its definition. Whether it reaches non-public or religious schools is not settled by the sources found; the likely answer is mostly no. Its main relevance to private schools is through BOCES-provided or district-provided services.

Every org should pre-write a family letter that combines:
- what happened
- do not engage with or pay extortionists
- the IC3 reporting route
- child credit-freeze steps

### Cited Findings
**NY SHIELD Act**
- The December 2024 amendment (S2659B) added that notice "shall be made within thirty days following discovery." Previously the statute said "most expedient time possible." — [Constangy](https://constangy.com/constangy-cyber-advisor/are-you-in-the-know-new-york-amends-data-breach-law); [Covington Inside Privacy](https://www.insideprivacy.com/cybersecurity-2/new-york-adopts-amendment-to-the-state-data-breach-notification-law/); [Baker McKenzie](https://connectontech.bakermckenzie.com/new-york-caps-2024-with-changes-to-cybersecurity-laws/)
- If residents are notified, the AG, Department of State and State Police must also be notified. A vendor maintaining data on behalf of another must notify the data owner. — [Sullivan & Cromwell](https://www.sullcrom.com/SullivanCromwell/_Assets/PDFs/Memos/SC-Publication-New-York-Amends-Data-Breach-Notification-Statute.pdf); [NY AG SHIELD Act](https://ag.ny.gov/index%2Ephp/resources/organizations/data-breach-reporting/shield-act)
- A4737B (effective March 21, 2025) adds medical information and health insurance information to covered data. Relevant for allergy and medical records held by schools and childcare. — [Covington](https://www.insideprivacy.com/cybersecurity-2/new-york-adopts-amendment-to-the-state-data-breach-notification-law/)

**Education Law 2-d**
- An educational agency is a school district, BOCES, school, or the State Education Department. — [NYSED 2-d definitions](https://www.nysed.gov/data-privacy-security/education-law-section-2-d-definitions)
- A contract-clause compilation adds charter schools. — [Law Insider](https://www.lawinsider.com/clause/educational-agency/_1)
- A third-party contractor is an entity receiving student data from an educational agency under contract. — [NYSED 2-d definitions](https://www.nysed.gov/data-privacy-security/education-law-section-2-d-definitions)

**Child credit freezes**
- A free credit freeze for children under 16 ("protected consumers") has been available at all three bureaus since September 2018. — earlier notes: [FTC](https://consumer.ftc.gov/consumer-alerts/2019/03/new-protections-available-minors-under-16)

**Parent communication examples and pitfalls**
- Castilleja School's 2024 letter to parents named the affected departments (College Counseling, Advancement, Food Services) and the steps taken (insurer, attorneys, FBI). — [Huntress](https://www.huntress.com/cybersecurity-for-education-guide/cost-of-a-school-cyberattack)
- Reynella East College (Australia) sent parent updates advising caution and password changes. — [Cyber Daily](https://www.cyberdaily.au/security/13937-reynella-east-college-updates-parents-carers-following-june-data-breach)
- A 2025 investigation of 300+ school cyberattacks found school leaders "repeatedly provide false assurances" about security. — [The 74](https://www.the74million.org/article/data-breach/)
- Fisher Phillips covered the PowerSchool follow-on extortion targeting individual schools. — [Fisher Phillips](https://www.fisherphillips.com/print/v2/content/40984/powerschool-cybercriminal-returns-to-extort-individual-schools.pdf)

### Inferences
**Parent-communication rules, drawn from The 74's findings and the Kido and PowerSchool cases**
- Never say "no evidence data was accessed" before forensics. Say what is known and what is not.
- Commit to an update cadence.
- Explicitly warn families that attackers may contact them directly and impersonate the school.
- Give a verification channel, such as a phone number on the school's website.

**Timeline and notice planning**
- The 30-day NY clock argues for pre-drafted letter templates and a pre-identified breach counsel, typically through the insurer.
- Child data such as names, birthdates and medical information may trigger SHIELD only in certain combinations: SHIELD's "private information" requires specific data elements. Breach counsel should decide.
- Mailbox compromises frequently contain SSNs or medical records in attachments (enrollment forms, tuition-aid documents). This is a common DFIR finding, and it makes "did the attacker read the mailbox?" (MailItemsAccessed) legally significant.

**Federal angle**
- FERPA applies only to schools receiving federal Department of Education funds. Many private schools do not. COPPA applies to operators of online services, not schools as such.
- These are background knowledge; check against privacy_law.md.

### Gaps
- I found no authoritative NYSED statement on whether 2-d applies to non-public or religious schools.
- I did not compile a 50-state comparison. I did not retrieve state breach-letter templates, though CA, MA and NY AG offices publish sample forms.
- I found no tested template for the "attacker is contacting parents" letter. The project would be first to publish one.

---

## 6. After-action realities: how small orgs recover, costs, lessons

### Takeaway
Published cost data is district-scale and skews high:
- GAO (2023): $50K-$1M losses, 3 days to 3 weeks of lost learning, 2-9 months to recover
- Sophos, lower education (2024): mean $3.76M
- FDD (2025): K-12 average $2.28M

Tiny private orgs rarely publish post-mortems, so there is almost no public small-org recovery data. The recurring lessons are:
- the exposure of private records outlasts the outage
- slow containment extends recovery
- overconfident early messaging damages trust

### Cited Findings
- GAO (2023): lost learning ranged from 3 days to 3 weeks; recovery took 2-9 months; monetary losses were $50K-$1M. — [Huntress summary](https://www.huntress.com/cybersecurity-for-education-guide/cost-of-a-school-cyberattack)
- FDD (Sep 2025): average K-12 ransomware recovery is $2.28M, the highest of targeted sectors; the trauma of records exposure is the lasting legacy. — [FDD](https://www.fdd.org/analysis/2025/09/19/hackers-are-costing-k-12-school-systems-more-than-money/)
- IBM: education recovery is prolonged when ransomware is not contained quickly. — [IBM](https://www.ibm.com/think/insights/reducing-ransomware-recovery-costs-in-education)
- Small-entity data point: a SC district (DD2) paid a $2,900 ransom to recover data after a server breach. — [ABC News 4](https://abcnews4.com/news/education-news/dd2-says-2900-ransom-paid-to-recover-data-after-server-breach-but-no-identities-stolen)
- NYC private-school example: a ransomware attack on an "elite Bronx private school" exposed student information. — [News12](https://brooklyn.news12.com/ransomware-attack-on-elite-bronx-private-school-exposes-students-personal-information)
- Francis Parker School (San Diego, private) warned parents of a ransomware attack. — [10News](https://www.10news.com/news/local-news/francis-parker-school-warns-parents-of-ransomware-attack)
- Lockton: lessons for schools and risk professionals from education ransomware. — [Lockton](https://global.lockton.com/us/en/news-insights/ransomware-hits-the-educator-sector-lessons-learned-for-schools-and-risk)

### Inferences
These come from a DFIR practitioner's view of small-org cases, consistent with the sources above.

**Where the money goes for a 10-50 person org**
1. Forensics and breach counsel, often $15K-$60K through an insurer panel, typically below the retention or deductible for small policies. This is an estimate; I found no source.
2. Notification and credit monitoring.
3. Staff time and lost operations.
4. Reputation and enrollment loss, which is never measured.

**Why tiny orgs recover badly**
- No asset inventory.
- No one knows the admin passwords.
- The "IT person" is a parent volunteer or the principal's relative.
- Backups were never tested.
- MFA recovery codes are lost.

All five are addressable by a breach-day kit (Q7).

**Lesson for the project**
- The cheapest recovery wins: cloud-first data plus native restore windows, combined with MFA and preserved logs.
- These reduce a "ransomware" event to a "one PC reimaged" event.

### Gaps
- I found no published board minutes or detailed post-mortems from a US parish school, childcare center or youth nonprofit.
- I found no small-org-specific cost data. The NetDiligence SME claims data was not retrieved.
- Recovery cost figures from vendor sources (Sophos, Huntress) carry vendor bias.

---

## 7. What a "breach-day kit" should contain, and how to keep it offline

### Takeaway
No government source I found provides a ready "breach-day kit" for tiny child-serving orgs. ACSC's IRP template appendices (incident log, evidence register, sitrep, role cards) and NCSC's "prepare" step are the closest. The project can fill this gap with:
- a printed, sealed, two-location kit
- one-page decision trees
- tenant-specific log-export instructions
- pre-written family letters

### Cited Findings
- The ACSC IRP template includes appendices for an incident log, evidence register, situation reports and role cards. — [ACSC IRP Guidance](https://www.cyber.gov.au/sites/default/files/2023-03/ACSC%20Cyber%20Incident%20Response%20Plan%20Guidance_A4.pdf)
- NCSC Step 1, "Prepare for incidents": identify critical functions, back up, plan whom to call. — [NCSC Step 1](https://www.ncsc.gov.uk/collection/small-business-guidance--response-and-recovery/step-1-prepare-for-incidents)
- Entra and Google log retention limits make pre-incident export instructions necessary. — [Entra retention](https://learn.microsoft.com/en-us/entra/identity/monitoring-health/reference-reports-data-retention); [Google retention](https://knowledge.workspace.google.com/admin/reports/data-retention-and-lag-times)
- IC3 fund recovery depends on hours, so bank fraud numbers and the IC3 URL must be at hand. — [CRS IF13094](https://www.everycrsreport.com/reports/IF13094.html); [FNF](https://fraudinsights.fnf.com/vol17iss11/article3.htm)
- Scammers target crime victims with fake recovery offers, so the kit should list only verified contacts. — [Malwarebytes on FBI warning](https://www.malwarebytes.com/blog/news/2025/05/fbi-issues-warning-as-scammers-target-victims-of-crime)

### Inferences
**Proposed kit contents (practitioner synthesis)**

1. **Contacts card, one page**
   - insurer 24/7 hotline and policy number
   - breach counsel
   - bank fraud line, plus the account officer's direct line
   - FBI field office (FBI New York for NYC)
   - ic3.gov
   - CISA, report@cisa.gov or (888) 282-0870 (verify)
   - state AG breach portal
   - the M365/Workspace reseller or volunteer admin
   - key vendors: SIS, tuition, childcare app, payroll
   - diocese or association contact

2. **Access materials, in a sealed envelope**
   - break-glass global admin or super admin credentials: an account excluded from routine use, with a hardware key or recovery codes
   - MFA recovery codes for the admin accounts
   - domain registrar and DNS login
   - bank portal admin recovery details

3. **Inventory**
   - list of systems and where child data lives (SIS, childcare app, Drive folders, paper)
   - which systems hold safeguarding and child-protection records, the highest-priority triage question

4. **Log export steps, screenshot-illustrated for that org's tenant**
   - Entra sign-ins export
   - Purview audit search export
   - Google Admin, Reporting, Audit and investigation, login and Gmail export
   - Vault export
   - an "export before reset" warning in bold

5. **Decision trees, one page each**
   - email compromise
   - payment diversion ("call the bank first")
   - ransomware PC
   - extortion contact to parents
   - lost or stolen device

6. **Letter templates**
   - staff notice
   - family notice: initial, update, final
   - extortion-warning letter to families, with child credit-freeze steps for Equifax, Experian and TransUnion, plus IdentityTheft.gov
   - regulator notice checklist (NY: AG, DOS, State Police, within 30 days)

7. **Incident log sheet** (ACSC-style): time, action, who, evidence reference.

8. **Restore notes**
   - how to run OneDrive "Restore your OneDrive" or the Drive version restore
   - where the offline backup drive is

**Keeping it offline**
- Print it.
- Keep one copy in the office safe and one at the board chair's or pastor's home.
- An encrypted USB is optional. Never keep the only copy inside the tenant that may be compromised.
- Review it each term, as part of an annual 30-minute tabletop exercise.
- Rotate break-glass credentials whenever the holder changes.

**What the project could build**
- a fill-in-the-blanks kit generator, split into M365 and Google variants
- printable decision trees
- a tested parent-extortion letter
- a "first 60 minutes" card

These fill the documented gaps in Q3 and Q5.

### Gaps
- I found no published, validated breach-day kit tailored to US schools or childcare.
- I did not find CISA's or a state's sample tabletop for small nonprofits; CISA Tabletop Exercise Packages exist but were not retrieved.
- Effectiveness data for such kits (did they shorten response?) is absent.
