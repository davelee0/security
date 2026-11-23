# Email impersonation and payment-diversion fraud defense for small child-serving organizations

Scope: technical controls, measurement methods and `checkup` extensions that reduce BEC, vendor email compromise (VEC), payroll diversion and lookalike-domain fraud for small schools (including parish and classical schools), childcare centers, youth nonprofits and dioceses. Researched Nov 2026. Method note: ic3.gov did not resolve from this research environment, so IC3 figures come from search-result extracts of the IC3 PDFs and secondary write-ups. Treat exact IC3 numbers as "verify against the PDF". Most adoption data are vendor-produced (Red Sift, Valimail, EasyDMARC, dmarcian, PowerDMARC, dmarcguard). Their populations and denominators differ, so numbers are not directly comparable.

Context carried forward from earlier notes (Kids data defense research tree): BEC plus funds-transfer fraud was about 60% of Coalition's 2024 small-business cyber claims and 58% of its 2025 claims. Cases include Dickinson ND, about $4.92M in two redirected vendor payments (Feb 2026); Sudbury MA payroll diversion of more than $12K after MFA was intercepted (2025); New Haven CT, more than $6M via the COO's mailbox with $3.6M recovered (2023); and Ohio Auditor findings of direct-deposit changes made on emailed requests (2024-2025). Sources are in `threat_landscape.md` and `economics_insurance_funding.md`.

---

## 1. DMARC/SPF/DKIM adoption among K-12, private schools, nonprofits and churches, and the effect of the 2024-2025 mailbox-provider sender requirements

### Takeaway
I found no published DMARC measurement specific to US K-12 districts, private or parochial schools, churches or dioceses. That is itself a finding, and a gap `checkup` could fill. The closest proxies all show that a DMARC record is now common, but enforcement (p=quarantine or p=reject) is rare: roughly 9-14% of education domains reject, and nonprofit/.org adoption is far lower. The Google/Yahoo (Feb 2024) and Microsoft (May 2025) bulk-sender rules sharply increased the number of DMARC records, mostly at p=none, which does not stop spoofing.

### Cited Findings
**Education proxies (no K-12 breakdown found)**
- dmarcian, US and Canada higher education (top 500 US institutions): 28% have no DMARC record; 77% of parent domains are unprotected (no record, broken record, or p=none); only 9% are at p=reject and 14% at p=quarantine. — [dmarcian](https://dmarcian.com/dmarc-adoption-among-us-and-canada-higher-education/)
- DmarcDkim, education sector (about 8,610 education domains, "as of September 2026"): 13.7% have full protection (reject at 100%) and 29.0% have partial coverage (quarantine or partial pct). — [DmarcDkim Education 2026](https://dmarcdkim.com/dmarc-adoption/education)
- dmarcguard scan of 5.5M domains (Feb 2026): .edu (4,332 domains) shows 84.0% DMARC adoption, with 761 at p=reject (about 17.6%, my calculation). That is much higher record adoption than the older higher-ed surveys, likely because of method and domain list. — [dmarcguard research](https://dmarcguard.io/research/email-authentication/)
- Older or undated: one summary says 7.8% of US educational institutions reject; EasyDMARC found 52.77% of 252 US institutions had deployed DMARC. — [DMARC Report](https://dmarcreport.com/blog/dmarc-adoption-amongst-us-education-sector/); [EasyDMARC](https://easydmarc.com/blog/dmarc-and-educational-institutions-in-the-usa/)
- Private K-12 schools mostly use .org or .com domains, not .edu or .k12.xx.us. So .edu figures likely overstate private-school posture (inference; see Inferences).

**Nonprofits and churches**
- EasyDMARC .org research: about 1.2% of nearly 10M .org domains had DMARC. Among top US nonprofits, adoption was about 20%, and 45.6% of those records were misconfigured. This appears to predate 2025. — [Dark Reading](https://www.darkreading.com/cyberattacks-data-breaches/nonprofit-domains-basic-dmarc-impersonation-protections); [EasyDMARC .org eBook](https://easydmarc.com/blog/ebook/org-domain-research-dmarc-adoption-in-nonprofits/)
- No church-, diocese- or faith-based DMARC measurement was found in any search.

**Global baselines (2025-2026)**
- EasyDMARC 2025: DMARC adoption among top domains rose to 47.7% (from about 27-29% in 2023; its sources disagree on the baseline). More domains monitor (p=none) than enforce. — [EasyDMARC 2025 report](https://easydmarc.com/blog/ebook/easydmarc-dmarc-adoption-report-2025/); [MSPAA summary](https://mspaa.net/easydmarc-2025-dmarc-adoption-report/)
- Red Sift (Dec 2025, 73.3M domains): 14.9% have any DMARC record and 2.5% enforce p=reject. — cited via search extract of Red Sift analysis; see also [Red Sift US DMARC report](https://redsift.com/blog/us-dmarc-adoption-report)
- dmarcguard (Feb 2026, 5.5M Tranco domains): 30.4% adoption and 12.8% enforcing. — [dmarcguard](https://dmarcguard.io/research/email-authentication/)
- DomainsProject (150M mail domains): "only 9% actually stop spoofing". — [DomainsProject blog](https://domainsproject.org/blog/a-state-of-txt)
- Peer-reviewed: USENIX Security 2023, "You've Got Report", measured DMARC reporting deployment across .com/.net/.org/.se over 13 months and found widespread mismanagement of the rua/ruf reporting addresses (a 2023 paper, slightly outside the window). — [USENIX Sec '23](https://www.usenix.org/conference/usenixsecurity23/presentation/ashiq)

**Effect of the sender requirements**
- Gmail and Yahoo bulk-sender rules became mandatory in February 2024. Senders of more than about 5,000 messages a day to Gmail need SPF, DKIM, aligned DMARC (at least p=none), one-click unsubscribe and a spam complaint rate under 0.3%. Microsoft began enforcement for Outlook.com/Hotmail/Live on May 5, 2025. Sources differ on whether non-compliant mail is junked or rejected; one cites rejection code 550 5.7.515. — [Courier](https://www.courier.com/blog/email-sender-requirements); [PowerDMARC](https://powerdmarc.com/bulk-email-sender-requirements/); [dmarc.com](https://dmarc.com/en/blog/gmail-yahoo-sender-requirements)
- Google reportedly increased temporary and permanent rejections of non-compliant bulk mail from November 2025 (vendor-reported). — [Poscha](https://poscha.com/compliance/gmail-yahoo-microsoft-sender-requirements/)
- Valimail: more than 500,000 of the top 10M domains published a DMARC record by the end of February 2024, which Valimail credits to the Google/Yahoo rules. — [Valimail](https://www.valimail.com/blog/dmarc-growth-data/)
- Red Sift: 795,824 additional DMARC records worldwide between early January and end of February 2024; about 2.3M domains added DMARC in the following year, roughly doubling adoption, while about 87% of domains still lack a record. — [Red Sift one-month](https://redsift.com/blog/where-are-we-now-one-month-of-google-and-yahoos-new-requirements-for-bulk-senders); [Dark Reading](https://www.darkreading.com/remote-workforce/google-dmarc-push-email-security-challenges); [Red Sift 2.3M](https://redsift.com/blog/2-million-organizations-embrace-dmarc-compliance)
- senderreputation.org: valid DMARC records rose 79% from 2023 to early 2026 (937,931 domains in its set), but only 411,935 are enforced. — [senderreputation.org](https://senderreputation.org/blog/state-of-email-authentication-2026)

### Inferences
- The sender rules require only p=none, so they produced records, not protection. A small school that "has DMARC" because a newsletter platform made it add one is probably still spoofable. `checkup` should keep treating p=none as a warning with a clear path to enforcement, not as a pass.
- Most small schools, parishes and childcare centers send fewer than 5,000 messages a day, so the bulk rules don't strictly apply to them. They are affected indirectly, through their newsletter, SIS or tuition-platform vendors (e.g. Constant Contact, Mailchimp, FACTS, ParentSquare) that send as their domain. Moving to p=reject requires those third-party senders to be aligned, which is where DMARC report parsing earns its keep (see section 7).
- DMARC enforcement protects the org's own domain against exact-domain spoofing of parents, staff and vendors. It does nothing against lookalike domains, display-name spoofing from Gmail accounts, or a compromised real mailbox. In the Dickinson, New Haven and Philadelphia losses, attackers used a vendor's or the org's real mailbox or a lookalike domain, not exact spoofing (inference from case descriptions in earlier notes). DMARC is necessary hygiene but not the main loss-stopper.
- A K-12/private-school/church measurement could be built by the project itself: run `checkup` (DNS-only) over public directory lists (NCES Private School Survey, NCES CCD district websites, diocesan school directories) and publish only aggregate statistics. That would produce the first such dataset I could find.

### Gaps
- No K-12-district, private-school, Catholic-school, church or diocese DMARC study was found for 2023-2026.
- Google's own figures on reductions in unauthenticated mail after 2024 (reported by Valimail and Dark Reading) were not extracted, so no number is given here. — see [Valimail "Google stats"](https://www.valimail.com/blog/google-stats-dmarc/)
- The exact Microsoft 2025 enforcement action (junk vs reject) is inconsistent across secondary sources; check Microsoft's own Tech Community post.

---

## 2. Vendor email compromise: why DMARC doesn't help, and free controls in Workspace/M365

### Takeaway
In VEC the attacker sends from the vendor's real, authenticated mailbox (or from a lookalike domain with its own valid SPF/DKIM/DMARC), so every authentication check passes. The controls that work are process controls (out-of-band callback, dual approval) plus mailbox UI cues. The free M365 cues are the first-contact safety tip, spoof intelligence and external tagging; impersonation protection needs Defender for Office 365. Workspace offers external-recipient warnings and lookalike-domain spoofing protection in Gmail safety settings.

### Cited Findings
- Abnormal (vendor telemetry, 1,400+ orgs): organizations faced a 70% chance of receiving at least one VEC attack per week in 2024; 83% of large enterprises saw VEC in 2024. Employees engaged with 44.2% of read VEC messages (72% at the largest firms). Attackers attempted to steal more than $300M via VEC over 12 months. Vendor-reported. — [Abnormal VEC engagement report](https://abnormal.ai/resources/employee-engagement-vendor-email-compromise-threat-report); [Abnormal press release](https://abnormal.ai/newsroom/press-releases/employee-engagement-vendor-email-compromise-threat-report); [Abnormal H1 2025](https://abnormal.ai/resources/threat-reports/h1-2025-report-bec-vec-phishing-trends); [BetaNews](https://betanews.com/2025/06/03/vendor-email-compromise-attacks-get-more-effective-in-large-enterprises/)
- FBI IC3 2025: 24,768 BEC complaints with $3,046,598,558 in losses (2024: 21,442 complaints, $2,770,151,146). BEC ranked second by loss after investment fraud. IC3 does not break out VEC. — [IC3 2025 report PDF](https://www.ic3.gov/AnnualReport/Reports/2025_IC3Report.pdf); [Red Sift summary](https://redsift.com/blog/fbi-ic3-2025-report-email-fraud)
- AFP survey (via aggregator): 74% of organizations experienced BEC in the past year, up from 63% in 2024. Secondary source. — [Deepstrike](https://deepstrike.io/blog/business-email-compromise-statistics)
- Microsoft 365: the "first contact safety tip" is available in anti-phishing policies for **all** cloud mailboxes (EOP included) and has no dependency on impersonation settings. It is **off** in the default policy and **on** in the Standard and Strict preset policies. — [Microsoft Learn: anti-phishing policies](https://learn.microsoft.com/en-us/defender-office-365/anti-phishing-policies-about); [Microsoft Learn: recommended settings](https://learn.microsoft.com/en-us/defender-office-365/recommended-settings-for-eop-and-office365); [Preset security policies](https://learn.microsoft.com/en-us/defender-office-365/preset-security-policies)
- User and domain impersonation protection (including protecting your own domain and up to N named users or vendor domains against lookalikes) requires Defender for Office 365 Plan 1 or 2; EOP alone lacks it. Sources conflict on how P1 is bundled. — [Microsoft Learn: anti-phishing policies](https://learn.microsoft.com/en-us/defender-office-365/anti-phishing-policies-about); [PowerDMARC](https://powerdmarc.com/anti-phishing-policy-office-365/); [Adaptive Security](https://www.adaptivesecurity.com/blog/email-security-for-microsoft-365)
- Google Workspace: Gmail > Safety > Spoofing and authentication includes "Protect against domain spoofing based on similar domain names" (lookalikes such as swapped letters or 0-for-o), with actions such as warn, spam or quarantine. Guides recommend enabling it and note some false positives from genuine partner domains. Edition availability was not confirmed. — [Adaptive Security Workspace guide](https://www.adaptivesecurity.com/blog/email-security-for-google-workspace-the-complete-guide); [Goodheart Tech nonprofit setup](https://learn.goodhearttech.org/google-workspace/google-workspace-nonprofit-setup/configure-email-protection-settings-in-google-workspace); [Aegis AI BEC in Workspace](https://www.aegisai.com/perspectives/bec-protection-google-workspace)

### Inferences
- The DMARC limit in VEC is structural: DMARC authenticates the domain, not the intent. A message from `ap@realvendor.com` sent by an intruder in that mailbox is DMARC-aligned and passes. Only behavioral signals (new bank details, reply-to changes, urgency, thread hijack) or out-of-band verification catch it.
- For a small M365 tenant on Business Basic or Standard, the free wins are: turn on the Standard preset (first-contact tip, spoof intelligence), add an "External" sender tag (Exchange `Set-ExternalInOutlook -Enabled $true`, a native Outlook feature), and create a mail-flow rule that flags messages mentioning "bank", "routing", "ACH", "wire" or "direct deposit" from external senders. These are low cost and can be scripted into a checklist. (The specific cmdlet is from general Microsoft knowledge and was not verified in this session.)
- Business Premium (which, per Microsoft licensing pages, bundles Entra ID P1 and Defender for Office 365 P1; verify current terms) is the realistic tier that unlocks impersonation protection plus Conditional Access for a small school.
- Detecting mailbox compromise inside the org (attacker inbox rules that hide replies, forwarding to external addresses) is a strong, free signal. M365 alert policies and the Workspace audit log both show new forwarding and filter rules. This was the persistence mechanism in many school BEC cases described in earlier notes (inference).

### Gaps
- No public data on VEC prevalence specifically among schools or nonprofits.
- The Gmail lookalike-domain setting's availability across Workspace editions (Business Starter, Education Fundamentals, Nonprofits) was not confirmed.
- Current Microsoft nonprofit licensing (Business Premium grant or discount status in 2025-2026) was not verified.

---

## 3. Lookalike domains: defensive monitoring for your own domain

### Takeaway
Lookalike monitoring for one domain is cheap and technically easy: dnstwist permutations plus certificate-transparency lookups (crt.sh) plus MX/registration checks. The hard parts are noise, and the fact that small orgs can do little about a hit besides warning staff, vendors and parents and filing abuse reports. A free, DNS-and-CT-only, weekly "new lookalikes with MX records" digest is feasible for a volunteer service. Public false-positive measurements were not found.

### Cited Findings
- dnstwist generates typo, homoglyph and TLD variants and checks which are registered. The flags `-r` (registered only), `-m` (MX check, i.e. mail-capable) and `-s` (page similarity) narrow output to registered, mail-capable, clone-like hits. Outputs are candidates, not confirmed threats. — [Trickest dnstwist](https://trickest.com/tools/dnstwist); [Vantage OSINT](https://vantageosint.com/tools/dnstwist)
- Practitioner guidance: a monthly dnstwist scan plus a monthly crt.sh review of new certificates on lookalike names gets "80% of the value at zero cost" for most non-regulated sites. — [GuardYourDomain](https://guardyourdomain.com/threats/lookalike-domains/); [sitemapfixer domain monitoring](https://sitemapfixer.com/learn/domain-monitoring)
- CT monitoring caveats: each certificate is logged twice (precertificate and final), so pipelines must dedupe; matching on a keyword catches unrelated sites sharing that string. — [DEV Community CT guide](https://dev.to/truong_bui_eaec3f963bbe21/how-to-monitor-certificate-transparency-logs-for-lookalike-domains-jd2); [Censys](https://censys.com/blog/cert-happens-protecting-your-brand-with-censys-collections/)
- Paid brand and domain-monitoring services aggregate all CT logs. Free options are permutation tools plus CT search. — [Wikipedia: Certificate Transparency](https://en.wikipedia.org/wiki/Certificate_Transparency); [ChainPatrol buyers' guide](https://chainpatrol.com/buyers-guide/best-domain-monitoring-services)

### Inferences
- **Signal-to-noise design**: BEC lookalikes need MX records to receive replies and often SPF to send. So the high-value filter is "registered + has MX (or SPF) + registered or first seen in the last N days". That cuts dnstwist's thousands of permutations to a handful. CT alone misses mail-only lookalikes (an attacker needs no TLS certificate to send mail), so DNS MX checks matter more than CT for BEC. CT is better for credential-phishing sites.
- **Short or generic names are noisy**: a parish domain like `stmarys.org` collides with hundreds of legitimate St. Mary's organizations, so many "lookalikes" are real parishes. Any free service must whitelist by a known-org list, or present results as "review" rather than "threat".
- **Vendor-side monitoring is more valuable than own-domain monitoring** for payment diversion. In Dickinson-style cases the attacker impersonates the vendor to the school. Running lookalike checks on the org's top 10-20 payees' domains (from its AP vendor list) would catch the lookalike used to divert *outgoing* payments. Own-domain monitoring mainly protects parents and other schools.
- **Cost**: dnstwist plus DNS queries for one domain is seconds of compute. crt.sh is free but rate-limited and sometimes slow, so a service should cache and query weekly. CertStream (real-time CT) requires a persistent connection, which suits a central service but not a CLI.
- **Action path for hits**: report to the registrar's abuse contact and the hosting provider, add the domain to the tenant block list (M365 Tenant Allow/Block List; Gmail blocked senders), and warn the business office. Small orgs rarely have trademark standing for UDRP, so takedown is best-effort.

### Gaps
- No measured false-positive rates for dnstwist or CT-based lookalike detection at small-org scale.
- No data on how often lookalikes of school or church domains are registered (could be measured by the project).
- crt.sh service-level and rate-limit specifics were not verified.

---

## 4. AiTM phishing that steals session cookies despite MFA, and which defenses stop it at what license tier

### Takeaway
AiTM kits such as Tycoon2FA proxy the real login, so push, OTP and SMS MFA all complete, and the attacker takes the session cookie. This is the likely mechanism in the Sudbury "MFA interception" case. Origin-bound credentials (passkeys/FIDO2 security keys) defeat the relay, and CISA calls FIDO/WebAuthn the only widely available phishing-resistant method. In M365, enforcing them by policy (authentication strengths) and binding tokens to devices (token protection) both require Conditional Access, which means Entra ID P1 (e.g. Business Premium). Passkeys themselves can be registered without P1.

### Cited Findings
- Microsoft (Mar 2026) on Tycoon2FA: the kit relays credentials to the real service, triggers the genuine MFA challenge, and captures the session cookie for real-time access. — [Microsoft Security Blog, Mar 4 2026](https://www.microsoft.com/en-us/security/blog/2026/03/04/inside-tycoon2fa-how-a-leading-aitm-phishing-kit-operated-at-scale/)
- Stolen cookies allow session replay and so bypass MFA, even if the password is changed afterward. Tokens must be revoked. — [Sekoia Tycoon 2FA analysis](https://www.sekoia.com/blog/tycoon-2fa-an-in-depth-analysis-of-the-latest-version-of-the-aitm-phishing-kit)
- Tycoon 2FA targets both Entra ID and Google Workspace accounts. — [Cybersecurity News](https://cybersecuritynews.com/tycoon-2fa-aitm-kit-bypasses-mfa/)
- CISA calls FIDO/WebAuthn "the only widely available phishing-resistant authentication" and recommends prioritizing IT admins and help-desk staff, then email and identity systems. OTP, push and SMS leak to relays. This is quoted via secondary sources; I did not open the CISA fact sheet directly. — [Jimber](https://jimber.io/blog/bypassing-mfa-how-aitm-phishing-works-and-what-stops-it/); [Push Security](https://pushsecurity.com/blog/phishing-2-0-how-phishing-toolkits-are-evolving-with-aitm)
- Caveat: phishing-resistant MFA does not stop device-code or OAuth consent phishing. One secondary source claims Tycoon2FA variants try to steer users off passkeys (downgrade), which I could not verify against primary sources. Several sources report a March 2026 Europol-led takedown of Tycoon 2FA, with Mamba 2FA and Whisper 2FA picking up activity afterward (unconfirmed). — [iamdevbox](https://www.iamdevbox.com/posts/aitm-phishing-starkiller-tycoon-2fa-mfa-bypass-defense/); [nhimg AiTM guide](https://nhimg.org/aitm-phishing-guide)
- Token protection in Conditional Access requires Entra ID P1. It is GA for Windows, with Apple platforms in preview or limited at the time of writing, and has exclusions such as Teams Rooms and bulk-enrolled devices. — [Microsoft Learn: token protection deployment guide](https://learn.microsoft.com/en-us/entra/identity/conditional-access/deployment-guide-token-protection-windows); [Petri](https://petri.com/microsoft-entra-conditional-access-token-protection/)
- Conditional Access requires Entra ID P1 or P2; risk-based policies (Entra ID Protection) require P2. Every user governed by a CA policy needs a P1 license (community answer). — [Microsoft Learn: plan CA deployment](https://learn.microsoft.com/en-us/entra/identity/conditional-access/plan-conditional-access); [Microsoft Learn: mandatory MFA](https://learn.microsoft.com/en-us/entra/identity/authentication/concept-mandatory-multifactor-authentication); [Microsoft Entra licensing](https://learn.microsoft.com/en-us/entra/fundamentals/licensing); [Microsoft Q&A](https://learn.microsoft.com/en-us/answers/questions/5524589/microsoft-licensing-requirement-for-conditional-ac)

### Inferences
- **Tiered recommendation for a small org**:
  - Free (M365 Basic/Standard with security defaults; any Workspace edition): register passkeys or security keys for the bookkeeper, payroll and business-manager, principal or pastor, and admin accounts. Phishing resistance holds only if weaker methods can't be used. Without Conditional Access you can't *require* the passkey, so an AiTM page can still push the user to an OTP or push fallback. Removing other methods for those users helps. In Workspace, the Advanced Protection Program or admin-enforced security-key-only 2SV is the analogue (edition specifics not verified here).
  - Business Premium / Entra P1: a CA policy requiring "phishing-resistant MFA" authentication strength for finance and admin roles, plus token protection on Windows, plus blocking device-code flow.
  - Response at every tier: on suspected compromise, revoke sessions (M365 "Revoke sessions"; Workspace "Sign out user") and reset the password, check inbox rules, forwarding, OAuth app grants and registered MFA methods. The K12 SIX compromised-account checklist from earlier notes covers this.
- Because finance staff are few (often 1-3 people), hardware keys (about $25-50 each, from general knowledge, unverified) for just those accounts is a high-return spend. Passkeys on phones are free.

### Gaps
- No public data on passkey or FIDO2 adoption at schools or nonprofits.
- Google Workspace edition requirements for enforcing security-key-only 2SV and for context-aware access were not verified in this session.
- I did not confirm whether the Sudbury attackers used an AiTM kit or a different MFA-relay method; the news report says only "intercepted MFA".

---

## 5. Payment-change controls: bank, payroll provider, callback; voice cloning; NACHA 2026; what tiny orgs can get

### Takeaway
The decisive control is procedural and free: no change to vendor or employee bank details on the strength of email, text or an inbound call alone. Verify by calling back a number already on file, use dual approval, and hold the first payment to new details. Banks offer ACH positive pay and debit blocks (about $20-75 a month per account) and payee-name account validation. Payroll platforms send change notifications to employees. NACHA's 2026 rule now obliges all business ACH originators to run risk-based fraud monitoring of credit-push entries. Voice cloning weakens "I recognized the voice" verification, so callbacks must go to known numbers and can use a pre-agreed code word.

### Cited Findings
**NACHA 2026 fraud-monitoring rule**
- Phase 1 took effect March 20, 2026 for ODFIs and for non-consumer originators, third-party service providers and third-party senders with 2023 ACH origination volume of 6 million or more (RDFIs at 10M+ for credit monitoring, per some sources). Phase 2 extends it to all remaining non-consumer originators with no volume threshold, formally June 19, 2026 and in practice June 22, 2026. It requires risk-based processes to monitor ACH credit entries for fraud, including false-pretenses and scam payments. It is a monitoring duty, not a shift of liability. — [Oscilar](https://oscilar.com/blog/nacha-2026-fraud-rules); [PaymentBrief](https://paymentbrief.com/articles/nacha-credit-push-fraud-rules-ach-operator-reference/); [Bottomline](https://www.bottomline.com/learning-center/2026-nacha-compliance-rules-risks-and-how-prepare); [Bravera Bank](https://www.bravera.bank/articles/2026-nacha-rule-updates-what-businesses-need-to-know); [JournalArta, Nov 2026](https://journalarta.com/en/2026/11/16/fintech-nacha-ach-fraud-rules-2026/)
- Secondary sources vary on thresholds; confirm against Nacha's rule text.

**Bank-side products**
- ACH positive pay typically costs about $20-50 a month per account, sometimes plus per-filter fees. Another source cites $30-75 a month with $100-500 setup. One bank lists $40 a month plus $0.25 per exception. ACH debit blocks and filters stop unauthorized debits. — [Melio](https://meliopayments.com/blog/enhancing-security-with-ach-positive-pay-for-businesses/); [DataPath](https://www.mydatapath.com/blog/ach-fraud-prevention-and-positive-pay-controls/); [ESL FCU](https://www.esl.org/business/commercial/cash-management/fraud-prevention-solutions/ach-positive-pay-debit-blocks); [Beancount, Jul 2026](https://beancount.io/blog/2026/07/09/positive-pay-bank-fraud-prevention-small-business)
- Account validation for new or changed account numbers (e.g. via Early Warning Services, which confirms an account exists and is open) is described mainly for eCheck and merchant risk, not for vendor bank-change verification. — [Ramp](https://ramp.com/blog/ach-verification-process); [Paycron on EWS](https://www.paycron.com/blog/breaking-down-early-warning-services-for-businesses-everything-you-need-to-know/)
- Guidance: call back vendors using a known-good number, never contact details from the change request, and pair this with dual approval. — [Melio](https://meliopayments.com/blog/enhancing-security-with-ach-positive-pay-for-businesses/); [Beancount](https://beancount.io/blog/2026/07/09/positive-pay-bank-fraud-prevention-small-business)

**Payroll providers**
- ADP's security organization (Oct 2021 alert) warned that criminals phish or call HR and payroll staff to change employees' bank details. ADP's employee flow sends a notice when direct-deposit details are added or changed, asking the employee to contact HR if they did not make the change. — [ADP security alert (2021)](https://www.adp.com/-/media/media/trust-center-alerts/2021/adp-gso-security-alert-cybercriminals-targeting-hr-and-payroll-practitioners-payroll-diversion-10222.pdf?rev=ee5db8978e7540fba968804ff6daa820); [ADP employee guide (2019)](https://www.royers.com/adp/employee/docs/directdeposit.pdf)
- No Paychex-specific documentation was found. General guidance: ask the provider what verification it applies, enable change notifications to the employee's email *and* phone, and disable admin-initiated direct-deposit changes where verified self-service exists. — [Vision Computers](https://www.visioncomputers.com/payroll-diversion-scam)
- Institutional patterns: UCPath emails employees on every direct-deposit change (Nov 2023). The University of Georgia's OneUSG (Nov 2025) added timestamped change emails, real-time third-party bank-account verification and blocks on accounts matching known fraud records. A Massachusetts retirement board (PERAC, Jul 2025) required verbal confirmation and re-verified recent changes after a diverted paycheck. — [UCLA/UCPath](https://cru.ucla.edu/news/ucpath-notice-direct-deposit-change-verification-emails); [UC Berkeley UCPath](https://ucpath.berkeley.edu/node/728); [UGA OneUSG](https://fyi.coe.uga.edu/2025-11-oneusg-connect-employee-self-service-fraud-prevention-features-effective-nov-15); [PERAC memo 22 (2025)](https://www.mass.gov/memorandum/perac-memo-22-fraud-alert)

**Voice cloning**
- FBI PSA I-051525-PSA (May 2025): actors impersonated senior US officials with AI-generated voice and text messages since April 2025. An update (reported as Dec 2025) says the activity dates to 2023. The FBI advises verifying new contacts via previously confirmed contact information. — [Cybersecurity Dive](https://www.cybersecuritydive.com/news/fbi-us-officials-impersonated-text-ai-voice/748334/); [CNBC](https://www.cnbc.com/2025/05/15/fbi-ai-us-officials-deepfake.html); [CyberScoop](https://cyberscoop.com/fbi-says-ongoing-deepfake-impersonation-of-us-officials-dates-back-to-2023/); [Malwarebytes](https://www.malwarebytes.com/blog/news/2025/05/scammers-are-using-ai-to-impersonate-senior-officials-warns-fbi)
- Earlier notes found no documented school case of AI-voice payment fraud (see `threat_landscape.md`).

### Inferences
- **Minimum viable payment-change control for a 1-3 person business office** (free):
  1. Any request to change bank details (vendor or employee) triggers a callback to the number in the vendor master file or HR record, never one from the email.
  2. A second person approves the change in the payroll or AP system.
  3. The first payment to new details is small or held 5 business days, with a confirmation call.
  4. Employees get automatic change notifications to a personal channel.
  5. A code word or passphrase is agreed in person with the top 10 vendors and the pastor, principal or treasurer, for verbal authorization of urgent wires. This beats voice recognition in the voice-clone era.
- **What tiny orgs can realistically get from banks**: most community banks and credit unions sell ACH debit block or filter and positive pay to small business accounts. Wire dual-authorization (initiator and approver tokens) is usually free within business online banking. Payee-name confirmation (e.g. account-owner matching) is increasingly offered through payment platforms (inference; see Gaps). Since Phase 2 (June 2026), a parish or school that originates ACH payroll is itself a "non-consumer originator" and should have a written fraud-monitoring process. A simple callback-and-dual-approval policy plus a review of new payees is plausibly sufficient for a tiny originator (inference; confirm with the ODFI).
- Many small schools run payroll through ADP, Paychex or Gusto, so the payroll processor, not the school, originates the ACH. The NACHA duty then falls on the processor, but the school's diocesan or HR-portal account remains the attack surface. Phishing-resistant MFA on payroll-admin logins matters as much as on email.

### Gaps
- No public pricing for payee-name account validation available to small business customers (e.g. EWS "Verify Payee" or similar) was found.
- No Paychex or Gusto documentation on direct-deposit change verification was found.
- Nacha's primary rule text was not retrieved; thresholds come from secondary sources that vary slightly.

---

## 6. Recovery: IC3 Recovery Asset Team, Financial Fraud Kill Chain success rates and time windows, and first-hour actions

### Takeaway
Speed is everything. In 2024 the IC3 Recovery Asset Team (RAT) froze $561.6M of $848.4M across 3,020 FFKC cases, a 66% success rate. In 2025 it froze about $679M of $1.16B across about 3,900 incidents, 58%. These rates apply only to cases reported quickly enough to enter the FFKC; the overall recovery rate for all BEC losses is far lower. First-hour actions: call your bank's fraud line to recall or freeze, file at ic3.gov with full transaction details, then contain the mailbox.

### Cited Findings
- IC3 2024: FFKC domestic, 2,651 complaints with $469.1M frozen; international, 369 complaints with $92.5M frozen; 66% success rate overall. RAT attempted recovery on 3,020 complaints representing $848.4M and froze $561.6M. — [IC3 2024 Annual Report (PDF)](https://www.ic3.gov/AnnualReport/Reports/2024_IC3Report.pdf); [TRM Labs](https://www.trmlabs.com/resources/blog/a-record-breaking-year-for-cybercrime-key-findings-from-the-fbis-2024-ic3-report)
- IC3 2025: about 3,900 incidents involving $1,163,919,846 in attempted theft; $679,013,183 frozen (split in the PDF as $507,042,623 and $171,970,560, likely domestic and international); 58% success rate. The majority of RAT-initiated FFKC incidents have historically been BEC, but tech-support and account-takeover cases rose in 2025. An IC3 brochure reportedly cites 61% for CY2025; this conflicts with the 58% figure, and I did not reconcile it. — [IC3 2025 Annual Report (PDF)](https://www.ic3.gov/AnnualReport/Reports/2025_IC3Report.pdf); [Wikipedia: IC3](https://en.wikipedia.org/wiki/Internet_Crime_Complaint_Center); [Alston & Bird](https://www.alstonprivacy.com/cybercrime-trends-to-watch-takeaways-from-the-fbis-2025-ic3-annual-report/)
- The FFKC numbers describe outcomes only for cases that reach the kill chain, not the baseline odds for every victim. — [LeadingIT, first 72 hours](https://goleadingit.com/blog/wire-transfer-fraud-recovery/)
- Domestic FFKC process brochure (criteria page): [IC3 D-FFKC brochure](https://www.ic3.gov/Outreach/Brochures/IC3-FFKC_Domestic.pdf). The brochure could not be fetched in this session, so its exact criteria (commonly cited as a wire of $50,000 or more reported within 72 hours) are **unverified here**.
- Coalition (from earlier notes) clawed back $31M for policyholders in 2024; 29% of BEC claims led to a fraudulent transfer. — [Coalition 2025 claims report](https://www.coalitioninc.com/blog/2025-cyber-claims-report)
- New Haven CT recovered $3.6M of more than $6M (2023). — [Insurance Journal](https://www.insurancejournal.com/news/east/2023/08/14/735130.htm)

### Inferences
- **First-hour runbook for a small org** (to be printed and taped up in the business office):
  1. Call the bank's fraud or treasury line, not the general branch line. Ask for a wire recall or SWIFT recall, or an ACH reversal, and for the bank to contact the receiving bank to freeze the funds. Get a case number.
  2. File at ic3.gov with the beneficiary bank, account number, amount, date and time, and the fraudulent email headers. Include the bank's case number. Call the local FBI field office if the amount is large.
  3. Notify the cyber insurer or broker before hiring vendors, since many policies require insurer-panel firms and early notice.
  4. Contain the mailbox: revoke sessions, reset the password, remove malicious inbox and forwarding rules, review OAuth grants, re-register MFA. Preserve logs (M365 unified audit log retention is short on basic tiers).
  5. Warn the impersonated vendor, other likely victims (parents, the diocese, sister schools) and payroll staff.
- Recovery odds drop with each day of delay. International beneficiary accounts and quick layering into crypto are the main reasons funds are lost. The 58-66% FFKC rates are a strong argument for "report within hours, not after an internal investigation". In the Sudbury case the district did not tell the town finance office, which is the opposite of this (inference from earlier notes).

### Gaps
- Exact current FFKC eligibility criteria (amount threshold, time window) were not verified from primary IC3 text, because ic3.gov was unreachable from this environment.
- No data on recovery rates specifically for small organizations or schools.
- The 61% (brochure) vs 58% (annual report) figures for CY2025 were not reconciled.

---

## 7. Tool extensions for `checkup`: MTA-STS, BIMI, own-domain lookalike detection, DMARC report parsing; value vs complexity

### Takeaway
Ranked by loss-reduction per unit of complexity: (1) sharper DMARC enforcement guidance (p=none, pct, sp=, rua present, subdomain policy) at near-zero cost; (2) a "payment-fraud readiness" non-DNS checklist output (callback, dual approval, passkeys for finance); (3) lookalike detection for the org's own domain *and* its top payees (registered + MX filter), at moderate cost; (4) DMARC aggregate-report parsing to get safely to p=reject, high value but high complexity and privacy considerations; (5) MTA-STS/TLS-RPT presence check, cheap but low loss impact; (6) BIMI, skip (needs enforcement plus a paid VMC/CMC, and adoption is 0.1-0.4%).

### Cited Findings
- MTA-STS adoption: about 0.6-0.7% of the top 1M domains (5,609 in 2025, up from 3,630 in 2024; about 0.7% in Jan 2026); 0.3% of 5.5M Tranco domains; 0.144% of 150M mail domains. Government and education lead in some countries (UK government near 40%; Swedish education about 6%). Among valid policies, roughly half are in enforce mode. — [Suped](https://www.suped.com/learn/dmarc/what-is-the-current-adoption-of-tls-reporting-with-mta-sts-for-domains); [dmarcguard](https://dmarcguard.io/research/email-authentication/); [DomainsProject](https://domainsproject.org/blog/a-state-of-txt); [PowerDMARC US report 2026](https://powerdmarc.com/united-states-dmarc-adoption-rates/); [PowerDMARC Sweden](https://powerdmarc.com/sweden-dmarc-report-2025/)
- BIMI adoption: 0.4% of 5.5M Tranco domains (20,518, of which 14,739 have valid SVG logos); 0.084% of 150M mail domains. — [dmarcguard](https://dmarcguard.io/research/email-authentication/); [DomainsProject](https://domainsproject.org/blog/a-state-of-txt)
- DMARC reporting (rua) is widely mismanaged (USENIX Sec '23), so a report-parsing feature must handle misdirected or absent reports and external-destination authorization records. — [USENIX Sec '23](https://www.usenix.org/conference/usenixsecurity23/presentation/ashiq)
- Free DMARC report tools exist (e.g. Red Sift's list of free DMARC checkers and analyzers). — [Red Sift free DMARC tools](https://redsift.com/guides/6-best-free-dmarc-tools)
- Current `checkup` scope (from repo README and code): DMARC record and policy, SPF (single record, ending, under 10 lookups), DKIM selectors for Google/M365, MX provider detection, HTTPS, certificate expiry, HSTS and redirect, and the CMS version banner. It explicitly limits network activity to DNS plus homepage requests. — `/home/user/security/checkup/README.md`, `/home/user/security/checkup/email_checks.py`

### Inferences
**Recommended additions, ranked**
1. **DMARC depth (low complexity, high value)**: flag `p=none` older than about 90 days as "monitoring only, not protecting"; flag `pct<100`; check `sp=` and whether parked or unused subdomains are protected; flag a missing `rua` (no visibility, so the org can never safely enforce); flag `rua` pointing at an external domain without the `_report._dmarc` authorization record. Add a **non-sending (parked) domain** profile: `v=spf1 -all`, `p=reject`, null MX (`MX 0 .`). Parishes and schools often own old domains (e.g. a former school name) that are prime spoofing targets. All of this is pure DNS, which fits checkup's privacy promise.
2. **Payment-fraud readiness section (zero network, high value)**: DNS can't see the controls that stop the losses (callback, dual approval, passkeys, bank positive pay). An optional `--questions` mode or a printed checklist in the report ("these five controls stop most money loss") would put the most important advice where it will be read. Low engineering cost.
3. **Lookalike detection (moderate complexity)**: generate dnstwist-style permutations (or vendor dnstwist as an optional dependency) and resolve only MX/A for each, which keeps network use DNS-only. Report "registered with mail servers". Optionally query crt.sh for recent certificates (an extra third-party request, so it should be opt-in under the README's network promise). Add a `--payees vendors.txt` mode to check the org's top vendors' domains for lookalikes too. Main risks: noise for generic names (St. Mary's, Trinity, Holy Cross), and hundreds of DNS queries per run. Mitigate with registered+MX filtering, a cap on permutations, and "review" wording rather than "attack".
4. **DMARC aggregate-report parsing (high complexity)**: parse rua XML (zip/gzip) to list which services send as the domain and whether they pass aligned SPF or DKIM, then tell the user when it is safe to move to quarantine or reject. Very valuable for the p=none to p=reject journey, but it needs a mailbox to receive reports and must handle personal data (source IPs) locally. Run it as a separate offline subcommand (`checkup dmarc-report file.xml.gz`) that never uploads anything. Alternatively, point users to a free hosted analyzer, with privacy caveats.
5. **MTA-STS / TLS-RPT presence (low complexity, low fraud impact)**: informational only. It protects against TLS downgrade on inbound mail, not impersonation. Google Workspace and M365 support it, but adoption is under 1%, and it adds hosting work (a policy file over HTTPS at `mta-sts.` subdomain). Report as "optional / advanced", not as a failure.
6. **BIMI (skip, or info only)**: requires p=quarantine/reject plus, for Gmail's checkmark, a paid VMC or CMC certificate (hundreds to over a thousand dollars a year, from general knowledge, unverified) and often a trademark. Negligible fraud reduction for tiny orgs. At most mention it as "possible once DMARC is enforced".
7. **Mailbox-provider posture hints (no network)**: when MX shows M365 or Google, print provider-specific steps: M365 Standard preset (first-contact tip), external tagging, a disabled-SMTP-AUTH check (not visible from DNS); Workspace lookalike-domain protection, external recipient warning, and passkeys for finance users.

**Measurement method for the project**: a DNS-only aggregate scan of a public list of private, Catholic and K-12 school domains (from NCES PSS/CCD websites or diocesan directories) would produce the first sector-specific DMARC/SPF/MTA-STS baseline. Publish only aggregate rates, consistent with the README's "don't commit reports about real organizations".

### Gaps
- No public evaluation of how much any single DNS control (vs process controls) reduces BEC losses for small orgs; the ranking is reasoned, not measured.
- Current VMC/CMC pricing and Gmail BIMI requirements were not verified in this session.
- crt.sh terms of use and rate limits for automated querying were not verified.
