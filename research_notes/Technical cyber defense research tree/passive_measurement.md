# Passive, Public-Data Security Measurement of Children's Data Protection: Methods, Precedents, Ethics

Researcher notes, compiled 2026-11-23. Method: web search only. Direct fetches of dl.acm.org and mlab.cyber.nyu.edu failed: those hosts are not on this session's network allowlist and must be allowed before anyone reads the full papers. Findings come from search-result summaries of the cited pages, so check numbers against the primary PDFs before publishing. Items marked "[prior knowledge, not re-verified]" come from the researcher's background knowledge, not from a source read in this session. This file builds on `Kids data defense research tree/public_datasets.md` and does not repeat its dataset inventory (SDPC, AG breach portals, ISL, Utah, Play labels).

Project boundary, restated for this file:
- Public information only.
- Never scan, probe or test systems the project does not own.
- Do not name small organizations in harmful ways.
- The owner has NOT approved passive DNS lookups of other organizations' domains. Every design below that queries a third party's infrastructure, even with a single DNS or HTTP request, is marked **[NEEDS OWNER CONSENT]**.

## 1. Precedents: what prior measurement work did, how, with what ethics and impact

### Takeaway
There is solid precedent for measuring trackers on school and children's websites and email authentication on government and education domains. The most defensible precedents share four habits:
- publish aggregates
- release data and tools so others can reproduce the work
- give named entities a chance to respond before publication
- prefer instrumented observation of public pages over anything resembling intrusion

The highest-impact examples (HRW 2022, The Markup's Pixel Hunt) named large institutions and companies, not small ones. Each paired measurement with right-of-reply letters.

### Cited Findings

**Trackers on school and district websites**
- EdTech Strategies (Doug Levin), 2018. Sample: 159 district homepages.
  - 158 of 159 had a Google, Facebook or Twitter tracker.
  - 143 (90%) used Google Analytics.
  - Only 30 (19%) posted a privacy policy.
  - 43% did not reliably support HTTPS.
  - One district's policy said it used no cookies while its site ran cookie-setting analytics.
  - Dated 2018. — [EdWeek, 2018-01](https://www.edweek.org/technology/state-and-district-education-websites-fail-to-disclose-ad-trackers-study-finds/2018/01); [EdTech Strategies Part III](https://www.edtechstrategies.com/tracking-edu/ad-tracking-and-surveillance/); [EdSurge 2018-01-30](https://www.edsurge.com/news/2018-01-30-cybersecurity-report-spotlights-privacy-concerns-on-state-education-and-district-websites)
- Chanenson et al., "Uncovering Privacy and Security Challenges In K-12 Schools", CHI 2023 (UChicago/NYU).
  - Methods: interviews with 18 school officials and IT staff, plus a scrape of 15,573 US K-12 school and district websites to find the edtech they list or recommend. Third-party trackers were measured on school pages and linked vendor pages.
  - Findings: trackers on 74% of school/district registered domains and 84.9% of vendor domains. Session recorders were also found.
  - The ethics/IRB section could not be read (PDF host blocked). — [ACM DOI 10.1145/3544548.3580777](https://dl.acm.org/doi/fullHtml/10.1145/3544548.3580777); [NSF PAR record](https://par.nsf.gov/biblio/10407360); [PDF (blocked here)](https://mlab.cyber.nyu.edu/static/chi23-k12.pdf); [UChicago news](https://news.uchicago.edu/story/uchicago-nyu-team-find-online-education-tools-pose-privacy-risks)
- ISL 2022 K-12 benchmark: 91.1% of school websites contained trackers, and 79.3% contained "red" (high-risk) trackers. Data from 2022; report published February 2024. — [ISL Findings Report 3 (PDF)](https://internetsafetylabs.org/wp-content/uploads/2024/02/2022-K-12-EdTech-Safety-Benchmark-Findings-Report-3.pdf)
- "Tracking the Trackers: Structural Evolution of Web-Tracking on Educational Websites" (ACM, DOI 10.1145/3795766.3799747). The search summary describes a 13-year longitudinal study (2013-2025) finding that tracker-free educational websites have sharply declined. Venue, authors and data source (likely archived snapshots) were not confirmed because the ACM page was blocked.
  - A related Leiden University thesis used Wayback Machine snapshots for 2012-2021. It found educational sites started with less tracking than a control group but grew faster, and overtook non-educational sites in tracking intensity around 2017. — [ACM DOI](https://dl.acm.org/doi/10.1145/3795766.3799747); [Leiden thesis](https://scholarlypublications.universiteitleiden.nl/access/item%3A3664974/view)
- Methodological ancestor: Lerner et al., "Tracking Excavator" (USENIX Security 2016). It reconstructed third-party tracking from 1996 onward using Wayback Machine snapshots, without touching live sites, and found a four-fold increase. The authors note the figures are underestimates because archives are incomplete. — [USENIX](https://usenix.org/conference/usenixsecurity16/technical-sessions/presentation/lerner); [Tracking Excavator FAQ](https://trackingexcavator.cs.washington.edu/faq.html)
- Children's (non-school) websites: "Targeted and Troublesome" (arXiv 2308.04887, IEEE S&P 2024) crawled about 2,000 child-directed websites. About 90% embedded at least one tracker and about 27% showed targeted ads. — [arXiv](https://arxiv.org/abs/2308.04887)

**Human Rights Watch, "How Dare They Peep into My Private Life?" (2022-05-25)**
- Scope: 163-164 edtech products endorsed by 49 governments during Covid closures (39 apps, 90 websites, 34 both). Testing took place March-August 2021.
- Methods:
  - Apps: manual static analysis by decompiling in Android Studio, plus dynamic analysis. Eight apps were independently re-checked by Esther Onfroy (Exodus Privacy / Pithus).
  - Websites: The Markup's Blacklight, run through a VPN set to each country. Sites that broke under Blacklight were analyzed manually with the same method.
  - HRW released its data and technical evidence for replication.
- Finding: 145 of 163 products (89%) put children's rights at risk.
- — [HRW report](https://www.hrw.org/report/2022/05/25/how-dare-they-peep-my-private-life/childrens-rights-violations-governments); [data Read Me (PDF)](https://features.hrw.org/features/StudentsNotProducts/files/data/_Read_Me_file.pdf); [Explore the data](https://features.hrw.org/features/StudentsNotProducts/files/data)
- Right of reply: HRW wrote to 95 edtech companies, 196 adtech companies and 49 governments. By publication, 48 edtech companies, 78 adtech companies and 10 governments had responded. Two adtech firms (Data Chemistry, Ve Global) said they cut ties with edtech clients that sent them children's data. The work was independently checked by a media consortium (EdTech Exposed, coordinated by The Signals Network). — [HRW news release](https://www.hrw.org/news/2022/05/25/governments-harm-childrens-rights-online-learning); [HRW 2023-02-14 follow-up](https://www.hrw.org/news/2023/02/14/some-governments-companies-take-steps-protect-children)
- Brazil follow-up (2023): HRW shared findings and technical evidence with companies and two state education secretariats, offered several chances to respond, and gave a final opportunity in March 2023 before publishing. — [HRW Brazil 2023-04-03](https://www.hrw.org/news/2023/04/03/brazil-online-learning-tools-harvest-childrens-data)

**The Markup, Pixel Hunt (2022-)**
- Methods:
  - Blacklight, a real-time public-page inspector, finds the Meta Pixel on a page but cannot see what data the pixel sends, and cannot reach pages behind a login.
  - Hospital study: the Newsweek top-100 hospitals were tested by clicking "schedule appointment". On 33 sites the pixel sent data to Facebook.
  - Login-protected patient portals were studied only through consenting volunteers using Mozilla Rally (a consented browser-extension panel). The Markup found the pixel in seven health systems' portals and documented real-patient data flows on five.
- Impact: most hospitals removed the pixel after being contacted. The work drew Congressional questions to Meta.
- — [The Markup: how we built a Meta Pixel inspector](https://themarkup.org/show-your-work/2022/04/28/how-we-built-a-meta-pixel-inspector); [hospital story 2022-06-16](https://themarkup.org/pixel-hunt/2022/06/16/facebook-is-receiving-sensitive-medical-information-from-hospital-websites); [AHCJ case study](https://healthjournalism.org/blog/2022/09/how-a-news-investigation-shed-light-on-potential-patient-privacy-violations/); [HIPAA Journal](https://www.hipaajournal.com/study-reveals-one-third-of-top-100-u-s-hospitals-are-sending-patient-data-to-facebook/); [Congress follow-up](https://themarkup.org/pixel-hunt/2022/09/19/meta-faces-mounting-questions-from-congress-on-health-data-privacy-as-%20Hospitals-remove-facebook-tracker)

**Email authentication (SPF/DKIM/DMARC) measurement**
- Peer-reviewed: "The Evolution of DNS-based Email Authentication: Measuring Adoption and Finding Flaws" (RAID 2021; data December 2018 to May 2020). DMARC adoption was growing, especially for .gov and .edu. SPF reached up to 50.7% of examined domains. — [ACM](https://dl.acm.org/doi/fullHtml/10.1145/3471621.3471842)
- "Lazy Gatekeepers: A Large-Scale Study on SPF Configuration in the Wild" (arXiv 2502.08240, 2025). — [arXiv](https://arxiv.org/pdf/2502.08240)
- Vendor and non-peer-reviewed K-12 figures. These conflict with each other and have unclear methods, so treat them as leads, not facts:
  - Lokentra reports 44.5% of 20,021 K-12 LEA domains with no DMARC record on one page, and an average of 46.7% DMARC adoption across 18,476 districts on another. The site is hosted on a firebase web.app domain, so its provenance is unclear.
  - DMARCguard reports 76.4% DMARC adoption across 3,746 .gov domains, which it attributes to CISA BOD 18-01.
  - A widely repeated dmarcian claim says 60% of 713 US government domains had SPF errors (September 2025). It was not verified against the primary source.
  - — [Lokentra education dataset](https://lokentra-site.web.app/research/education-dataset-paper); [Lokentra education](https://lokentra-site.web.app/research/education); [DMARCguard 2026](https://dmarcguard.io/research/email-authentication/)
- Public DNS datasets:
  - OpenINTEL (University of Twente, SURF, SIDN Labs) runs daily forward-DNS measurements of lists such as Tranco top-1M, including MX/TXT (and therefore SPF and _dmarc), stored as Parquet since about 2015-16. Raw-data access appears to depend on a data agreement, per secondary sources. Tranco is biased toward popular sites, so most school districts are absent. — [RIPE Labs](https://labs.ripe.net/author/artem-berezin/two-providers-a-stubborn-plateau-and-a-very-long-tail-email-in-the-tranco-top-1m/); [ISOC Pulse](https://pulse.internetsociety.org/en/blog/what-99300-domains-reveal-about-email-authentication-and-dns-resilience/)
  - dmarc.org statistics come from Farsight and DomainTools passive-DNS data. — [dmarc.org stats](https://dmarc.org/stats/dmarc/)

**Certificate Transparency as a data source**
- CT logs are public, append-only records of issued certificates. Researchers used them as a data source in "In Log We Trust" (PAM 2018), which cited the Menlo Report, and in "The Rise of Certificate Transparency" (IMC 2018), which discussed the privacy cost of hostnames exposed in CT. — [PAM 2018 PDF](https://www.net.in.tum.de/fileadmin/bibtex/publications/papers/pam18ctlog.pdf); [arXiv 1809.08325](https://ar5iv.arxiv.org/html/1809.08325)
- An EuroSP 2023 study used honeypots to show that appearing in CT logs draws only a modest rise in scanning. In other words, attackers already mine CT logs for reconnaissance. — [APNIC blog 2023-08-30](https://blog.apnic.net/2023/08/30/certifiably-vulnerable-using-certificate-transparency-logs-for-target-reconnaissance/); [paper](https://sites.cs.ucsb.edu/%7Evigna/publications/2023_EuroSP_Certified.pdf)

### Inferences
- The common pattern among the precedents (publish aggregate rates, give large named parties a right of reply, release reproducible data) fits this project's boundary well.
- The weakest link in K-12 measurement right now is that school-specific DMARC figures come only from vendors. A transparent, reproducible, aggregate-only measurement would add real value. Even so, it requires DNS queries to districts' authoritative servers unless an existing dataset covers them, which would be uncommon.
- The Markup's choice to reach login-walled pages only through consenting volunteers is a direct model for the project's rule against touching systems it does not own. It suggests that observing a consenting parent's own browser on their own child's school portal could be defensible, but that step would need IRB-style consent design.

### Gaps
- The ethics sections of CHI'23, the "Tracking the Trackers" paper, and the RAID'21 DMARC paper were not read (hosts blocked).
- No 2023-2026 peer-reviewed study was found that measures DMARC/SPF or HTTPS specifically for US K-12 or childcare domains.
- No precedent was found for measuring childcare-provider websites specifically.
- Systematic HTTPS-adoption studies for US school and government sites (2020-2026) were not found in this session. The 2018 EdTech Strategies figure (43% without reliable HTTPS) is outdated.

## 2. Sources of school and childcare domain lists, and whether to use them

### Takeaway
The NCES Common Core of Data (public schools and LEAs) and the Private School Universe Survey (PSS) are federal public-use files. They are the standard sampling frames used by ISL, CHI'23 and others. Using them to build a domain list is uncontroversial. What needs ethical care is the measurement done against each domain, not the list itself. Childcare and diocesan lists are less clean. They are made up of small organizations, so the project's "don't name small orgs" rule means any findings from them must be reported only as aggregates.

### Cited Findings
- CCD public school and LEA directory files are released yearly (2024-25 preliminary directory available). They contain NCES IDs and location and mailing addresses. Data can also be pulled through ElSi. — [IES 2024-25 CCD preliminary directory](https://ies.ed.gov/use-work/resource-library/data/data-file/2024-25-common-core-data-ccd-preliminary-directory-files); [NCES ElSi](https://nces.ed.gov/ccd/elsi/); [CCD directory page](https://nces.ed.gov/ccd/pub_directory.asp)
- [prior knowledge, not re-verified] Recent CCD school and LEA directory files include a WEBSITE field. It is incomplete and often holds only the district's URL. Confirm the field name in the 2024-25 record layout.
- State directories sometimes have cleaner URL fields. For example, the California Department of Education directory export includes the website address of each school, district, or administrative authority. — [CDE Directory Export file structure](https://www.cde.ca.gov/SchoolDirectory/Topic?id=8)
- PSS 2021-22 is the most recent public-use private school file (SAS, SPSS, text, with documentation and questionnaire). Use the PIN to join across years. A separate geocoded "Private School Locations 2021-22" file is on data.gov. Whether PSS has a website field was not confirmed. — [NCES PSS 2021-22 public-use data](https://nces.ed.gov/use-work/dataset/private-school-survey-public-use-data-2021-22-school-year); [data.gov Private School Locations](https://catalog.data.gov/dataset/private-school-locations-2021-22); [UChicago record](https://knowledge.uchicago.edu/records/1dt7j-gy194)
- CHI'23 scraped 15,573 school and district websites, which shows that such frames are used routinely in academic work. — [NSF PAR](https://par.nsf.gov/biblio/10407360)
- ISL's benchmark drew a stratified sample of 663 schools (13 per state plus DC). — see `public_datasets.md` §4.

### Inferences
- Appropriateness ladder, from most to least appropriate:
  1. CCD/PSS federal files: public, intended for research, cover institutions only (no individuals).
  2. State education department directories: public records.
  3. State childcare licensing directories: public, but many entries are home-based family childcare providers whose "domain" may be a personal Facebook page, and whose address is a home. Collecting and publishing that information raises privacy concerns for individuals. **Recommendation: exclude home-based providers entirely. Use only centers, and report only state-level aggregates.**
  4. Diocesan school lists: public, but they cover small organizations. Aggregate only, consistent with the earlier notes in `Kids data defense research tree/catholic_classical_ecosystem.md`.
- Never republish the joined domain list together with findings (for example, "district X lacks DMARC"). Releasing the frame alone, which is already public, is fine. Attaching findings to small entities turns it into a target list.

### Gaps
- The exact URL coverage rate in CCD (share of LEAs with a non-empty, valid website) was not found.
- Whether PSS includes website URLs.
- Childcare licensing directory formats and terms of use, state by state, were not researched.

## 3. Lighter methods that avoid touching organizations' systems: CT logs, HTTP Archive, Common Crawl, public DNS datasets

### Takeaway
Methods that read existing third-party datasets (HTTP Archive, Common Crawl, the Wayback Machine, CT logs, OpenINTEL/dmarc.org aggregates) do not send a single packet to the measured organization. They are the most defensible under the boundary.

The main limitation is coverage:
- HTTP Archive crawls origins drawn from the Chrome UX Report, which leaves out low-traffic sites, and so leaves out many small schools.
- Common Crawl and Wayback coverage of small school sites is patchy.
- OpenINTEL covers only popular-domain lists.

Querying crt.sh or CT logs touches the CT operator's infrastructure, not the school's. It is passive with respect to the school but still reveals hostnames, so publish with care.

### Cited Findings
- HTTP Archive / Web Almanac 2024:
  - Metrics come from the June 2024 crawl.
  - The URL list is the most recent Chrome UX Report (CrUX) release.
  - The 2025 privacy chapter matches requests against the WhoTracks.Me tracker catalog.
  - 61% of cookies were set in third-party contexts.
  - — [Web Almanac 2024 Methodology](https://almanac.httparchive.org/fr/2024/methodology); [2024 Privacy](https://almanac.httparchive.org/en/2024/privacy); [2025 Privacy](https://almanac.httparchive.org/en/2025/privacy); [2024 Cookies](https://almanac.httparchive.org/en/2024/cookies); [SEJ summary](https://www.searchenginejournal.com/http-archive-report-61-of-cookies-enable-third-party-tracking/532581/)
- [prior knowledge, not re-verified] HTTP Archive data is queryable in Google BigQuery (`httparchive` public dataset). Each crawl records requests, response headers and third-party domains for the home page and, since 2022, some secondary pages. Queries cost BigQuery credits. Joining CCD website hosts against crawled origins gives the subset of schools covered.
- [prior knowledge, not re-verified] Common Crawl publishes monthly WARC/WAT/WET archives plus a URL index (CDX). The raw HTML can be searched for script tags (e.g. `googletagmanager.com`, `connect.facebook.net`, `fbevents.js`) without visiting the site. Static HTML misses trackers that are injected dynamically, so it undercounts.
- Wayback-based reconstruction of trackers is an established, peer-reviewed method (Tracking Excavator, USENIX Sec 2016; Leiden 2012-2021 study), and the authors acknowledge it underestimates. — [Tracking Excavator](https://trackingexcavator.cs.washington.edu/faq.html); [Leiden thesis](https://scholarlypublications.universiteitleiden.nl/access/item%3A3664974/view)
- CT logs are a long-standing research source (PAM 2018, IMC 2018). Attackers already harvest CT logs for reconnaissance (EuroSP 2023), so publishing aggregate CT-derived counts adds little attacker capability. Publishing per-organization hostname lists, though, would make discovery easier. — [PAM 2018](https://www.net.in.tum.de/fileadmin/bibtex/publications/papers/pam18ctlog.pdf); [APNIC 2023](https://blog.apnic.net/2023/08/30/certifiably-vulnerable-using-certificate-transparency-logs-for-target-reconnaissance/)
- OpenINTEL raw data likely needs a data agreement. Aggregates are public. dmarc.org stats come from passive-DNS vendors. — [RIPE Labs](https://labs.ripe.net/author/artem-berezin/two-providers-a-stubborn-plateau-and-a-very-long-tail-email-in-the-tranco-top-1m/); [dmarc.org](https://dmarc.org/stats/dmarc/)
- The IRTF PEARG "Safe Internet Measurement" draft (-14, January 2026, expires July 2026) covers informed, proxy and implied consent. An earlier version said implied consent is insufficient for any experiment that may collect sensitive or identifying data. It cites Allman and Paxson's guidelines on sharing measurement data. No dedicated section on reusing existing datasets was found in the snippets. — [draft -14](https://www.ietf.org/archive/id/draft-irtf-pearg-safe-internet-measurement-14.html); [draft -06](https://datatracker.ietf.org/doc/html/draft-irtf-pearg-safe-internet-measurement-06)

### Inferences: does each method count as "touching" an organization's systems?
| Method | Packets to the measured org? | Under the current boundary |
|---|---|---|
| HTTP Archive (BigQuery) / Common Crawl / Wayback queries | None. The data was collected earlier by a third party with its own crawl policies (robots.txt honored by Common Crawl and Internet Archive). | **Allowed without new consent.** Equivalent to reading a library archive. |
| OpenINTEL aggregates, dmarc.org stats, published vendor datasets | None | Allowed, though a data agreement is needed for raw OpenINTEL data. |
| CT log search (crt.sh, Google CT API) | None to the school. Queries go to the CT operator or crt.sh, which is designed for public search. | Arguably allowed. Treat as a gray area and flag it to the owner, because it enumerates an organization's hostnames. Publish aggregates only. |
| Live DNS TXT/MX lookups for `_dmarc.<district>` via a public resolver | Yes, indirectly: the resolver queries the district's authoritative DNS (often hosted by a registrar or Microsoft/Google). This is a negligible load and the data is published precisely so the world can read it. | **[NEEDS OWNER CONSENT]** per the owner's explicit decision, even though measurement norms treat it as among the most benign measurements. |
| Live HTTP fetch of a school's homepage (Blacklight, OpenWPM) | Yes: equivalent to one page view | **[NEEDS OWNER CONSENT]**, and arguably outside "never test systems you don't own". It is a normal page view, not a test, but the owner should decide. |
| Any port scan, TLS handshake probing or vulnerability scan | Yes | **Prohibited** by the boundary. Do not propose. |

- Ethical nuance for the owner: a DNS TXT lookup asks a public directory for information the domain owner published so that every mail server in the world will read it. Every email a district receives triggers equivalent lookups. The Menlo "respect for persons" concern is minimal here, while the "justice" and "beneficence" concerns center on how results are published (not creating target lists). That said, the owner's caution is legitimate. Volunteers lack an IRB and institutional cover, and a vendor-style "X% of districts are spoofable" headline can be misused.

### Gaps
- What fraction of CCD LEA websites appear in HTTP Archive's CrUX-based crawl. This is the key feasibility number and is cheap to compute once the project decides to query BigQuery.
- Common Crawl's coverage of .k12.xx.us and school domains was not quantified.
- crt.sh's terms of use and rate limits were not found.

## 4. Website privacy measurement of school and childcare sites from archives (2022-2026)

### Takeaway
Prior work shows trackers are close to universal on school sites: 74% (CHI'23), 91% (ISL 2022), 90%+ Google Analytics (2018). Another headline tracker rate would therefore be low insight. The open, high-value questions are narrower:
1. Trackers on **sensitive pages**: enrollment, registration, lunch/free-meal applications, donation and tuition-payment forms, counseling and mental-health pages. This applies the Pixel Hunt "schedule appointment" lens to schools.
2. **Longitudinal change** after events such as state laws and the Meta-pixel publicity.
3. **Private, parochial and childcare sites**, which are understudied.

Archives can answer (2) and part of (1) without live crawling.

### Cited Findings
- CHI'23: trackers on 74% of school/district domains, 84.9% of vendor domains, and session recorders present. — [ACM](https://dl.acm.org/doi/fullHtml/10.1145/3544548.3580777)
- ISL 2022: 91.1% of school websites had trackers, 79.3% had "red" trackers. — [ISL report 3](https://internetsafetylabs.org/wp-content/uploads/2024/02/2022-K-12-EdTech-Safety-Benchmark-Findings-Report-3.pdf)
- Educational sites have shown a 13-year rise in tracking and a decline in tracker-free sites (2013-2025), per the search summary; not verified in full. — [ACM 10.1145/3795766.3799747](https://dl.acm.org/doi/10.1145/3795766.3799747)
- Pixel Hunt showed the high-impact lens is the **data a pixel sends on a sensitive action**, not mere presence. Blacklight alone detects presence but not payload. — [The Markup methodology](https://themarkup.org/show-your-work/2022/04/28/how-we-built-a-meta-pixel-inspector)
- HRW found Google Analytics "remarketing audiences" (an ad feature) on government education sites in Argentina, Spain and Colombia. That is a specific, detectable configuration signal. — [HRW Argentina submission](https://hrw.org/news/2022/11/21/argentina-submission-committee-rights-child); [HRW Spain](https://www.hrw.org/news/2022/12/16/spain-submission-committee-rights-child)

### Inferences
- Archive-only design: take CCD/PSS hosts and look up Wayback/Common Crawl captures of URLs matching `/enroll`, `/registration`, `/donate`, `/give`, `/tuition`, `/lunch`, `/counsel`. Then search the archived HTML for known tracker signatures (Meta Pixel `fbq(`, GA4 `gtag(`, TikTok pixel, session-replay scripts like Hotjar or FullStory). Report the share of schools whose archived sensitive pages load ad pixels, by sector (public, charter, private) and over time.
- Limits of this design:
  - Static HTML misses tag-manager-injected pixels, so findings are lower bounds.
  - Archives rarely capture form submissions, so the actual data sent cannot be observed.
  - Third-party form hosts (e.g. SchoolMint, Finalsite, Blackbaud, donation platforms) are vendors. Vendors are companies, and the project boundary allows naming them. Aggregating by **vendor platform** ("sites using platform P load the Meta Pixel on donation pages at rate R") gives a systemic finding with an accountable, large target.

### Gaps
- No 2022-2026 study was found that focuses on trackers on sensitive school pages specifically (enrollment, donation, meal forms). This looks like a genuine open niche, but absence of evidence is not proof.
- No study of childcare-center websites was found.

## 5. App behavior measurement on one's own device (ISL/AppCensus style): legal and ethical considerations

### Takeaway
Observing your own device's network traffic while running apps you installed is within the project boundary ("systems you own"), and HRW, ISL, Utah/BYU and academia all have precedent for it. Legal risk is low but not zero:
- Breaking TLS certificate pinning or decompiling may involve DMCA §1201 anti-circumvention. The Copyright Office's good-faith security research exemption was renewed in the ninth triennial rulemaking (effective 2024-10-28). Its exact scope should be read before relying on it.
- App terms of service often prohibit reverse engineering. That is a contract risk, not a criminal one, after Van Buren.

The ethics hinge on using test accounts, never using real children's data or accounts, and not interacting with other users.

### Cited Findings
- HRW 2022: static analysis by decompiling in Android Studio, dynamic analysis, and independent replication by Exodus Privacy/Pithus. — [HRW report](https://www.hrw.org/report/2022/05/25/how-dare-they-peep-my-private-life/childrens-rights-violations-governments)
- Utah/BYU/ISL 2023-25: traffic analysis of 100 apps compared against DPAs. — see `public_datasets.md` §4; [USBE report](https://www.schools.utah.gov/studentdataprivacy/files/Utah%20EdTech%20App%20Data%20Collection%20and%20Sharing%20-%202023-25%20Investigation.pdf)
- "Not Seen, Not Heard" (arXiv 2303.09008): 81.25% of Play "Family" apps used trackers that Play disallows for children's apps. — [arXiv](https://arxiv.org/abs/2303.09008)
- DMCA §1201, ninth triennial rule effective 2024-10-28. DOJ's Criminal Division supported renewing the security-research exemption. A proposed AI-trustworthiness research exemption was denied. — [Copyright Office 1201 (2024)](https://copyright.gov/1201/2024/); [DOJ letter](https://www.Copyright.gov/1201/2024/USCO-letters/Letter%20from%20Department%20of%20Justice%20Criminal%20Division.pdf); [CDT](https://cdt.org/blog/security-research-and-the-dmca-the-copyright-office-streamlines-the-exemption-process/); [IPWatchdog 2024-10-25](https://ipwatchdog.com/2024/10/25/copyright-office-denies-proposed-ai-security-research-exemption-triennial-rulemaking-dmca/)
- CFAA: per Van Buren (2021) and hiQ (9th Cir. 2022), accessing public data without bypassing authentication is likely not "without authorization". — see `public_datasets.md` §5.

### Inferences
- Tools (prior knowledge, not re-verified; check current versions):
  - mitmproxy, or HTTP Toolkit, on a rooted spare Android device or emulator
  - PCAPdroid (no root, VPN-based capture with optional TLS decryption)
  - Exodus Privacy (static tracker-signature detection from APKs, with no execution needed)
  - Frida/objection for unpinning (this is the step that touches §1201)
  - TrackerControl
- Lowest-risk tier: **static signature scans of APKs** (Exodus-style), which detect embedded SDKs from public app packages, need no account, send no traffic, and involve no circumvention. These can be compared against Play Data Safety labels and DPAs.
- Middle tier: **dynamic analysis without decryption**. Record which domains the app contacts (DNS/SNI) on your own device with a test account. The only party touched is the app's own servers, through normal use of the app.
- Highest tier: **TLS interception with unpinning**. It shows payload contents (e.g. whether a student name reaches an ad SDK). Read the exact §1201(j)/exemption text first, keep logs private, and consider partnering with ISL or a university.
- Ethical guardrails:
  - Never use a real child's account or a real school login.
  - Create test accounts only where the terms allow self-registration. Do not impersonate a school or obtain teacher credentials under false pretenses.
  - Do not submit fake data into school systems.
  - Delete captured third-party data.

### Gaps
- The exact text and conditions of the 2024 renewed security-research exemption (whether it requires lawful acquisition, good faith, and no violation of other laws) were not retrieved.
- State law (e.g. California Penal Code 502) as applied to own-device traffic analysis was not reviewed.
- ISL's and AppCensus's published methodology and ethics documents were not fetched in this session.

## 6. Responsible disclosure for systemic, aggregate findings

### Takeaway
Classic coordinated vulnerability disclosure (CVD) is designed for specific bugs in specific products. Aggregate findings ("X% of districts lack DMARC", "Y% of donation pages load a pixel") have no single owner. Precedent suggests a hybrid approach:
1. Give **large named parties** (vendors, state agencies, big districts) a pre-publication right of reply with technical evidence, as HRW and The Markup did.
2. Notify **sector intermediaries** privately (K12 SIX, MS-ISAC, state education department CPOs, SDPC/A4L) so they can push remediation guidance.
3. **Do not name small entities**. Publish distributions and medians.
4. Release methods and code, but not per-entity target lists.

### Cited Findings
- HRW sent letters with evidence to 95 edtech companies, 196 adtech companies and 49 governments, and published response counts (48/78/10). It gave final opportunities to respond before publication in the Brazil work. Some adtech firms changed behavior (cut ties). — [HRW 2022 release](https://www.hrw.org/news/2022/05/25/governments-harm-childrens-rights-online-learning); [HRW Brazil 2023](https://www.hrw.org/news/2023/04/03/brazil-online-learning-tools-harvest-childrens-data); [HRW 2023-02 follow-up](https://www.hrw.org/news/2023/02/14/some-governments-companies-take-steps-protect-children)
- The Markup contacted hospitals before publication. Most removed the pixel; two had not at publication time. — [HIPAA Journal](https://www.hipaajournal.com/study-reveals-one-third-of-top-100-u-s-hospitals-are-sending-patient-data-to-facebook/)
- EdTech Strategies (2018) and CHI'23 published aggregate rates. CHI'23 directed recommendations at policymakers and educators rather than naming districts, per available summaries. — [EdWeek 2018](https://www.edweek.org/technology/state-and-district-education-websites-fail-to-disclose-ad-trackers-study-finds/2018/01); [UChicago news](https://news.uchicago.edu/story/uchicago-nyu-team-find-online-education-tools-pose-privacy-risks)
- The PAM 2018 CT paper invoked the Menlo Report and published data and code for reproducibility. — [PAM 2018](https://www.net.in.tum.de/fileadmin/bibtex/publications/papers/pam18ctlog.pdf)
- The Menlo Report remains the baseline framework. A 2025 study found most measurement researchers rely on informal norms. — see `public_datasets.md` §5; [arXiv 2511.10408](https://arxiv.org/html/2511.10408v1)

### Inferences
- A disclosure protocol for this project:
  - (a) Before publication, send each **vendor** named in a finding the evidence, with a 30-45 day reply window. This is a common CVD-style window [prior knowledge].
  - (b) Brief the state CPO (e.g. NYSED for New York) and MS-ISAC/K12 SIX on sector-level results.
  - (c) Offer any individual school a private lookup of its own result on request. Do not publish one.
  - (d) Publish aggregates, methods and code, with a statement of what was not done (no scanning, no logins).
  - (e) If a finding reveals a live, specific vulnerability or exposed child PII, stop, do not retain the data, and notify the owner privately (and CISA if appropriate). Never include it in aggregate publication.

### Gaps
- No formal standard (ISO 29147/30111, CISA CVD) addressing aggregate, non-vulnerability findings was retrieved.
- How K12 SIX or MS-ISAC accept third-party research notifications was not checked.

## 7. Ranked measurement designs (insight x ethics x effort) for a solo volunteer

Scoring: H/M/L. "Ethics risk" is the residual risk after mitigations. Consent marking is per the project boundary.

| Rank | Design | Data source | Method | Insight | Ethics risk | Effort | Owner consent? |
|---|---|---|---|---|---|---|---|
| 1 | **Trackers on sensitive school pages, from archives** (enrollment, donation, tuition, meal, counseling pages) | CCD + PSS hosts joined to HTTP Archive (BigQuery) and Common Crawl/Wayback captures | Search archived HTML and HAR data for pixel and session-replay signatures. Aggregate by sector, state, year and **form-vendor platform** | H (open niche; Pixel Hunt lens; names only vendors) | L (no packets to schools) | M (BigQuery costs; coverage gaps) | **No**: reads existing datasets only. Inform the owner anyway. |
| 2 | **Static SDK census of DPA-covered edtech apps** | Public APKs of vendors listed in SDPC/NYC 2-d; Exodus Privacy reports | Static tracker-signature scan, compared against Play Data Safety labels and DPA advertising/sale clauses | H (systemic; vendor-level; extends the Utah finding nationally) | L (no execution; public packages; vendors are companies) | M | No (own analysis of public files). Check app terms. |
| 3 | **Longitudinal tracker trend on school sites (2015-2026)** | Wayback/Common Crawl captures of CCD district homepages, sampled | Tracking Excavator-style reconstruction; trend in GA, Meta and remarketing tags; before/after state privacy laws | M-H | L | M-H (archive coverage, API rate limits) | No |
| 4 | **Own-device dynamic traffic study of the top ~20 edtech apps** used in NYC (from the 2-d list) | Spare phone or emulator, test accounts | PCAPdroid/mitmproxy; domains only first; payload only with a §1201 review | H | M (test accounts only; §1201/ToS) | H | Within boundary (own device), but **recommend owner sign-off** and an ISL/university partner for the decryption step. |
| 5 | **K-12 DMARC/SPF posture census, transparent and reproducible** | CCD LEA domains, then live `_dmarc` TXT lookups via a public resolver | One TXT and one MX query per domain, rate-limited, with an identifying contact; publish state and sector distributions only | M-H (replaces opaque vendor numbers; relevant to phishing of parents) | L-M (benign queries; publication risk of a spoofable-target list) | L | **YES: NEEDS OWNER CONSENT** (live DNS of others' domains). |
| 5b | Same, archive-only variant | OpenINTEL (data agreement), dmarc.org/passive-DNS aggregates | Filter to education domains present in these datasets | M (coverage biased to large districts) | L | M (agreements) | No |
| 6 | **CT-log hostname census of school vendors/platforms** | crt.sh / CT logs for CCD domains | Count subdomains pointing to SIS/LMS/form vendors (e.g. `*.powerschool.com` CNAME patterns appear only via DNS, so CT gives only names) to estimate vendor concentration | M (vendor concentration = systemic single points of failure) | M (hostname enumeration resembles recon; publish only aggregates) | L-M | **Gray: recommend OWNER CONSENT** (does not touch schools, but enumerates their infrastructure). |
| 7 | **Live Blacklight-style crawl of school homepages and sensitive pages** | CCD hosts | One headless page view per URL, rate-limited, identifying user-agent | H (catches dynamic tags that archives miss) | M (it is a normal page view, but it is live interaction) | M | **YES: NEEDS OWNER CONSENT.** Use only to validate #1 on a small sample, if approved. |
| 8 | **Childcare center website privacy/security baseline** | State licensing directories (centers only) + archives | Archive-only presence of privacy policy and trackers on enrollment pages; state aggregates | M (unstudied sector) | M (small orgs; home providers excluded) | H (messy directories, low archive coverage) | No for the archive-only version. Live version needs consent. |

### Takeaway
The best first project needs no consent change: Design 1, trackers on sensitive school pages measured from HTTP Archive and Common Crawl and aggregated by form-vendor platform. It pairs naturally with Design 2, the static SDK census of DPA-covered apps. Both name only companies, send nothing to schools, and extend existing work (Pixel Hunt, Utah/BYU) into a niche no published study was found to cover. The DMARC census (Design 5) is the cheapest and most benign *active* measurement, but it requires the owner's explicit consent and a publication plan that avoids creating a target list.

### Inferences
- A reasonable ethics statement for any of these: Menlo principles (respect for persons, beneficence, justice, respect for law and public interest); data minimization; no PII collected; aggregate publication; vendor right of reply; no scanning; and an archive-first choice that avoids imposing any load on schools.
- Archive coverage bias (toward larger, higher-traffic districts) must be reported. It likely *understates* problems at small schools, which also have the fewest IT resources.

### Gaps
- None of these designs has been piloted. Coverage of CCD hosts in HTTP Archive and Common Crawl is the main feasibility unknown for Designs 1, 3 and 8.
- Whether OpenINTEL would grant data access to an unaffiliated volunteer.
