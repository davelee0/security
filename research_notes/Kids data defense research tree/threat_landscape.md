# Threat Landscape: Small Organizations Holding Children's Data (2023-2026)

Research method note: Direct page fetching was blocked in this environment (comparitech.com and helpnetsecurity.com failed DNS resolution), so the findings below come from web search result summaries. Every figure is tied to the URL the search returned. Exact numbers should be checked against the primary PDF before publication. Dates of figures are given in brackets.

## 1. Which attack types most often hit schools, childcare, and dioceses (2024-2026), and how often?

### Takeaway
Ransomware and data-theft extortion against education stayed roughly flat at a high level in 2025, about 250 publicly claimed attacks a year worldwide. The everyday incidents that actually cost money or expose data are account takeover, phishing that leads to payroll or vendor payment diversion, and vendor/third-party breaches. Payroll and vendor-payment fraud losses per incident (roughly $12K to $6M) often exceed what a small school would face from ransomware.

### Cited Findings
**Overall incident rates**
- [Report published Oct 27, 2026, covering the 2025-26 school year] CIS/MS-ISAC/CoSN "State of K-12 Cybersecurity 2026": 51% of schools/districts reported a cyber incident in the past 12 months, and 34% reported impacts to school operations. More than 11,600 K-12 incidents needed escalation among the 1,764 K-12 organizations using MS-ISAC services. — [Route Fifty](https://www.route-fifty.com/cybersecurity/2026/11/more-half-schools-suffered-cyber-incident-past-year-report-finds/416972/); [K-12 Dive](https://www.k12dive.com/news/cybersecurity-incidents-hit-over-50-of-schools-and-districts-in-past-year/872783/); [CIS report page](https://www.cisecurity.org/insights/white-papers/state-k-12-cybersecurity-report-2026)
- [2026 report] About 13% of schools/districts receiving MS-ISAC monitoring had a credential compromise or exposure. 83% say they have implemented MFA and email security protections. Note that this is self-reported, and MFA may cover only some accounts. — [K-12 Dive](https://www.k12dive.com/news/cybersecurity-incidents-hit-over-50-of-schools-and-districts-in-past-year/872783/); [CIS press release](https://www.cisecurity.org/about-us/media/press-release/cis-ms-isac-cosn-report-k12-schools-face-growing-cyber-threats-ai-adoption)
- [Report released Mar 2025, covering Jul 2023 to Dec 2024] CIS 2025 K-12 report: 82% of reporting K-12 organizations experienced cyber threat impacts. Sources summarizing it give different confirmed-incident counts (about 9,300 vs 8,100), which shows that secondary reporting of these figures is inconsistent. — [THE Journal](https://thejournal.com/articles/2025/03/19/cis-study-finds-82-of-k-12-organizations-experienced-cyber-threat-impacts-in-the-past-18-months.aspx); [CIS](https://www.cisecurity.org/insights/white-papers/2025-k12-cybersecurity-report)
- [2023] K12 SIX had cataloged more than 1,300 publicly disclosed K-12 cyber incidents since 2016. I found no K12 SIX "State of K-12 Cybersecurity" report for 2025 or 2026 in search results. K12 SIX contributed data to the Verizon 2025 DBIR. — [K12 SIX release](https://www.k12six.org/releases-announcements/k12-six-contributes-to-verizon-2025-data-breach-investigations-report); [BusinessWire 2023](https://www.businesswire.com/news/home/20230202005174/en)

**Ransomware volume (Comparitech, which counts both claims and confirmed attacks)**
- [Q1 2025] 81 education ransomware attacks, up 69% year over year. 22 were confirmed. — [K-12 Dive](https://www.k12dive.com/news/ransomware-attacks-surge-69-across-global-education-sector/)
- [H1 2025] 130 attacks, up 23% year over year. Average ransom demand was $556,000. — [K-12 Dive](https://www.k12dive.com/news/ransomware-attacks-education-jump-23-percent-h1-2025/753483/)
- [Full year 2025] 251 attacks: 94 confirmed and 157 unconfirmed, about 2% more than 2024. The US had 130 (50 confirmed). Average ransom demand was $464,000. Top claimants were Qilin (37), SafePay (23), Fog and Interlock (18 each), and INC (17). Interlock led confirmed attacks with 11, followed by Qilin with 9. — [Comparitech 2025 roundup](https://www.comparitech.com/news/education-ransomware-roundup-2025-stats-on-attacks-ransoms-and-data-breaches/); [K-12 Dive](https://www.k12dive.com/news/ransomware-attacks-against-education-sector-slow-worldwide/811133/); [THE Journal Jan 2026](https://thejournal.com/articles/2026/01/22/report-ransomware-attacks-plateau-in-education-sector-while-third-party-risks-loom-large.aspx?p=1)
- [Late 2025] Comparitech reported the first quarterly dip in education ransomware since 2024. — [K-12 Dive](https://www.k12dive.com/news/first-dip-ransomware-attacks-quarters-since-2024-comparitech/804339/)
- An H1 2026 Comparitech education roundup exists, but its contents were not retrieved. — [Comparitech H1 2026](https://www.comparitech.com/news/education-ransomware-roundup-h1-2026-stats-on-attacks-ransoms-and-data-breaches/)

**Sophos State of Ransomware in Education 2025** [survey Jan-Mar 2025; published Aug/Sep 2025; 243 lower-ed and 198 higher-ed respondents across 17 countries]
- Lower-ed average recovery cost fell 39% from $3.76M (2024). Education went from among the highest ransom payers in 2024 to among the lowest in 2025. 22% of lower-ed ransomware attacks started with phishing. 97% recovered encrypted data. — [Sophos blog](https://www.sophos.com/en-us/blog/the-state-of-ransomware-in-education-2025); [Sophos press release](https://www.sophos.com/en-us/press/press-releases/2025/09/sophos-ransomware-education-report-2025); [PDF](https://assets.sophos.com/X24WTUEQ/at/5s8hqqszx4kckr3m5rhjp54/sophos-state-of-ransomware-in-education-2025.pdf)
- Caveat: regional Sophos pages give different median demand and payment figures. Use the English PDF for exact numbers.

**BEC / payroll and vendor-payment diversion (the under-counted money loss)**
- [Feb 2026] Dickinson Public Schools (ND) lost about $4.92M after criminals impersonated a vendor and redirected two payments. — [Valley News Live](https://www.valleynewslive.com/2026/02/11/north-dakota-school-district-loses-nearly-5-million-sophisticated-email-scam/?outputType=amp)
- [Aug 2025, discovered late Oct 2025] Sudbury (MA) Public Schools: a payroll specialist clicked a phishing link. Attackers took over payroll and email accounts, **intercepted MFA**, and diverted more than $12,000 in payroll. The district did not tell the town finance office. — [Sudbury Weekly](https://sudburyweekly.com/sps-hit-by-payroll-cyberattack-in-2025-over-12000-diverted/)
- [Nov 2024; Oct 2025] Ohio Auditor findings: a payroll officer changed an employee's routing number after an email request, and a teacher's compromised account was used to request a direct-deposit change. Auditors noted that districts had no verification policy until after the loss. — [Ohio Auditor](https://ohioauditor.gov/news/PressReleases/Details/7603); [Ohio Auditor](https://ohioauditor.gov/news/PressReleases/Details/7799); [AOL/Maysville](https://www.aol.com/news/cyber-scam-mars-otherwise-clean-090147882.html)
- [2024] A Tennessee district lost more than $3M to a fake-vendor BEC. — [The Record](https://therecord.media/tennessee-school-district-loses-3-million-bec-scam)
- [Mar 2024] Seminole County (FL) Public Schools lost $1.3M. — [ClickOrlando](https://clickorlando.com/news/local/2024/03/04/13m-lost-after-scammers-target-seminole-county-public-schools)
- [Mar 2024] Philadelphia: a hijacked vendor email requested $563K, and nearly $700K was diverted in total. — [PhillyVoice](https://www.phillyvoice.com/school-district-philadelphia-cyber-fraud-scheme/)
- [2023] New Haven (CT) lost more than $6M via the COO's compromised email ($3.6M recovered). — [Insurance Journal](https://www.insurancejournal.com/news/east/2023/08/14/735130.htm)
- Independent-school business offices are explicitly targeted by BEC. — [Venable 2023](https://www.venable.com/insights/publications/2023/02/online-fraud-aimed-at-independent-school-bus)

**Account takeover chains**
- [Oct 2026] CIS reports "account takeover hopping": an attacker phishes one legitimate school account, then phishes that account's contacts, including staff at other districts. CIS expects this to continue in 2026-27. CIS recommends expanding MFA, monitoring for exposed credentials, reviewing privileged accounts, and running tabletop exercises. — [Help Net Security](https://www.helpnetsecurity.com/2026/10/29/cis-k-12-cybersecurity/)

### Inferences
- For a small private school, parochial school, or childcare center, the most likely costly event is a compromised staff mailbox. That leads to payroll or vendor bank-detail change fraud, or to phishing of parents and other schools from a trusted address. Full ransomware is less likely. Ransomware counts (about 250 per year globally) are small compared with the more than 11,600 escalated incidents MS-ISAC saw.
- The Sudbury case shows that ordinary push or code MFA can be phished in real time (adversary-in-the-middle). Out-of-band verification of bank changes is the control that actually stops the loss.

### Gaps
- FBI IC3 education-sector complaint and loss figures for 2024 and 2025 were not found in searches. The IC3 annual reports do not appear to break out education clearly.
- No quantitative data was found on credential stuffing against parent portals specifically.
- No state AG breach-portal aggregate for schools or childcare was found.

## 2. Ransomware groups, children's data on leak sites, and direct extortion of parents and students

### Takeaway
Leak sites have repeatedly published the most sensitive child records: psychological evaluations, sexual-misconduct and abuse reports, special education files, and medical data. Districts have often understated what leaked. Since 2023 there is a clear and growing trend of criminals contacting parents, students, and staff directly: Minneapolis and Allen ISD (2023), PowerSchool follow-on extortion (May 2025), and Kido nursery attackers phoning parents (Sep 2025).

### Cited Findings
- [2023] Minneapolis Public Schools / Medusa: the leak included campus sexual misconduct cases, child abuse inquiries, mental health crises, and suspension reports. The district later acknowledged about 2,000 student psychological assessments were leaked. — [The 74](https://www.the74million.org/article/from-campus-rape-cases-to-child-abuse-reports-worst-case-data-breach-rocks-mn-schools/); [The 74 "Kept in the Dark"](https://www.the74million.org/article/kept-in-the-dark-inside-the-minneapolis-schools-cyberattack/); [The 74, hackers' new threat](https://www.the74million.org/article/hackers-use-stolen-student-data-against-minneapolis-schools-in-brazen-new-threat/)
- [2024] Providence (RI) / Medusa: after the district refused a $1M demand, the gang posted sexual misconduct complaints, special education records, and vaccine histories. The district publicly said there was no evidence student data was exposed. — [The 74](https://www.the74million.org/article/providence-students-sensitive-data-exposed-in-cyberattack-district-denies-leak/); [The 74](https://www.the74million.org/article/providence-hack-exposes-thousands-of-sensitive-student-records/)
- [2022, reported through 2025] LAUSD / Vice Society: student psychological evaluations were posted. The superintendent first called the claim "absolutely incorrect," then the district acknowledged about 2,000 were exposed. — [The 74](https://www.the74million.org/article/trove-of-l-a-students-mental-health-records-posted-to-dark-web-after-cyber-hack/?web_view=true); [Route Fifty Feb 2025](https://www.route-fifty.com/cybersecurity/2025/02/kept-dark-inside-trio-los-angeles-school-cyberattacks/402862/?oref=rf-next-story)
- The 74's reporter investigated more than 300 school cyberattacks, which documents a systemic pattern of minimized disclosure. — [The 74](https://www.the74million.org/article/the-story-behind-the-story-how-i-investigated-more-than-300-cyberattacks/)
- [Year not shown in snippet; Allen ISD attack widely reported in 2022] Allen ISD (TX): after the district refused to pay, hackers emailed employees, parents, and students threatening to publish data. — [NBC DFW](https://www.nbcdfw.com/news/local/howdy-hackers-email-parents-and-students-after-allen-isd-refuses-to-pay-ransom/2758256)
- Clark County (NV): a hacker used a compromised email account from another school district to email a parent directly with their child's data. This frightened families and pressured the district. — [The 74](https://www.the74million.org/article/why-a-new-type-of-cyberattack-on-las-vegas-schools-should-worry-everyone/)
- [May 2025] PowerSchool follow-on extortion: PowerSchool paid about $2.9M in Dec 2024, but the data was not deleted. Districts in the US and Canada received extortion demands, including more than 20 NC districts plus the NC Department of Public Instruction. Toronto officials told parents the actor had contacted them directly. — [The 74](https://www.the74million.org/article/powerschool-paid-off-hackers-after-huge-breach-now-theyre-extorting-districts/); [EdWeek](https://edweek.org/technology/powerschool-paid-a-hackers-ransom-now-cyber-criminals-are-threatening-schools/2025/05); [BleepingComputer](https://www.bleepingcomputer.com/news/security/powerschool-hacker-now-extorting-individual-school-districts/?es_id=bce4c8df88); [ABC11](https://abc11.com/post/powerschool-hackers-attempt-extort-money-north-carolina-schools-staff/16352928/); [CBC](https://www.cbc.ca/1.7529277)
- [Oct 2025] Matthew Lane (19, Massachusetts) was sentenced to 4 years, about $14.1M restitution, and a $25K fine. Initial access was a PowerSchool contractor's credentials in Sep 2024. Most of the roughly $3M paid is unaccounted for. — [CyberScoop](https://cyberscoop.com/powerschool-hacker-matthew-lane-sentenced/); [SecurityWeek](https://www.securityweek.com/four-year-prison-sentence-for-powerschool-hacker/); [K-12 Dive lessons learned](https://www.k12dive.com/news/powerschool-hacker-sentencing-lessons-learned-data-breach/803053/)
- [Sep 2025] Kido nurseries (UK) / "Radiant": data on about 8,000 children was stolen, including names, photos, addresses, birthdates, parent details, safeguarding notes, and medical records. The group posted profiles and photos of 10 children and phoned parents to pressure the nursery. After public backlash it claimed to delete the data (unverified). Two 17-year-olds were arrested. — [Malwarebytes](https://www.malwarebytes.com/blog/news/2025/09/hackers-threaten-parents-get-nursery-to-pay-ransom-or-we-leak-your-childs-data); [Malwarebytes Oct 2025](https://www.malwarebytes.com/blog/news/2025/10/from-threats-to-apology-hackers-pull-child-data-offline-after-public-backlash); [Bitdefender](https://www.bitdefender.com/en-us/blog/hotforsecurity/kido-nursery-cyber-attack-arrests)
- Groups most active against education in 2025: Qilin, SafePay, Fog, Interlock, INC (see Q1 citations). Earlier school-focused groups were Medusa (2023-2024) and Vice Society (2022). — [Comparitech](https://www.comparitech.com/news/education-ransomware-roundup-2025-stats-on-attacks-ransoms-and-data-breaches/)

### Inferences
- The threat is no longer "pay or lose your files." Children and parents are being made into leverage. Small organizations need a pre-written parent communication that says do not engage, do not pay, and report, plus guidance on credit freezes for children. Kido and PowerSchool show that paying does not guarantee deletion.
- Counseling notes, IEP/504 files, safeguarding/custody notes, and medical forms are the highest-harm data. They are often kept on shared drives or in email, outside the SIS. Minimizing and locking down that data reduces harm more than any single tool.
- Teenage and young-adult offenders (Lane, the Kido arrests) and "Com"-style actors show that capability is low. Basic controls defeat many of these attackers.

### Gaps
- No quantified dataset of what data types appear on education leak sites.
- No confirmed 2024-2026 cases found of attackers emailing US parents directly outside the PowerSchool context. The Clark County article's year was not confirmed in the snippet.

## 3. Catholic dioceses, Catholic and private schools, and childcare chains (2023-2026)

### Takeaway
Most diocesan and Catholic-school exposure came through vendors (PowerSchool, Berkeley Research Group) and staff email compromise, not direct network ransomware. Private-school and childcare incidents are real but thinly reported. Childcare platforms have suffered both ransomware (Kido via a public-facing app) and simple database misconfiguration (LineLeader, about 140K records).

### Cited Findings
- [2025] Berkeley Research Group (BRG), a bankruptcy consultant, suffered ransomware. Data of several bankrupt Catholic dioceses (abuse-case Chapter 11s, including Baltimore) was stolen. BRG paid the actor for a promise to delete. This was disclosed in at least 8 diocese bankruptcy dockets. Abuse-survivor data is extraordinarily sensitive. — [Bloomberg Law](https://news.bloomberglaw.com/bankruptcy-law/bankrupt-catholic-groups-data-stolen-in-brg-ransomware-attack); [Yahoo/Baltimore](https://www.yahoo.com/news/sensitive-information-baltimore-archdiocese-data-170000215.html)
- [2025] Archdiocese of Baltimore Catholic schools and Diocese of Arlington schools were affected via PowerSchool. Diocesan networks were not breached. — [Arch Baltimore](https://www.archbalt.org/?p=194445); [Arlington notice](https://allsaintsvaschool.org/wp-content/uploads/2025/06/Catholic-Diocese-of-Arlington-PowerSchool-Website-Notice-Updated-6-9-25.pdf)
- [2025] Diocese of Cleveland: an unauthorized party may have accessed an employee email account. — [Yahoo](https://www.yahoo.com/news/just-cleveland-catholic-diocese-security-143315998.html)
- [2025] Roman Catholic Diocese of Fall River filed a Massachusetts breach notice on behalf of Trinity School. — [Mass.gov](https://www.mass.gov/doc/2025-1391-roman-catholic-diocese-of-fall-river-on-behalf-of-trinity-school/download)
- [2025] Diocese of Las Cruces denied a hack claim. — [Yahoo](https://www.yahoo.com/news/articles/las-cruces-diocese-says-no-221110046.html)
- Leak-site listings (unverified, tracker sites): St. Francis Xavier Catholic School System (WorldLeaks) and Trinity Catholic High School (Beast). — [SOCRadar](https://socradar.io/free-tools/ransomware-intelligence/victims/st-francis-xavier-catholic-school-system-worldleaks-01e840d4); [SOCRadar](https://socradar.io/free-tools/ransomware-intelligence/victims/trinity-catholic-high-school-beast-27a3648e)
- [Dec 2025] Trocaire College (Catholic, Buffalo NY): ransomware affected about 23,436 people, with SSNs exposed. — [ClaimDepot](https://www.claimdepot.com/data-breach/trocaire-college-2026)
- [2025] University of St. Thomas (Houston, Catholic) suffered a large breach with a ransomware claim. — [Comparitech](https://www.comparitech.com/news/ransomware-gang-says-it-hacked-catholic-university-in-houston-tx); [ABC13](https://abc13.com/amp/post/university-st-thomas-releases-little-information-following-massive-data-breach-houston-chronicle/18007188/)
- [Australia] Loyola College (Catholic, Victoria): Interlock posted about 600 GB including passports and financial records. — [Cyber Daily](https://www.cyberdaily.au/security/12574-exclusive-victoria-s-loyola-college-confirms-cyber-incident)
- [Feb 2025] Riverdale Country School (private, NYC): 1,524 affected, RansomHub. [Jun 2025] Christian Brothers Academy: 2,928 affected, Interlock. — [Comparitech roundup](https://www.comparitech.com/news/education-ransomware-roundup-q1-q3-2025-stats-on-attacks-ransoms-and-data-breaches)
- [Sep 2025] Kido nursery chain (UK): see Q2. The attackers reportedly exploited a public-facing application. Kido said the data was hosted on Famly; Famly denied any breach of its platform. — [FireCompass](https://firecompass.com/kido-nursery-chain-ransomware-attack-and-child-doxing/)
- [Closed Dec 5, 2025] LineLeader (ChildcareCRM by CRM Web Solutions, which says it serves more than 9,000 childcare centers): an open Elasticsearch database exposed more than 140K records of parents, leads, and children. Notification status is unknown. — [Cybernews](https://cybernews.com/security/childcare-crm-database-leak-lineleader/); [eSecurity Planet](https://www.esecurityplanet.com/threats/140k-childcare-records-exposed-in-crm-database-leak/); [SC World](https://www.scworld.com/brief/misconfiguration-exposes-over-140k-childcare-center-records)
- [2022, still relevant] EFF found daycare apps dangerously insecure and lacking 2FA. Brightwheel then rolled out 2FA. — [EFF](https://www.eff.org/deeplinks/2022/06/daycare-apps-are-dangerously-insecure)
- [Feb 2025] Procare acknowledged media concern about the security of childcare software. No breach was described. Its app has passed 10M downloads. A "ProCare" ransomware listing (MoneyMessage, Aug 2026) appears to be a different, healthcare entity and is unverified. — [Procare](https://procaresoftware.com/?p=29009); [PR Newswire](https://www.prnewswire.com/news-releases/procare-child-care-mobile-app-reaches-10-million-downloads-302539080.html); [SOCRadar](https://socradar.io/data-breach/procare-moneymessage-2026/)

### Inferences
- Dioceses face an unusual risk: centralized legal, insurance, and abuse-claim data held by outside advisors (BRG). Diocesan vendor due diligence should cover law firms and consultants, not just edtech.
- Parochial schools share diocesan email tenants and SIS contracts, so one weak school account can expose the whole diocese. This is account-takeover hopping on a small scale.
- Childcare data (photos, custody and pickup authorizations, allergies and medical information, safeguarding notes) sits in a handful of SaaS platforms. Misconfiguration and app-level flaws are the main risk, and the center cannot see either. Small centers should ask vendors about MFA for admins and parents, breach notification commitments, and data deletion.

### Gaps
- No incidents found for KinderCare, brightwheel, or Procare in 2023-2026.
- No US Catholic K-12 school ransomware case with confirmed leaked student data was found. The SOCRadar listings are unverified claims.
- Classical-school and youth-program (camps, sports leagues) incidents were not researched within the call budget.

## 4. Child identity theft: how minors' SSNs are used, scale, and the credit-freeze defense

### Takeaway
Children's SSNs are prized for synthetic identity fraud because they have no credit file and no one checks them, so fraud surfaces years later, often at 18. A free federal credit freeze for children under 16 has been available since September 2018 in every state. This is the single most actionable post-breach step for parents.

### Cited Findings
- Most child ID fraud is synthetic identity creation. The SSN is the key element, typically combined with a different date of birth. Because there is no existing file, nothing triggers an alert for years. — [Infosecurity Magazine (Javelin)](https://www.infosecurity-magazine.com/news/little-understood-child-id-theft-reaching-crisis/); [ITRC/Javelin podcast Sep 2025](https://www.idtheftcenter.org/podcast/fraudian-slip-how-does-child-identity-theft-occur/)
- [Javelin 2024 Child & Family Cybersecurity Study] 1 in 43 US children had personal information compromised in a single year. [Jul 2021-Jul 2022] 915,000 children (1 in 80) were targets of ID theft. — [Infosecurity Magazine](https://www.infosecurity-magazine.com/news/little-understood-child-id-theft-reaching-crisis/); [PaymentsJournal](https://www.paymentsjournal.com/?p=495689)
- [Javelin 2018] More than 1 million children were victims in 2017. About 60% of child victims knew the perpetrator (a family member or friend). — [NBC News](https://www.nbcnews.com/business/consumer/more-1-million-children-were-victims-id-theft-last-year-n885351)
- [2021-2024] FTC data show child identity theft reports rose about 40% (secondary citations). — [Bitdefender](https://www.bitdefender.com/en-us/blog/hotforsecurity/child-identity-theft); [LSEG white paper](https://www.lseg.com/content/dam/risk-intelligence/en_us/documents/gated/white-papers/risk-intelligence-child-id-threft.pdf)
- [Effective Sep 21, 2018] The Economic Growth, Regulatory Relief, and Consumer Protection Act gives a free security freeze to "protected consumers," which includes children under 16, at all three bureaus nationwide. A parent must show proof of authority, such as a birth certificate. At 16 the minor can manage the freeze. — [FTC](https://consumer.ftc.gov/consumer-alerts/2019/03/new-protections-available-minors-under-16); [CFPB](https://www.consumerfinance.gov/about-us/blog/new-protections-available-minors-under-16); [FTC 2018](https://ftc.gov/news-events/press-releases/2018/09/starting-today-new-law-allows-consumers-place-free-credit-freezes)
- Contradiction: one vendor blog says only "29 states" allow minor freezes. That reflects pre-2018 state law and is superseded by the federal law above. — [Guard.io](https://guard.io/blog/child-ssn-identity-theft-protection) vs [FTC](https://consumer.ftc.gov/consumer-alerts/2019/03/new-protections-available-minors-under-16)

### Inferences
- Schools and childcare centers often collect SSNs (enrollment, tuition aid, state childcare subsidy forms) without needing them. Not collecting SSNs, or purging them, removes the highest-value item for synthetic fraud.
- Breach notices to families should include child-freeze instructions (Equifax, Experian, TransUnion; IdentityTheft.gov), because standard adult credit monitoring is useless for a child with no file.

### Gaps
- No primary 2025 or 2026 Javelin child-fraud figures were found. Search results referenced 2024 and earlier.
- No data linking specific school breaches (e.g., PowerSchool SSNs) to downstream fraud was found.

## 5. Under-watched vectors: SIS admin accounts, Google Workspace tenants, Chromebooks/MDM, cameras, payment portals, AI voice cloning

### Takeaway
The best-documented under-watched vector is the trusted-account path. A single vendor or contractor credential without MFA (PowerSchool, Sep 2024) or a single staff or student Google/Microsoft account becomes a launchpad. Google Classroom and Workspace abuse is widespread. Evidence for Chromebook/MDM or camera compromises in 2024-2026 is thin. AI voice impersonation at schools is documented as harassment (Pikesville), not yet as payment fraud.

### Cited Findings
- [Sep 2024] The PowerSchool breach used a single contractor's credentials to reach the customer-support portal (PowerSource). That one credential led to data on tens of millions of students. — [CyberScoop](https://cyberscoop.com/powerschool-hacker-matthew-lane-sentenced/); [The 74](https://www.the74million.org/article/powerschool-hacker-thankful-i-got-caught-sentenced-to-4-years-in-prison/)
- [2026] Moody's ranks education among the top sectors hit through third-party services (PowerSchool, Instructure Canvas). — [K-12 Dive](https://www.k12dive.com/news/cybersecurity-incidents-hit-over-50-of-schools-and-districts-in-past-year/872783/)
- K12 SIX published (first to members, then publicly) a checklist for mitigating compromised K-12 Google Workspace / Microsoft 365 accounts. A school IT consortium says to follow the full checklist even when MFA is enabled, because session tokens and app grants persist. — [K12 SIX](https://k12six.org/news/k12-six-releases-guidance-on-mitigating-compromised-accounts); [WSIPC](https://www.wsipc.org/news/new-cyberattack-pattern-and-resource)
- [Aug 6-12, 2025] Check Point: 115,000 phishing emails abused Google Classroom invitations to target 13,500 organizations. — [Check Point](https://blog.checkpoint.com/email-security/phishing-in-the-classroom-115000-emails-exploit-google-classroom-to-target-13500-organizations/)
- A years-old, still-active student Google Workspace mailbox was used to phish a public school district, with links hosted on Google's own servers to evade filters. — [IronScales](https://ironscales.com/threat-intelligence/student-google-account-apps-script-credential-phishing)
- Spamhaus reportedly identified more than 450 compromised education domains using Google Workspace. This is secondary and vendor-reported. — [GAT Labs](https://gatlabs.com/education/?p=16101)
- [Jun 2026] AI-generated phishing is gaining inside access to K-12 data. — [EdTech Magazine](https://edtechmagazine.com/k12/article/2026/06/ai-phishing-gains-inside-access-vulnerable-k-12-data?amp)
- [2024 incident; Apr 2025 sentence] Pikesville High (MD): an athletic director used AI voice cloning to fabricate a racist recording of the principal, who was investigating him over mishandled school funds. He received 4 months. The principal's career was upended. — [CBS Baltimore](https://www.cbsnews.com/baltimore/news/maryland-pikesville-principal-ai-voice-impersonation-trial); [Washington Times](https://www.washingtontimes.com/news/2025/apr/28/ex-athletic-director-takes-plea-making-bigoted-ai-recording-baltimore/)
- [Since 2023] WIRED: nearly 90 schools and more than 600 students worldwide affected by AI-generated nude deepfakes made from ordinary student photos. At least half of US states legislated on AI-fabricated images in 2025. — [Stacker/KEYT 2026](https://keyt.com/stacker-k-12/2026/08/03/school-cameras-may-protect-students-but-who-protects-the-footage/)
- [2021] Verkada camera breach: a leaked super-admin credential exposed live feeds, including schools (Sandy Hook Elementary). 2026 coverage centers on governance of camera footage (export logs). — [Fortune](https://fortune.com/2021/03/11/security-camera-hack-verkada-surveillance/); [Stacker 2026](https://stacker.com/stories/k-12/school-cameras-may-protect-students-who-protects-footage)

### Inferences
- Publicly posted student photos (school websites, social media, yearbooks) are a raw material for deepfake abuse. Kido shows that photos are also extortion leverage. Photo-publication policies are now a security control.
- AI voice cloning of principals and bookkeepers for payment fraud is plausible but undocumented in K-12 in these sources. The defense is the same as for BEC: call back on a known number and use dual approval.
- Stale accounts (graduated students, departed staff, contractors) and long-lived vendor support accounts are the clearest hidden exposure for a small school.

### Gaps
- No 2024-2026 public cases found of Chromebook/MDM console abuse, school IP camera compromise, or tuition/payment portal (FACTS, Blackbaud tuition, etc.) credential stuffing. These may be under-reported rather than absent.
- No documented school case of AI-voice payment fraud was found.

## 6. Simple controls that would have prevented the most common incidents

### Takeaway
Nearly every incident above maps to a handful of low-cost controls:
- phishing-resistant MFA on every admin, finance, and vendor account
- out-of-band verification for any bank-detail change
- removing stale accounts
- keeping sensitive records out of email and shared drives, and not collecting SSNs
- vendor MFA and deletion terms
- a pre-written family communication with child credit-freeze steps

### Cited Findings
- PowerSchool: one contractor credential reached the support portal. MFA on vendor support access and least privilege would have blocked or contained it. — [CyberScoop](https://cyberscoop.com/powerschool-hacker-matthew-lane-sentenced/); [K-12 Dive lessons](https://www.k12dive.com/news/powerschool-hacker-sentencing-lessons-learned-data-breach/803053/)
- Payroll and vendor fraud: Ohio auditors found districts lacked verification policies until after the losses. Sudbury attackers intercepted MFA, so callback verification of direct-deposit and vendor bank changes is the decisive control. — [Ohio Auditor](https://ohioauditor.gov/news/PressReleases/Details/7799); [Sudbury Weekly](https://sudburyweekly.com/sps-hit-by-payroll-cyberattack-in-2025-over-12000-diverted/)
- CIS 2026 recommendations: expand MFA, monitor exposed credentials, review privileged accounts, run tabletop exercises. — [Help Net Security](https://www.helpnetsecurity.com/2026/10/29/cis-k-12-cybersecurity/); [CIS on MFA in K-12](https://www.cisecurity.org/about-us/media/media-mention/multifactor-authentication-keeps-cybercriminals-out-of-k-12-networks)
- Compromised account response: follow the full K12 SIX checklist even with MFA (revoke sessions, check forwarding rules and OAuth grants). — [WSIPC](https://www.wsipc.org/news/new-cyberattack-pattern-and-resource); [K12 SIX](https://k12six.org/news/k12-six-releases-guidance-on-mitigating-compromised-accounts)
- Phishing was the entry point for 22% of lower-ed ransomware in 2025. — [Sophos](https://www.sophos.com/en-us/blog/the-state-of-ransomware-in-education-2025)
- Paying does not guarantee deletion (PowerSchool in May 2025; Kido's deletion claim is unverified), so offline backups plus a parent communication plan beat ransom payment. — [The 74](https://www.the74million.org/article/powerschool-paid-off-hackers-after-huge-breach-now-theyre-extorting-districts/)
- Child credit freeze (free, under 16, since 2018). — [FTC](https://consumer.ftc.gov/consumer-alerts/2019/03/new-protections-available-minors-under-16)
- LineLeader and EFF: an open database and missing 2FA in childcare SaaS. Asking vendors about 2FA, security testing, and notification is the center-level control. — [Cybernews](https://cybernews.com/security/childcare-crm-database-leak-lineleader/); [EFF](https://www.eff.org/deeplinks/2022/06/daycare-apps-are-dangerously-insecure)

### Inferences
Suggested top 10 for a no-staff school or center, ranked by incidents prevented:
1. MFA on email, the SIS, and finance, with phishing-resistant keys or passkeys for admin and finance staff.
2. A written rule: no bank, payroll, or vendor payment change without a callback to a known number and a second approver.
3. A quarterly purge of former staff, student, and contractor accounts, plus review of vendor support access.
4. Disable external auto-forwarding and third-party app grants in Google or Microsoft by default.
5. Move counseling, IEP, safeguarding, and custody files out of email and shared drives into restricted storage, and keep only what is needed.
6. Stop collecting SSNs, or purge them.
7. Offline or immutable backups of critical systems.
8. Vendor questions: MFA for admins and parents, breach notification time, data deletion at contract end.
9. A pre-drafted parent letter: do not respond to extortion, report it, plus child-freeze steps.
10. Minimize public student photos.

### Gaps
- No controlled study quantifying which control prevents what share of K-12 incidents was found. The ranking above is inference from case patterns.
- Insurance-claim data (e.g., Coalition or At-Bay education breakdowns) was not retrieved.
