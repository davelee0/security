# Endpoint, IoT and Network Security for Tiny Child-Serving Organizations

Research date: 2026-11-23. Scope: parish and classical schools, childcare centers, youth programs, and small NYC providers. The lens is a hands-on practitioner walking the building. This is defensive only. Nothing here describes how to find or access specific exposed devices.

Method note: research ran on web search result summaries (about 16 queries). No pages were fetched in full, so treat exact figures as "as reported by the search-indexed page" and check them before quoting. Earlier notes in `Kids data defense research tree/` (threat_landscape.md, child_safeguarding.md, economics_insurance_funding.md) already cover NurseryCam 2021, Kido 2025, the MDBR loss and the Microsoft nonprofit change. This file goes deeper on the device and network layer and does not repeat their sources except where needed.

Overall framing: the public record of device and IoT compromise in *small* child-serving buildings is thin. Incidents are documented mainly for (a) camera *vendors* and cloud platforms (NurseryCam, Verkada, Ring), (b) school-safety *SaaS* misconfigurations (Raptor), and (c) internet-exposed camera and access-control hardware in general (Dahua, Hikvision, Nice Linear). The realistic building-level risks are inferred from those vendor and hardware cases plus device lifecycle facts (Windows 10 end of support, Chromebook AUE, copier drives). They are not drawn from case studies of individual daycares.

---

## 1. Cameras and video: parent livestreams, NVR/DVR and IP cameras, Verkada, baby monitors

### Takeaway
Every documented child-relevant camera incident traces to the vendor or cloud account layer: hardcoded or exposed credentials (NurseryCam), a leaked super-admin credential (Verkada), staff over-access and no MFA (Ring). On the device side, mass compromise of internet-exposed cameras through default or weak passwords and unpatched firmware keeps happening (Dahua CameraSwarm, Hikvision). The cheapest effective controls: no port-forwarding of cameras or NVRs, MFA on the cloud/app account, unique admin passwords, revoking parent access when families leave, and vendor due diligence. I found no confirmed 2024-2026 US daycare livestream breach.

### Cited Findings
**Parent livestream services**
- NurseryCam (UK, Feb 2021): the service was used by about 40 UK daycares. Account data for about 12,000 users was taken, and the company shut the service down. Researcher Andrew Tierney had warned for years that its security was weak, including credentials exposed in page code — [The Register](https://www.theregister.com/2021/02/22/nurserycam_breach/); [Threatpost](https://threatpost.com/daycare-webcam-exposes-12000/164203/); [UpGuard](https://www.upguard.com/news/nurserycam-breach); [Security Affairs](https://securityaffairs.com/114919/data-breach/nurserycam-security-breach.html)
- Exposed data reportedly included usernames, hashed passwords, names and email addresses — [UpGuard](https://www.upguard.com/news/nurserycam-breach)
- No breach involving WatchMeGrow or Kinder Cam specifically surfaced in search — [search results incl. WatchMeGrow blog](https://watchmegrow.com/blog/can-child-care-center-cameras-be-hacked)
- WatchMeGrow, a vendor and therefore self-interested, says some camera providers use third-party software built for businesses like gas stations. It also says several cameras at Canadian childcare facilities were compromised, with video appearing on sites that stream unsecured webcams. It stresses revoking parent passwords when families leave — [WatchMeGrow blog](https://watchmegrow.com/blog/can-child-care-center-cameras-be-hacked); [WatchMeGrow questions to ask](https://watchmegrow.com/blog/know-questions-ask-prevent-unsecured-streaming-video-your-school)
- Montreal: parents raised alarms after a daycare lobby appeared on a public webcam-aggregator site (date unclear in results). A separate Montreal case involved children allegedly filmed by a neighbour's surveillance camera — [Global News](https://globalnews.ca/video/2931496/webcam-app-has-parents-worried/amp); [CTV Montreal](https://montreal.ctvnews.ca/kids-at-montreal-daycare-allegedly-filmed-on-neighbour-s-surveillance-camera-1.6591961)
- EdSurge (Mar 2023): as childcare programs adopt tech tools, privacy and security questions are rising — [EdSurge](https://www.edsurge.com/news/2023-03-20-as-child-care-programs-adopt-tech-tools-new-questions-arise-about-privacy-and-security)

**Verkada (2021 breach, 2024 FTC/DOJ settlement)**
- In 2021, attackers using a leaked super-admin credential reached Verkada's Command platform. The FTC says the platform exposed about 150,000 live camera feeds. Prior notes record that schools, including Sandy Hook Elementary, were among the exposed customers — [BleepingComputer](https://www.bleepingcomputer.com/news/security/verkada-to-pay-295m-for-security-failures-leading-to-breaches/); [Fortune 2021](https://fortune.com/2021/03/11/security-camera-hack-verkada-surveillance-cameras-tesla-hospitals-jails/)
- Conflicting scale: Verkada says image data from 97 customers (<2% of its base) was viewed. The 150,000 figure is feeds *exposed*, not confirmed *viewed* — [BleepingComputer](https://www.bleepingcomputer.com/news/security/verkada-to-pay-295m-for-security-failures-leading-to-breaches/)
- Aug 2024: Verkada agreed to a $2.95M civil penalty, which the FTC called its largest CAN-SPAM penalty. The FTC also alleged Verkada misrepresented its data security and its HIPAA compliance. The order requires a comprehensive infosec program, regular third-party assessments, and reporting of incidents to the FTC for 20 years. Verkada neither admitted nor denied the allegations — [DOJ press release 24-1092](https://www.justice.gov/opa/pr/295m-penalty-and-permanent-injunction-resolves-lawsuit-against-verkada-inc-alleged-unlawful); [FTC stipulated order PDF](https://www.ftc.gov/system/files/ftc_gov/pdf/2123068verkadajtmtnstipulatedorder.pdf); [SC World](https://scworld.com/news/ftc-calls-out-security-camera-vendor-verkada-over-data-exposure)

**Consumer cameras and baby monitors (relevant where small centers buy consumer gear)**
- FTC v. Ring (2023): $5.8M. The FTC alleged employees and contractors had broad, unrestricted access to customer videos, and that Ring failed to adopt MFA despite credential-stuffing attacks in 2017-18. The FTC says Ring adopted MFA in 2019; Ring says mandatory 2FA came in Feb 2020. The order requires MFA for employee and customer accounts and a 20-year assessed program. Refunds of more than $5.6M went out in Apr 2024 — [TechSpot](https://www.techspot.com/news/98910-amazon-agrees-58-million-settlement-ftc-over-ring.html); [Ring response](https://blog.ring.com/about-ring/rings-response-to-our-recent-settlement-with-the-ftc/); [Malwarebytes Apr 2024](https://www.malwarebytes.com/blog/news/2024/04/ring-agrees-to-pay-5-6-million-after-cameras-were-used-to-spy-on-customers); [BleepingComputer](https://www.bleepingcomputer.com/news/security/ring-customers-get-56-million-in-privacy-breach-settlement/)
- Mississippi/Tennessee family case (Dec 2019): a hacker accessed a Ring camera in an 8-year-old's room and taunted her. The family had not enabled 2FA — [WJLA](https://wjla.com/news/nation-world/tennessee-family-says-hackers-accessed-ring-camera-in-8-year-old-girls-room)

**NVR/DVR and IP camera exposure research (general, not school-specific)**
- "CameraSwarm": more than 14,500 Dahua cameras were compromised in a 35-day brute-force campaign, mostly in Ukraine and Russia — [BleepingComputer](https://bleepingcomputer.com/news/security/hackers-compromise-14-500-dahua-web-cameras-in-35-day-campaign); [SecPod](https://www.secpod.com/learn/security-research/operation-camera-swarm-inside-the-toolkit-behind-14-530-compromised-dahua-cameras)
- FBI IC3 advisory (Dec 2024): Hikvision had not mitigated a vulnerability across all affected devices as of 13 Dec 2024 — [IC3 CSA 241216](https://ic3.gov/CSA/2024/241216.pdf)
- Hunt.io research: open camera management ports can expose the camera and also act as a breach point into the customer's network — [SecurityInfoWatch](https://www.securityinfowatch.com/cybersecurity/news/55400371/huntio-research-highlights-remote-access-risks-for-ip-camera-deployments)
- SANS ISC guest diary (Apr 2026): compromised DVRs are being found in the wild — [SANS ISC](https://isc.sans.edu/diary/32886)
- 2026 advisory coverage of Iranian operations against cameras: patches exist for all five CVEs, but many devices remain unpatched and internet-exposed — [HivePro TA2026076](https://hivepro.com/wp-content/uploads/2026/03/TA2026076.pdf)
- Censys publishes defender-oriented research on internet-exposed cameras — [Censys](https://censys.com/blog/blog-finding-internet-cameras-before-adversaries-do/)

### Inferences
- Common building pattern: a cheap DVR/NVR installed by an AV or alarm contractor, port-forwarded on the router so the director can watch from a phone, with the installer's default password. Each piece matches the documented exposure patterns above, though I found no daycare-specific survey quantifying it.
- Cheapest controls, in order: (1) remove any router port-forwards and UPnP for cameras or NVRs, and use the vendor's cloud relay with MFA or a VPN; (2) change default and installer passwords, and keep the admin credential somewhere other than the installer's head; (3) put cameras on a separate VLAN or SSID with no internet access, or only vendor cloud access; (4) apply firmware updates or plan replacement; (5) for parent livestreams, use per-family accounts, revocation at disenrollment, MFA, viewing limited to classroom hours, and no restroom or diapering areas in view.
- Vendor due-diligence questions for livestream or camera vendors: Do you enforce MFA? Can staff view feeds, and are views logged (the Ring lesson)? Who holds super-admin, and how is it protected (the Verkada lesson)? Is any credential embedded in the client (the NurseryCam lesson)? What is your breach history and FTC/ICO status?
- Banned-vendor angle: FCC Covered List restrictions on Hikvision and Dahua equipment are a policy issue for new purchases. I did not research whether small private schools are affected (see Gaps).

### Gaps
- No public 2024-2026 incident found for WatchMeGrow, Kinder Cam, or other US daycare livestream services. This may reflect under-reporting.
- No school- or daycare-specific camera exposure study was found. All exposure research is sector-agnostic.
- Baby monitors used *inside* daycare rooms (Wi-Fi monitors, Nanit, Owlet-type devices): no incident or guidance found.
- Applicability of FCC Covered List and NDAA Section 889 to small private schools buying Hikvision or Dahua was not researched.

---

## 2. Building systems: door access control, visitor management, intercoms, school safety apps

### Takeaway
The best-documented school incident in this category is the Raptor Technologies cloud-storage exposure (Dec 2023 to Jan 2024): about 4M records, including emergency and lockdown plans and some student data. It came from SaaS misconfiguration, not on-site hardware. Separately, CISA has repeatedly flagged door-controller hardware (Nice Linear eMerge E3) for hardcoded or default credentials and exploited flaws. For small buildings, the controls are installer-credential hygiene, keeping controllers off the internet, and vendor due diligence on safety SaaS.

### Cited Findings
- Raptor Technologies: researcher Jeremiah Fowler found an exposed cloud database and reported it in Dec 2023. Raptor restricted access the next day. Coverage put the exposure at about 4M records — [vpnMentor](https://vpnmentor.com/news/report-raptortech-breach); [K-12 Dive](https://www.k12dive.com/news/raptor-technologies-school-safety-data-leak/704790/); [EdWeek Jan 2024](https://edweek.org/technology/a-massive-data-leak-exposed-school-lockdown-plans-what-districts-need-to-know/2024/01)
- The exposed material reportedly included emergency response plans, campus evacuation routes and, in one district, student names and ID numbers — [EdWeek](https://edweek.org/technology/a-massive-data-leak-exposed-school-lockdown-plans-what-districts-need-to-know/2024/01); [SC World](https://scworld.com/brief/unsecured-raptor-technologies-web-buckets-expose-sensitive-us-school-records); [GovTech](https://insider.govtech.com/texas/news/houston-based-school-security-company-says-leak-contained)
- Sources conflict on visitor data. Raptor's customer notice said affected containers held files from Visitor Management and Emergency Management features but no Visitor Management driver's-license data. Elmira City Schools said visitor management data was not included. Arlington Public Schools said some of its data was externally exposed — [Coppell ISD notice](https://www.coppellisd.com/article/1409028); [Elmira notice](https://elmiracityschools.com/news/what_s_new/raptor_data_incident); [WTOP](https://wtop.com/education/2024/01/how-a-school-tech-software-companys-data-breach-could-impact-dc-area-districts)
- Raptor said there was no indication of third-party access beyond the researcher and its own staff. The duration of exposure was unconfirmed — [Elmira notice](https://elmiracityschools.com/news/what_s_new/raptor_data_incident); [TechRadar](https://techradar.com/pro/security/school-software-breach-reveals-private-data-on-millions-of-users)
- The leak revived scrutiny of the ed-tech Student Privacy Pledge, which Raptor had signed — [The 74](https://www.the74million.org/article/leaked-active-school-shooter-plans-revive-scrutiny-of-ed-tech-privacy-pledge-2/)
- Earlier, Rapid7 (Apr 2023) disclosed client-side security-control flaws in Raptor's Volunteer Management product, since fixed — [Rapid7](https://www.rapid7.com/blog/post/2023/04/11/raptor-technologies-volunteer-management-client-side-security-controls-fixed/)
- CISA ICSA-24-065-01 (Mar 2024), Nice Linear eMerge E3-Series door access controllers: CVSS 10.0, public exploits, SSH enabled with hardcoded root credentials. Mitigation: change default credentials and the default IP — [CISA](https://cisa.gov/news-events/ics-advisories/icsa-24-065-01)
- CISA ICSA-25-114-04 (Apr 2025): further eMerge E3 issues (CVSS v4 9.3). Recommends changing defaults and using a VPN for remote access — [CISA](https://www.cisa.gov/news-events/ics-advisories/icsa-25-114-04)
- CVE-2019-7256 (eMerge OS command injection) has been reported as exploited in the wild and went years without a patch — [SecurityWeek](https://www.securityweek.com/exploited-building-access-system-vulnerability-patched-years-after-disclosure/); [Fortinet outbreak alert](https://filestore.fortinet.com/fortiguard/outbreak_alert/nice_linear_emerge_command_injection_vulnerability/report.pdf)
- CVE-2022-31269 (eMerge): admin credentials stored in a file could let an attacker open a building's doors — [NVD](https://nvd.nist.gov/vuln/detail/CVE-2022-31269)
- Nice said in May 2023 that some Linear telephone-entry (intercom) products had been compromised. No CVEs were named — [SecurityWeek](https://www.securityweek.com/exploited-building-access-system-vulnerability-patched-years-after-disclosure/)

### Inferences
- In tiny buildings, the door system is often a keypad or fob controller with a web UI or cloud app installed by a locksmith or alarm company. Its admin password, the codes shared across staff and former staff, and any remote-access arrangement are the practical risks. A volunteer can inventory these and confirm that departing-staff codes are revoked.
- Emergency and lockdown plans and floor plans are sensitive data. They should be shared with least privilege, and it should be known which SaaS holds them (the Raptor lesson).
- Visitor-management kiosks that scan IDs create a store of adult PII. Ask the vendor about retention and where the data lives.

### Gaps
- No documented incidents found involving school-safety or panic-button apps (e.g., CENTEGIX, Rave/Motorola, SchoolGuard), or cloud intercoms (Ring Intercom, ButterflyMX, Verkada intercom) at schools.
- No data on how many small schools or daycares have internet-exposed access controllers.

---

## 3. Devices: Windows 10 end of support and ESU, Chromebook AUE, shared PCs, personal devices, copiers

### Takeaway
Windows 10 support ended 14 Oct 2025. Education customers can buy ESU for $1, $2 and $4 per device for years 1-3, against $61, $122 and $244 commercial. That makes ESU the cheapest stopgap for schools that qualify for education licensing. Chromebooks now get 10 years of updates from platform release, not purchase, but used or refurbished units can arrive with years already gone. Reports say ChromeOS updates end in 2034 as Google transitions to "Googlebook OS" (this needs confirming). Copier hard drives retain scans of student and health records, and FTC guidance on wiping and encrypting them still applies.

### Cited Findings
- Windows 10 ESU for education (K-12 and higher ed): $1 in year 1, $2 in year 2, $4 in year 3 per device. Commercial: $61, $122, $244 — [Microsoft Education Blog](https://microsoft.com/en-us/education/blog/?p=5226); [Computerworld](https://www.computerworld.com/article/2081793/heres-how-much-microsoft-will-charge-for-win10-security-updates-once-support-ends.html); [The Register Apr 2024](https://www.theregister.com/2024/04/03/windows_10_extended_support/)
- Non-US education pricing is converted. University of Toronto lists Year 1 $1.90, Year 2 $3.70, Year 3 $7.40, presumably CAD — [U of T EASI](https://easi.its.utoronto.ca/?p=17085)
- UK schools also get discounted ESU — [Schools Week](https://schoolsweek.co.uk/schools-will-get-discounted-updates-to-keep-windows-10-running)
- Free consumer ESU (tied to Microsoft account, backup or rewards) applies only to consumers, not organizations — [Computerworld](https://www.computerworld.com/article/4012425/microsoft-offers-free-windows-10-security-updates-but-only-for-consumers.html)
- Chromebooks: 10 years of automatic updates for platforms released from 2021 onward. Admins can opt older devices in if they haven't reached end of support. The window counts from the *platform release date* — [Google blog (2023)](https://blog.google/outreach-initiatives/education/automatic-update-extension-chromebook); [Google support: old Chromebooks](https://support.google.com/chromebook/answer/7052113?hl=en); [PCWorld](https://www.pcworld.com/article/2067677/google-extends-chromebook-support-to-ten-years-retroactively-too.html)
- Past AUE, devices keep working but get no security updates. Schools often buy units two or more years into their life — [PIRG FAQ](https://pirg.org/resources/frequently-asked-questions-google-announced-10-years-of-software-updates-for-chromebooks/); [The Register Jan 2025](https://www.theregister.com/2025/01/06/chromebook_end_of_life/)
- 2026 reports say ChromeOS updates end in mid-2034 as "Googlebook OS" arrives. Devices whose 10-year policy runs past 2034 would be eligible to move. This comes from secondary sources and conflicts on details — [The Next Web](https://thenextweb.com/news/chromeos-updates-end-2034-googlebook-os); [tech-insider](https://tech-insider.org/chromeos-support-ends-2034-not-2036-2026/); [BetaNews](https://betanews.com/article/google-is-ending-support-for-chromeos-earlier-than-previously-announced/)
- Copiers and MFPs: the drive stores data about documents copied, printed, scanned, faxed or emailed. Deleting or reformatting doesn't remove the data. Encryption and periodic overwrite are recommended. Retain the drive or require overwrite at lease end. The guidance dates from 2010 and is still the latest federal copier guidance found — [FTC Digital Copier Data Security guide](https://www.ftc.gov/tips-advice/business-center/guidance/digital-copier-data-security-guide-businesses); [FTC 2010 press release](https://www.ftc.gov/news-events/news/press-releases/2010/12/ftc-offers-businesses-tips-securing-data-digital-copiers)
- Vendors sell add-on kits that encrypt or auto-erase the copier cache — [U. Michigan Safe Computing](https://safecomputing.umich.edu/protect-the-u/protect-your-unit/copier-multi-function-data-security); [TechSoup](https://blog.techsoup.org/posts/your-copiers-are-storing-confidential-information-what-you-can-do-about-it)
- Stolen laptops: historic cases show unencrypted student data on staff laptops, sometimes copied for personal use (e.g., a thesis). A UK case had an encrypted laptop holding unencrypted files. Most cases found predate 2024 — [CSO Online](https://www.csoonline.com/article/517164/data-protection-colo-college-warns-93-000-after-laptop-theft.html); [ITPro](https://itpro.com/636553/education-bodies-caught-in-data-breach-gaffes); [DataBreaches.net 2017 Niskayuna](https://databreaches.net/2017/05/24/ny-niskayuna-school-laptop-stolen-945-students-personal-information-on-device)

### Inferences
- Windows 10 decision tree for a tiny school: (a) if the device can run Windows 11, upgrade it; (b) if not, and the org qualifies for Microsoft education licensing (many parish schools do; childcare centers often do not), buy ESU at $1 per device as a bridge to Oct 2028 at most; (c) otherwise, replace the device or convert it to ChromeOS Flex or Linux for single-purpose use. ChromeOS Flex is a free Google option for converting old PCs; I did not verify current Flex terms in this session. As of Nov 2026, ESU year 1 is ending and year 2 ($2) begins.
- Childcare centers using non-education Microsoft licensing would pay the $61 commercial ESU rate, which pushes them toward replacement. This is an equity gap worth flagging.
- Chromebook buying rule: check the published AUE date per model before buying, and avoid cheap refurbished lots near AUE. An *unmanaged* Chromebook (no Chrome Education Upgrade) cannot be force-enrolled, wiped remotely, or restricted to school accounts. A lost one is then a privacy incident rather than a non-event. (Inference; Chrome Education Upgrade pricing was not verified this session.)
- Full-disk encryption (BitLocker or FileVault; ChromeOS encrypts by default) is the control that turns a stolen laptop from a reportable breach into a property loss under most state breach laws' encryption safe harbors. NY SHIELD Act safe-harbor specifics were not verified here.
- Staff personal devices: the practical control is keeping student data in cloud apps (Google Workspace or M365) behind MFA rather than in downloaded files, plus a basic acceptable-use agreement.
- Copiers are a lease-return blind spot. The lease contract should require drive overwrite or retention, with a certificate.

### Gaps
- No 2024-2026 case found of a stolen laptop at a small school or daycare causing a notified breach. State AG breach portals were not searched.
- Chrome Education Upgrade per-device price and ChromeOS Flex support status in 2026 were not verified.
- No data on how many small private schools or daycares still ran Windows 10 after Oct 2025.

---

## 4. Network: consumer routers, defaults, guest Wi-Fi, protective DNS, MDBR loss, CIPA vs security filtering

### Takeaway
MS-ISAC moved to fee-based membership on 23 June 2025, and free MDBR (protective DNS) ended around 30 Sep / 1 Oct 2025 when CISA's cooperative agreement with CIS ended. Free replacements exist but are uneven. Cloudflare's Project Cybersafe Schools gives free DNS filtering and email security, but only to US public K-12 districts with up to 2,500 students, which excludes private and parish schools and daycares. CISA's own Protective DNS was in a pilot that included K-12 and is not open enrollment. Cisco Umbrella for K-12 is paid. For tiny private orgs, free public protective resolvers (Quad9, Cloudflare 1.1.1.1 for Families) set on the router are the realistic baseline. Note that CIPA content filtering is an e-Rate compliance requirement, distinct from malware and phishing (security) filtering.

### Cited Findings
- MS-ISAC introduced fee-based membership as of 23 June 2025, and references to no-cost MS-ISAC services no longer apply — [CIS MDBR page](https://www.cisecurity.org/ms-isac/services/mdbr); [CIS MDBR FAQ](https://www.cisecurity.org/ms-isac/services/mdbr/mdbr-faq)
- CISA's cooperative agreement with CIS ended 30 Sep 2025, and free MDBR ended about 1 Oct. Vendor sources differ by a day — [Total Uptime (vendor)](https://totaluptime.com/managed-services/protective-dns-service/mdbr-replacement/); prior notes: [Armorpoint](https://armorpoint.com/2025/10/24/what-the-ms-isac-transition-means-for-k-12-and-public-education/)
- The White House ONCD K-12 page (2024) said some states and regional Educational Service Agencies offer PDNS to schools, and some companies offer PDNS free to certain K-12 schools — [ONCD archive](https://bidenwhitehouse.archives.gov/oncd/protecting-k-12-schools)
- CISA Protective DNS: originally federal-only. CISA piloted it with critical-infrastructure entities in healthcare, water and K-12. The Aug 2024 fact sheet welcomes full FCEB participation via CyberSharedServices@cisa.dhs.gov — [CISA "Piloting New Ground"](https://www.cisa.gov/news-events/news/piloting-new-ground-expanding-scalable-cybersecurity-services-protect-broader-critical); [CISA PDNS Fact Sheet Aug 2024](https://cisa.gov/sites/default/files/2024-08/Protective%20DNS%20Fact%20Sheet%20-%20August%202024.pdf)
- FCC's cybersecurity resource list for schools and libraries includes CISA PDNS among free and low-cost resources — [FCC PDF](https://fcc.gov/sites/default/files/Cybersecurity-Resource-Recommendations.pdf)
- Cloudflare Project Cybersafe Schools: free Email Security and Gateway DNS filtering for US K-12 *public school districts* with up to 2,500 students. It can be used for CIPA compliance. Others can email k-12@cloudflare.com — [Cloudflare docs](https://developers.cloudflare.com/fundamentals/security/cybersafe); [Cloudflare blog](https://blog.cloudflare.com/project-cybersafe-schools); [Cloudflare CIPA overview](https://developers.cloudflare.com/learning-paths/cybersafe/concepts/cipa-overview/)
- UK comparison: NCSC offers free "PDNS for Schools" and has expanded eligibility — [NCSC intro](https://www.ncsc.gov.uk/blog-post/introducing-pdns-for-schools); [NCSC expansion](https://www.ncsc.gov.uk/blog-post/pdns-for-schools-provide-cyber-resilience-for-more-institutions)
- Cisco Umbrella for K-12 is sold as a CIPA-compliance product and has moved to "Secure Access - DNS Defense" education packages (contact sales). Only a 14-day trial is free. MSP licensing requires one user license per 10 students — [Cisco Umbrella K-12](https://umbrella.cisco.com/use-cases/k-12); [Cisco MSLA terms](https://www.cisco.com/c/dam/en_us/about/doing_business/legal/msla/MSLA-and-Secure-MSP-Center-Product-Terms-Umbrella-SIG-and-DNS.pdf); [Umbrella trial](https://umbrella.cisco.com/free-trial-quick-start-guide)
- Academic study (Oct 2025) questions consistency across protective DNS providers ("Wild West") — [arXiv 2510.25352](https://arxiv.org/html/2510.25352)

### Inferences
- Practitioner baseline for a tiny building: (1) replace ISP-default or end-of-life consumer routers, or at least change admin credentials, disable WPS, UPnP and remote admin, and update firmware; (2) run three logical networks: staff/admin, guest/parent, and IoT (cameras, door, smart TVs, thermostats), with guest isolation turned on; (3) point the router's DHCP DNS at a protective resolver; (4) where CIPA applies (e-Rate recipients, including Catholic schools taking e-Rate), the content filter must also be CIPA-compliant, and a protective resolver alone may not satisfy that.
- Free resolver options (from practitioner knowledge, not verified by search this session): Quad9 (9.9.9.9, a nonprofit, blocks malicious domains) and Cloudflare 1.1.1.1 for Families (1.1.1.2 blocks malware; 1.1.1.3 blocks malware and adult content). These are free and need no account, but provide no reporting or per-device policy.
- Eligibility gap: free US K-12 programs (Cloudflare Cybersafe, state PDNS, former MDBR) target *public* districts and SLTT entities. Private parish schools, daycares and youth programs largely fall outside them. This is a concrete gap a volunteer project can fill by documenting the free public-resolver route.
- Many tiny orgs' "network" is an ISP gateway plus a mesh kit bought at retail, with one Wi-Fi password shared with parents. Separating guest Wi-Fi is often a single checkbox and is the highest-value 10-minute fix.

### Gaps
- Quad9 and Cloudflare 1.1.1.1 for Families details were not confirmed by search in this session. Cite their official pages before publishing.
- No current data on CIS's paid "MDBR+" pricing or whether private schools qualify.
- No research found on consumer-router default-credential prevalence in schools or daycares. Router "secure by design" rules (e.g., the US Cyber Trust Mark, the UK PSTI Act banning default passwords from Apr 2024) were not researched here.
- Whether CISA PDNS opened beyond the pilot by late 2026 is unknown.

---

## 5. Free or cheap endpoint protection and backups for nonprofits and schools (2026)

### Takeaway
Microsoft's free Business Premium grant (10 seats) ended for renewals on or after 1 July 2025. Nonprofits now get up to 300 free Business Basic seats, plus discounts of up to 75% on Business Premium (which includes Defender for Business and Intune). Nonprofit pricing on the Defender and Purview add-on suites was promised for Jan 2026. The ACSC's small-business cloud guides assume Business Premium. Built-in Microsoft Defender Antivirus on Windows 10 and 11 remains the zero-cost floor, but it depends on the OS being patched (see the ESU section).

### Cited Findings
- Microsoft announced in May 2025 that the Business Premium (10 free licenses) and Office 365 E1 grants would be discontinued at renewals from 1 July 2025 — [Microsoft Partner asset](https://partner.microsoft.com/asset/collection/microsoft-365-business-premium-and-office-365-e1-grant-discontinuation); [Tech Community thread](https://techcommunity.microsoft.com/discussions/nonprofitpartners/microsoft-365-business-premium-grant-is-being-discontinued/4413944); [Yeo & Yeo](https://www.yeoandyeo.com/resource/nonprofits-what-you-need-to-know-about-microsoft-ending-free-business-premium)
- Replacement: up to 300 free Business Basic licenses, and up to 75% off Business Premium and other offers — [Microsoft Partner asset](https://partner.microsoft.com/asset/collection/microsoft-365-business-premium-and-office-365-e1-grant-discontinuation); [Microsoft Learn nonprofit updates](https://learn.microsoft.com/en-us/industry/nonprofit/microsoft-for-nonprofits/updates)
- Microsoft staff said nonprofit pricing for the Defender and Purview Security add-ons for Business Premium would be available Jan 2026 — [Tech Community](https://techcommunity.microsoft.com/discussions/NonProfitPartners/nonprofit-pricing-for-the-defender-and-purview-suites-for-business-premium/4475762)
- Prior note: for a 15-person parish school, Business Premium now costs about $1,000 a year — [economics_insurance_funding.md, prior research](../Kids%20data%20defense%20research%20tree/economics_insurance_funding.md)
- ACSC Small Business Cloud Security Guides (Essential Eight-aligned, Intune-based) require Microsoft 365 Business Premium — [ACSC executive overview](https://www.cyber.gov.au/publication/small-business-cloud-security-guides-executive-overview)
- Insurers ask K-12 for MFA, EDR, isolated or offline backups, an incident response plan and phishing training (prior note) — [Cybersecure California K-12 checklist](https://cybersecureca.com/k12/cyber-insurance-readiness)

### Inferences
- Lowest-cost stack by org type (inference):
  - *Parish or classical school on Google Workspace for Education Fundamentals (free):* Chromebooks with Chrome Education Upgrade for management, a few Windows office PCs with built-in Defender plus BitLocker and auto-updates, Google 2-Step Verification enforced.
  - *Childcare center or youth program, nonprofit:* free Business Basic for email and MFA. Buy discounted Business Premium only for the 2-5 staff with admin or financial roles, to get Defender for Business and Intune where it matters.
  - *For-profit small daycare:* no nonprofit pricing. Built-in Defender plus Microsoft 365 Business Standard or Google Workspace with MFA is the floor.
- Backups: the documented failure in child-sector incidents is loss or leak of cloud-held records, so cloud-to-cloud backup of Workspace or M365, plus one offline or immutable copy of the office PC's local files, meets the "isolated backups" insurer ask. Specific free backup offers for nonprofits were not researched this session.

### Gaps
- Actual nonprofit price points for Business Premium and the Defender add-ons in 2026 were not confirmed.
- Google Workspace for Education security-tier pricing (Education Standard or Plus) and TechSoup offers for EDR or backup in 2026 were not researched.
- Free EDR options for small nonprofits (e.g., vendor nonprofit programs) were not found in this pass.

---

## 6. Small-org security baselines and how they map to childcare and school realities

### Takeaway
Four government or nonprofit baselines converge on the same short list: MFA, patching and supported OS, admin-privilege limits, backups, secure configuration (no defaults), and an asset inventory. CIS IG1 (56 safeguards) is the most granular. UK Cyber Essentials became stricter in April 2026: MFA on any cloud service that offers it is now mandatory, with automatic failure otherwise. The ACSC recommends its Small Business Guide, then Essential Eight Maturity Level One. None is written for childcare. The IoT layer (cameras, doors) is weakly addressed by all four and needs a supplementary checklist.

### Cited Findings
- CIS IG1 is "essential cyber hygiene," an emerging minimum standard. v8 and v8.1 have 153 safeguards in total; IG1 is a subset widely cited as 56 — [CIS IG1](https://www.cisecurity.org/controls/implementation-groups/ig1); [CIS IG overview](https://www.cisecurity.org/controls/cis-controls-implementation-groups); [Arkansas DESE handout](https://dese.ade.arkansas.gov/Files/CIS_Controls_v8_Implementation_Groups_handout_20220126125456.pdf)
- CIS offers CSAT (Controls Self-Assessment Tool), per third-party sources; confirm on cisecurity.org — [Hudson Valley MSP blog](https://sm911.github.io/compliance-blog/cis/cis-controls-v8-ig1-smbs.html)
- UK Cyber Essentials: from 28 Apr 2025, assessments use Requirements v3.2 and the "Willow" question set. From 27 Apr 2026 (v3.3), MFA must be enabled on any cloud service that offers it (free or paid) or the assessment fails automatically. Cloud services are defined and cannot be excluded from scope. These details come mainly from certification bodies and consultancies — [IASME Apr 2026 update](https://iasme.co.uk/articles/important-update-changes-to-cyber-essentials-for-april-2026/); [NCC Group](https://www.nccgroup.com/major-cyber-essentials-changes-coming-april-27-2026-what-organisations-need-to-know/); [NCSC requirements v3.2 PDF](https://ncsc.gov.uk/files/cyber-essentials-requirements-for-it-infrastructure-v3-2.pdf); [nibusinessinfo](https://www.nibusinessinfo.co.uk/content/cyber-essentials-changes-april-2026)
- ACSC Small Business Cyber Security Guide (Jan 2025 version): MFA and software updates first, then Essential Eight Maturity Level One — [ACSC Jan 2025 PDF](https://cyber.gov.au/sites/default/files/2025-01/ACSC_Small_business_cyber_security_guide_January_2025.pdf); [ACSC guide page](https://www.cyber.gov.au/acsc/view-all-content/publications/small-business-cyber-security-guide)
- ACSC Small Business Cloud Security Guides assume M365 Business Premium and Intune — [ACSC](https://www.cyber.gov.au/publication/small-business-cloud-security-guides-introduction)
- CISA Cyber Essentials was not re-searched this pass. Prior notes reference CISA Cyber Hygiene services enrollment — [economics_insurance_funding.md](../Kids%20data%20defense%20research%20tree/economics_insurance_funding.md)

### Inferences
- Mapping to a 1-building childcare center or parish school (inference):
  - *Asset inventory (CIS 1-2):* includes the NVR, door controller, Wi-Fi gear, copier and every phone with the parent app.
  - *Secure configuration (CIS 4; CE "secure configuration"):* change installer defaults on cameras, door controllers and routers; disable port-forwards.
  - *Account management and MFA (CIS 5-6; CE v3.3 mandatory cloud MFA):* covers the childcare app (Brightwheel, Procare and others), tuition portal, camera cloud, Google or Microsoft, and bank. Remove departed staff on day one.
  - *Patching and supported OS (CIS 7; E8 "patch OS"):* no Windows 10 without ESU; no Chromebooks past AUE; replace camera or NVR firmware that no longer gets updates.
  - *Backups (CIS 11; E8 "regular backups"):* cloud records plus an offline copy.
  - *Data protection (CIS 3):* full-disk encryption; copier drive policy; paper records in locked cabinets.
- UK CE v3.3's auto-fail on cloud MFA is a useful forcing function for US volunteers too: "if the app offers MFA, it's on."
- Creative threads:
  - *The "IT guy" model:* a parent volunteer or a local MSP often holds the only admin credentials to router, cameras and the Google tenant. When that person leaves, the org loses control. A break-glass envelope with a second admin, plus MSP contract clauses for credential handover, is a low-cost control. (Inference; no source found quantifying this.)
  - *Paper records:* enrollment forms, immunization records and custody orders in unlocked file cabinets near reception are higher-risk than most digital stores in tiny buildings. They also fall under the same breach laws when stolen. (Inference.)

### Gaps
- No childcare-specific version of any of these baselines was found. Australia's National Quality Framework and US state licensing information-security requirements were not researched.
- CISA Cyber Essentials and the CISA "Cyber Guidance for Small Businesses" were not re-verified in 2026.
- No published evaluation was found of MSP or volunteer-IT models in small schools.
