# Identity and Cloud-Tenant Security for Very Small Child-Serving Organizations (Google Workspace and Microsoft 365)

Scope: parish and classical schools, childcare centers, youth nonprofits and small NYC providers that have no IT staff. Written from the point of view of a cloud identity security engineer. Research date: Nov 2026. This builds on the findings in `Kids data defense research tree/threat_landscape.md` and `economics_insurance_funding.md`, which covered Sudbury AiTM payroll fraud, CIS "account takeover hopping", the end of the Microsoft Business Premium grant, and the K12 SIX compromised-account checklist. Those points are not repeated here except as anchors.

Method note: many fetches of news sites were blocked from this session (helpnetsecurity.com and update.dsesecurity.com did not resolve). The CISA ScubaGoggles and ScubaGear repositories were shallow-cloned from GitHub on 2026-11-23, and the claims below about their scopes, roles, limitations and baselines come from reading those files directly. File paths are cited as GitHub URLs.

---

## 1. Current attack techniques against Workspace and M365 tenants (2024-2026), and which hit education and nonprofits

### Takeaway
Identity is the attack surface. Education is a top target for identity attacks. Microsoft says "research and academia" accounted for 39% of identity compromise incidents it observed in H1 2025. Proofpoint attributes most Tycoon 2FA campaigns to education lures. The techniques that matter for a 15-seat tenant are:
1. AiTM phishing kits that steal session cookies and so beat push, SMS and TOTP MFA.
2. OAuth consent phishing and fake apps.
3. Device-code phishing, which uses no malicious link at all.
4. Password spray against weak or legacy authentication.
5. Abuse of Google's own services (Classroom, Forms, Apps Script) to deliver lures that pass filters.

Partner/GDAP abuse and Google domain-wide delegation (DWD) abuse are real but are tail risks for small organizations. They matter mainly when an MSP or a former volunteer "IT person" holds standing access.

### Cited Findings
**AiTM phishing-as-a-service (PhaaS)**
- Tycoon 2FA (operator tracked as Storm-1747) used AiTM to capture credentials and session tokens, which let attackers bypass MFA for Microsoft 365 and Gmail. Microsoft, Europol and partners disrupted it in March 2026, and Microsoft seized 330 domains under a US court order. — [Microsoft On the Issues, 2026-03-04](https://blogs.microsoft.com/on-the-issues/2026/03/04/how-a-global-coalition-disrupted-tycoon/); [The Hacker News](https://thehackernews.com/2026/03/europol-led-operation-takes-down-tycoon.html)
- Microsoft says Tycoon 2FA was linked to about 62% of the phishing attempts it blocked by mid-2025, and that healthcare and education were hit hardest. It says the kit enabled access to almost 100,000 organizations, including schools and nonprofits. In New York alone, six municipal schools and three universities faced attempted or successful compromise. These are vendor-reported figures. — [Microsoft On the Issues](https://blogs.microsoft.com/on-the-issues/2026/03/04/how-a-global-coalition-disrupted-tycoon/); [CyberScoop](https://cyberscoop.com/tycoon-2fa-phishing-kit-takedown-microsoft/)
- Proofpoint saw Tycoon 2FA distributed from compromised accounts in many sectors, including education. A Proofpoint vertical breakdown lists Education at 75% of Tycoon 2FA campaigns; the search snippet did not explain the metric. — [Proofpoint](https://www.proofpoint.com/us/blog/threat-insight/disruption-targets-tycoon-2fa-popular-aitm-phaas)
- Barracuda counted more than 1 million PhaaS attacks in Jan-Feb 2025. In January, Tycoon 2FA was 89% of detected PhaaS incidents, EvilProxy 8% and Sneaky 2FA 3%. — [Barracuda, 2025-03-19](https://blog.barracuda.com/2025/03/19/threat-spotlight-phishing-as-a-service-fast-evolving-threat)
- Barracuda's year-end review says the number of known phishing kits doubled during 2025, and that Mamba 2FA surged in late 2025 to close to 10 million attacks. — [Barracuda, 2026-01-07](https://blog.barracuda.com/2026/01/07/threat-spotlight-phishing-kits-evolved-2025)
- Sekoia ranked the most widespread AiTM kits for Jan-Apr 2025 as Tycoon 2FA, Storm-1167, NakedPages, Sneaky 2FA, EvilProxy and Evilginx. — [Infosecurity Magazine summarizing Sekoia](https://www.infosecurity-magazine.com/news/sneaky-2fa-joins-tycoon-2fa/)
- In late 2025, Sneaky 2FA added fake browser-in-the-browser sign-in windows. — [Malwarebytes, Nov 2025](https://www.malwarebytes.com/pt/blog/news/2025/11/attackers-are-using-sneaky-2fa-to-create-fake-sign-in-windows-that-look-real)

**OAuth consent phishing and malicious apps**
- Proofpoint documented fake Microsoft 365 OAuth apps impersonating RingCentral, SharePoint, Adobe and DocuSign that led to MFA phishing. RH-ISAC reports Proofpoint saw attempted compromises of about 3,000 accounts in more than 900 M365 environments, with a confirmed success rate above 50% since early 2025. — [Proofpoint](https://www.proofpoint.com/us/blog/threat-insight/microsoft-oauth-app-impersonation-campaign-leads-mfa-phishing); [RH-ISAC](https://rhisac.org/threat-intelligence/microsoft-oauth-app-impersonation-leads-to-mfa-phishing/)
- Wiz separately found 19 malicious OAuth apps in early 2025 impersonating Adobe, DocuSign and OneDrive. — [Wiz](https://www.wiz.io/blog/detecting-malicious-oauth-applications)
- A March 2025 wave of apps impersonating Adobe and DocuSign requested only "low-risk" scopes (profile, email, openid) to avoid scrutiny. This matters because some consent policies auto-allow low-risk scopes. — [SC World](https://www.scworld.com/brief/microsoft-365-credentials-subjected-to-malicious-oauth-app-attack)

**Device-code phishing**
- Storm-2372, active since August 2024 and assessed by Microsoft as aligned with Russian interests, used fake Teams-invite lures. Victims typed an attacker-generated code into the genuine Microsoft sign-in page, which handed tokens to the attacker. The attacker then read mail via Graph and phished colleagues from the compromised account. Targets included NGOs and education. Microsoft recommends blocking device code flow with Conditional Access and revoking refresh tokens. — [Microsoft Security Blog, 2025-02-13](https://www.microsoft.com/en-us/security/blog/2025/02/13/storm-2372-conducts-device-code-phishing-campaign/); [H-ISAC bulletin](https://www.aha.org/h-isac-white-reports/2025-02-14-h-isac-tlp-white-threat-bulletin-storm-2372-conducts-device-code-phishing-campaign)
- Secondary sources say a 2026 surge in device-code phishing came from a PhaaS kit called "EvilTokens", and that Microsoft folded Storm-2372 into Midnight Blizzard. Neither claim is confirmed by a Microsoft primary source. — [Flamingo](https://www.flamingo.run/blog/device-code-phishing); [Mjolnir](https://intel.mjolnirsecurity.com/storm-2372-device-code-phishing)

**Password spray and legacy auth**
- MDDR 2025 says more than 97% of identity attacks are password spray or brute force. Identity attacks rose 32% in H1 2025, and research and academia accounted for 39% of identity compromise incidents. The 39% figure comes from a mirrored copy of the PDF. — [Microsoft MDDR 2025 PDF](https://cdn-dynmedia-1.microsoft.com/is/content/microsoftcorp/microsoft/msc/documents/presentations/CSR/Microsoft-Digital-Defense-Report-2025.pdf); [mirror](https://downloads.uth.gr/synodos110/pre167.pdf); [Microsoft On the Issues](https://blogs.microsoft.com/on-the-issues/2025/10/16/mddr-2025/)
- Microsoft's secure-by-default change, MC1097272, rolled out mid-July to August 2025. It blocked legacy browser auth to SharePoint/OneDrive and FrontPage RPC, and set Microsoft-managed consent policies so that users cannot consent to third-party apps accessing files and sites. It applied to all tenants with no extra licensing. Tenants that already had custom consent settings were not changed. A further Exchange/Teams API change followed in Oct-Nov 2025. — [mc.merill.net MC1097272](https://mc.merill.net/message/MC1097272); [Petri](https://petri.com/microsoft-365-block-legacy-authentication/); [The Register](https://www.theregister.com/2025/06/19/the_microsoft_axeman_is_coming/)

**Abuse of Google education services**
- Check Point: between 6 and 12 Aug 2025, attackers sent more than 115,000 phishing emails to about 13,500 organizations, in five waves. They built fake classrooms whose invitations came from the real no-reply@classroom.google.com. — [Check Point](https://blog.checkpoint.com/email-security/phishing-in-the-classroom-115000-emails-exploit-google-classroom-to-target-13500-organizations/)
- Google/Mandiant observed malicious Google Forms imitating university communications sent to at least 15 universities. Hijacked staff accounts were then used to send "job application" Forms to students. — [Google Cloud Threat Intelligence](https://cloud.google.com/blog/topics/threat-intelligence/phishing-targeting-higher-education)
- (Prior research) A stale student Google account plus Apps Script phish was used against a district. — see threat_landscape.md; [IronScales](https://ironscales.com/threat-intelligence/student-google-account-apps-script-credential-phish)

**Google domain-wide delegation (DWD)**
- Unit 42: any GCP identity able to mint tokens for a DWD-enabled service account can impersonate any Workspace user within the delegated scopes. This includes a developer with project Editor rights, or the Compute Engine default service account, which has Editor by default. Full investigation needs both GCP and Workspace logs. — [Unit 42](https://unit42.paloaltonetworks.com/critical-risk-in-google-workspace-delegation-feature/)
- Hunters' "DeleFriend": DWD is bound to the service account's OAuth client ID, not to a specific key, so anyone who can create a new key inherits the delegation. — [Dark Reading](https://www.darkreading.com/cloud-security/vendor-claims-design-flaw-in-google-workspace-is-putting-organizations-at-risk)
- **Directly relevant to the project:** ScubaGoggles' own service-account mode *requires* creating a DWD grant and a JSON key file. Its docs say to store the key "somewhere it won't be inadvertently deleted or accessed by unauthorized entities." — [ScubaGoggles ServiceAccount.md](https://github.com/cisagov/ScubaGoggles/blob/main/docs/authentication/ServiceAccount.md)

**MSP / partner access (GDAP/DAP)**
- Microsoft (Mar 2025): Silk Typhoon shifted in late 2024 to IT service providers and cloud solution providers. It abused stolen API keys, delegated admin privileges and multi-tenant apps to exfiltrate mail, OneDrive and SharePoint data from downstream customers via Graph, and also used password spray. — [Microsoft Security Blog 2025-03-05](https://www.microsoft.com/en-us/security/blog/2025/03/05/silk-typhoon-targeting-it-supply-chain/)
- CrowdStrike tracks the same cluster as MURKY PANDA and documented compromise of a Microsoft CSP used to reach downstream tenants (Aug 2025). — [CrowdStrike](https://www.crowdstrike.com/en-us/blog/murky-panda-trusted-relationship-threat-in-cloud/); [BleepingComputer](https://www.bleepingcomputer.com/news/security/murky-panda-hackers-exploit-cloud-trust-to-hack-downstream-customers/?web_view=true)

### Inferences
- For these organizations the realistic kill chain is:
  1. A lure from a peer school or vendor that is already compromised, or a Classroom/Forms/DocuSign-style lure.
  2. AiTM, consent or device-code capture of a session.
  3. Mailbox rules and forwarding, OAuth persistence and internal phishing.
  4. Payroll or vendor bank-change fraud.

  A posture check should be weighted toward steps 2 and 3. Step 4 is stopped by process (callback verification), not by tenant configuration.
- "MFA enabled" is not a pass. A checker should report MFA strength: phishing-resistant, app/TOTP, or SMS/voice. It should also report whether device-code flow, user consent and legacy auth are closed.
- The Tycoon takedown (Mar 2026) does not reduce the risk. Barracuda's data shows kit count doubling and Mamba 2FA filling the gap.
- Small Google tenants that use a GCP project for one script, such as an Apps Script add-on or a volunteer's sync, may hold forgotten DWD grants with broad scopes. These are invisible to staff and are a high-value find for a checker.

### Gaps
- No source quantifies AiTM, consent or device-code incidents specifically for K-12 private schools, childcare or youth nonprofits. Sector figures are higher-ed- or "education"-wide and vendor-reported.
- Could not retrieve a primary Microsoft or Google statement on EvilTokens or on 2026 device-code volume.
- No public case found of GDAP abuse against a small nonprofit or school tenant specifically.

---

## 2. CISA SCuBA: ScubaGoggles (Google Workspace) and ScubaGear (M365)

### Takeaway
Both tools are mature and free. Both assume enterprise/federal licensing (GWS Enterprise Plus / Education Plus; M365 E3/G3 + E5/G5), so on a Business Basic, Education Fundamentals or Nonprofits tenant they will report many "failures" that the organization cannot fix without buying licenses. Both also demand more privilege than a "read-only" pitch suggests. ScubaGoggles needs a **Super Admin** user, or a DWD service account. ScubaGear is **Windows/PowerShell 5 only**, and its non-interactive SharePoint check needs `Sites.FullControl.All`. Both are usable by a non-expert only with hand-holding. The project should wrap them or reimplement a subset, not hand them over raw.

### Cited Findings
**ScubaGoggles**
- Version **1.1.0** per `scubagoggles/__init__.py`; last commit 2026-11-16. A secondary report says CISA released ScubaGoggles v1.1.0 and ScubaGear v2.0 in Oct 2026, with a new "assured controls" baseline. — [ScubaGoggles repo](https://github.com/cisagov/ScubaGoggles); [Help Net Security 2026-10-28](https://www.helpnetsecurity.com/2026/10/28/cisa-scubagear-scubagoggles-update/)
- Pipeline: export settings and logs to JSON via the Admin SDK, Cloud Identity Policy API and others; verify with OPA Rego; report as HTML and JSON. Installed from PyPI. — [README](https://github.com/cisagov/ScubaGoggles)
- Auth: "ScubaGoggles requires the user to have Super Admin role." OAuth scopes are all `.readonly` (Reports audit, Directory domain/group/orgunit/user/rolemanagement/customer, cloud-identity.policies.readonly, inboundsso.readonly) **plus** `apps.licensing` and `apps.groups.settings`, which are not read-only scopes. The docs say the Groups Settings API "does not natively support a read-only API scope," so CISA works around it with a Groups Reader admin role via Delegated Admin Service Account. The user must also create a GCP project and enable four APIs: Admin SDK, Groups Settings, Cloud Identity, Enterprise License Manager. — [Prerequisites.md](https://github.com/cisagov/ScubaGoggles/blob/main/docs/prerequisites/Prerequisites.md)
- Service-account mode requires DWD, a downloaded JSON key, a custom "License Read" admin role, the Groups Reader role and `--subjectemail` of an admin. That is about 30 console steps. — [ServiceAccount.md](https://github.com/cisagov/ScubaGoggles/blob/main/docs/authentication/ServiceAccount.md)
- **Log-based checks are unreliable.** Settings not exposed by the Policy API are inferred from Admin audit log events. The tool cannot see a setting that was never changed from default. Admin logs are kept only 6 months. For custom OUs with no event, it assumes inheritance, and false negatives are possible. CISA says to view such results "with a healthy degree of skepticism." — [Limitations.md](https://github.com/cisagov/ScubaGoggles/blob/main/docs/usage/Limitations.md)
- Known issue: SPF/DKIM/DMARC checks (GWS.GMAIL.2-4) may fail even when DNS records exist. — [README troubleshooting](https://github.com/cisagov/ScubaGoggles)
- Baselines: Common Controls, Gmail, Calendar, Chat, Classroom, Drive, Meet, Sites, Groups, Gemini, Assured Controls. Every baseline except Classroom states "This document assumes the organization is using GWS Enterprise Plus." Classroom assumes **Education Plus**. — [baselines directory](https://github.com/cisagov/ScubaGoggles/tree/main/scubagoggles/baselines)
- Common Controls highlights:
  - 1.1 phishing-resistant MFA SHALL be required for all users; 1.3 SMS/voice SHALL NOT be used.
  - 6.2 requires 2-8 super admins.
  - 10.1-10.5 OAuth app access control: restrict third-party access to all services, no user consent to low-risk scopes, do not trust unconfigured internal apps, block unconfigured third-party apps, block less-secure apps.
  - 11.1 approved Marketplace apps only.
  - 14.2 logs retained ≥3 months searchable / ≥12 months retrievable.
  - 17.1 multi-party approval for sensitive admin actions.
  - 18 DLP.

  — [commoncontrols.md](https://github.com/cisagov/ScubaGoggles/blob/main/scubagoggles/baselines/commoncontrols.md)
- Classroom baseline:
  - 1.1/1.2: joins limited to allowlisted domains.
  - 2.1: users SHOULD NOT authorize apps to Classroom data.
  - 3.1: Clever roster import off.
  - 4.1: only teachers unenroll students.
  - 5.1: class creation limited to verified teachers.

  Restricting class creation and joins directly addresses the Aug 2025 fake-classroom campaign. — [classroom.md](https://github.com/cisagov/ScubaGoggles/blob/main/scubagoggles/baselines/classroom.md)
- The Common Controls baseline notes that Google DLP is available in Education Fundamentals, Standard, Teaching & Learning Upgrade and Plus, among others. — [commoncontrols.md §18](https://github.com/cisagov/ScubaGoggles/blob/main/scubagoggles/baselines/commoncontrols.md)
- Under BOD 25-01, federal agencies must run ScubaGoggles/ScubaGear on in-scope tenants. A secondary guide says that as of May 2025 only the M365 baselines were "final" and the GWS baselines were draft. — [CISA BOD 25-01 guidance](https://www.cisa.gov/news-events/directives/bod-25-01-implementation-guidance-implementing-secure-practices-cloud-services); [nhimg guide](https://nhimg.org/cisa-scuba-baselines-guide)

**ScubaGear**
- Version **2.0.0** (`ScubaGear.psd1`); last commit 2026-11-20. It covers Entra ID, "Security Suite" (formerly Defender), Exchange Online, Power BI, Power Platform, SharePoint and Teams, with a "Super Intelligence" baseline in development. Output is HTML, JSON and CSV. — [ScubaGear repo](https://github.com/cisagov/ScubaGear)
- "At least one of these libraries is tied to PowerShell 5 … ScubaGear will only run on Windows." `Install-ScubaDependencies` installs modules, OPA and MSAL. — [docs/prerequisites/dependencies.md](https://github.com/cisagov/ScubaGear/tree/main/docs/prerequisites)
- Interactive roles: Global Reader is enough for Entra, Security Suite, Exchange, SharePoint and Teams. Power BI needs Fabric Administrator plus a Power BI/Fabric license. Power Platform needs Power Platform Admin plus a license. Non-interactive (service principal) SharePoint requires **`Sites.FullControl.All`**, which is far from read-only. Setting up the service principal itself needs Application Administrator or Privileged Role Administrator. — [permissions docs](https://github.com/cisagov/ScubaGear/tree/main/docs/prerequisites)
- License assumption: "tested against tenants that have an M365 E3 or G3 and E5 or G5 license bundle. It may still function for tenants that do not have one of these bundles." Some checks rely on Entra ID P2 and Defender for Office 365 P1/P2. Controls met with third-party tools can be omitted through config. — [docs/misc/assumptions.md](https://github.com/cisagov/ScubaGear/blob/main/docs/misc/assumptions.md)
- Entra baseline policies MS.AAD.7.4-7.9 (PIM-style privileged access) require Entra ID P2. Several policies are evaluated as Conditional Access policies. In the cloned baseline (`aad.md`) and Rego, the string "security defaults" does not occur, so tenants that rely on Security Defaults rather than CA, which is the normal Business Basic setup, are not modeled as compliant. — [aad.md](https://github.com/cisagov/ScubaGear/blob/main/PowerShell/ScubaGear/baselines/aad.md) (my grep of the cloned repo, 2026-11-23)

### Inferences
- **Fit for small tenants is poor out of the box.** A Business Basic tenant using Security Defaults, or an Education Fundamentals/Nonprofits Workspace tenant, will see a wall of red, much of it license-gated: CA, PIM, context-aware access, SIEM export, multi-party approval. That is demoralizing and not actionable. The project should keep a "license-aware profile" that marks each SCuBA control as *achievable on your tier / needs upgrade / not applicable*.
- Requiring a Super Admin or Global Reader to run a third-party tool is acceptable only if the tool runs locally and stores nothing off-device. That should be the design invariant (see §6).
- ScubaGoggles' OAuth mode is safer for this audience than service-account mode. Creating a DWD key would itself add the exact risk described in §1. The project's docs should steer users to OAuth with a short-lived token and tell them to delete the GCP OAuth client afterwards.
- ScubaGear being Windows-only matters. Many small-org admins use Macs or Chromebooks. A cross-platform alternative (Maester is PowerShell 7 and cross-platform) or a Graph-only reimplementation may be needed for M365.

### Gaps
- Could not fetch the official release notes or dates for ScubaGoggles 1.1.0 / ScubaGear 2.0.0 (only secondary confirmation).
- No published usability study of SCuBA tools by non-experts was found.
- Did not verify whether ScubaGear's Rego emits "N/A / license" rather than "Fail" for Business Basic/Premium SKUs across all products. Only the AAD license-warning helpers were seen (`ReportDetailsArrayLicenseWarning`, `Aad2P2Licenses`).

---

## 3. What each license tier offers (security-relevant), 2025-2026

### Takeaway
The free tiers (Workspace Education Fundamentals, Workspace for Nonprofits, M365 Business Basic for nonprofits) include enough to stop most account takeover if configured:
- MFA/2SV and passkeys
- Security Defaults / app access control
- an alert center
- 6-month (Google) or 180-day (M365) audit logs

What they lack is Conditional Access (M365), premium investigation and remediation (Google), long log retention and DLP depth. For a small org the biggest tier-gated loss is **Conditional Access on M365**, which needs Business Premium or Entra P1. That is what allows blocking device-code flow, requiring compliant devices and scoping MFA strength.

### Cited Findings
**Google Workspace for Education**
- Official comparison: the alert center and audit and investigation tool (log events) are in **all three** editions (Fundamentals, Standard, Plus). Exporting logs to Google Security Operations, and the full **security investigation tool** (acting on results, activity rules, saved investigations), are Standard and Plus only. Email/chat retention rules are in all. — [Compare Education editions](https://knowledge.workspace.google.com/admin/getting-started/editions/compare-education-editions)
- A third-party blog says the investigation tool is Plus-only, which conflicts with Google's table showing Standard. Use Google's table. — [Dito](https://www.ditoweb.com/2025/06/google-workspace-security-investigation-tool-your-top-questions-answered/)
- Classroom log events in the investigation tool require Education Standard or Plus. — [Classroom log events](https://knowledge.workspace.google.com/admin/reports/classroom-log-events)
- Admin audit logs are retained 6 months (CISA cites Google's data-retention page). — [ScubaGoggles Limitations.md](https://github.com/cisagov/ScubaGoggles/blob/main/docs/usage/Limitations.md); [Google data retention](https://support.google.com/a/answer/7061566)
- DLP is available in Education Fundamentals, Standard, T&L Upgrade and Plus. — [ScubaGoggles commoncontrols.md](https://github.com/cisagov/ScubaGoggles/blob/main/scubagoggles/baselines/commoncontrols.md)
- Education-only: users designated as **under 18** are blocked by default from unconfigured third-party apps. They can request access, and admins can allow apps that need only basic profile sign-in. Admins set apps to Trusted, Limited, Specific Google data, or Blocked. Pending requests drop off after 6 months. — [Google Help 13288950](https://support.google.com/a/answer/13288950); [Workspace Updates 2023-08](https://workspaceupdates.googleblog.com/2023/08/third-party-app-access-enhancements-for-google-workspace-edu.html?m=0)

**Google Workspace for Nonprofits**
- The free Nonprofits edition is available. Discounts: Business Standard 75%+ off, Business Plus 72%+ off, Enterprise 70%+ off, sold only direct from Google, not via resellers. Listed US prices are about $3.50 (Business Standard) and $6.16 (Business Plus) per user per month on an annual plan; Google pages disagree. The 2,000-user cap applies to Nonprofits/Business discounts. Vault appears only in paid tiers; 2SV appears in all. — [Google Admin Help nonprofits](https://knowledge.workspace.google.com/admin/billing/compare-google-workspace-features-for-nonprofits); [Google Nonprofits compare](https://www.google.com/nonprofits/workspace/compare/); [support.google.com/nonprofits/answer/15503706](https://support.google.com/nonprofits/answer/15503706)

**Microsoft 365**
- Audit (Standard) keeps logs **180 days** for records generated on or after 2023-10-17 and is enabled by default. Audit (Premium) keeps Entra, Exchange, OneDrive and SharePoint records for 1 year and comes with E5 / E5 Compliance. — [Microsoft Learn: Audit solutions](https://learn.microsoft.com/purview/audit-solutions-overview); [Audit Premium](https://learn.microsoft.com/en-us/purview/audit-premium)
- A Microsoft Q&A answer says Business Basic lacks advanced audit events such as MailItemsAccessed and extended retention. A community answer claims audit is off by default on Business Basic, which contradicts Microsoft docs. Verify per tenant. — [Microsoft Q&A](https://learn.microsoft.com/en-us/answers/questions/5096209/audit-log-availability)
- Nonprofit grants (prior research): the free Business Premium (10 seats) and E1 grants ended at the first renewal after 2025-07-01. They were replaced by free Business Basic (up to 300 users) and about 75% off Business Premium. — see economics_insurance_funding.md
- MC1097272 secure-by-default changes (legacy auth block, admin consent for third-party file/site access) applied to all tenants with no extra licensing. — [mc.merill.net](https://mc.merill.net/message/MC1097272)
- ScubaGear's Entra privileged-access controls need P2 (E5). — [aad.md](https://github.com/cisagov/ScubaGear/blob/main/PowerShell/ScubaGear/baselines/aad.md)

### Inferences
- Tier matrix for a checker to encode. ✓ = included, ✗ = not included, ? = unverified:

| Capability | GWS Edu Fundamentals / Nonprofits (free) | GWS Edu Standard/Plus or Business/Enterprise paid | M365 Business Basic (free NP) | M365 Business Premium (~75% off NP) |
|---|---|---|---|---|
| Enforce 2SV/MFA | ✓ | ✓ | ✓ (Security Defaults; per-user MFA) | ✓ + Conditional Access |
| Phishing-resistant enforcement (keys/passkeys) | ✓ ("only security key" option; see §4) | ✓ | ? Authentication-methods policy is free; *enforcing* strength per app needs CA (P1) | ✓ CA auth strengths |
| Block device-code flow | n/a | n/a | ✗ (no CA) | ✓ CA auth-flows |
| Alert center / alerts | ✓ | ✓ (+ investigation tool, activity rules) | Basic alert policies | + Defender for Business, Defender for Office P1 |
| Audit log retention | ~6 months admin logs | same + export to SecOps | 180 days | 180 days (Premium audit = E5) |
| OAuth/third-party app control | ✓ App access control; Edu under-18 default block | ✓ | ✓ user-consent settings (now default admin consent for files/sites) | ✓ + app governance? (unverified) |
| DLP | ✓ (Edu); paid only for NP Business? (unverified) | ✓ | ✗ | ✓ Purview DLP |
| Vault / retention | Edu: ✓; NP free: ✗ | ✓ | Basic retention? (unverified) | ✓ |

- The single most valuable upgrade conversation for M365 is Business Premium, at about $5.50/user/month for nonprofits based on the 75% discount (inferred; not sourced in this session). It is justified by CA (block device code, legacy auth, require phishing-resistant MFA for admins) and Defender for Office (Safe Links against AiTM links).
- On Google, Education Fundamentals already has most posture controls. The tier gap is mainly the investigation/remediation tool and Classroom log visibility.

### Gaps
- Could not verify the Google "Security health page" tier availability or context-aware access tiers. CAA is commonly Enterprise / Education Standard+ but this was not confirmed this session.
- Could not confirm whether Google Workspace for Nonprofits (free) includes DLP or the alert center. The extracted table was incomplete.
- Could not confirm Entra Free sign-in log retention, or whether Graph `signInActivity` (last sign-in) requires Entra ID P1. I believe it does, which would block a stale-account check on Business Basic; this needs testing.

---

## 4. Passkeys and phishing-resistant MFA feasibility for small orgs in 2026; SMS risks

### Takeaway
2026 is the year this became feasible by default. Microsoft is making passkeys the default Entra method and is retiring Microsoft-delivered SMS/voice MFA by **1 Feb 2027**. Google lets admins enforce "security key only," which also accepts passkeys, at OU level on any edition. For a 10-30 person organization:
- Enforce passkeys or hardware keys on admins and finance/payroll first.
- Use synced passkeys or the Authenticator app for everyone else.

Caveat: passkeys stop AiTM only if weaker fallbacks are disabled. Users who can still choose SMS or TOTP can be downgraded by a phishing kit.

### Cited Findings
- Microsoft (2026-07-13): passkeys become the default authentication method in Entra ID, and Microsoft steps back from native telecom SMS/voice. — [Microsoft Security Blog](https://microsoft.com/en-us/security/blog/2026/07/13/microsoft-entra-id-security-updates-passkeys-are-the-default-authentication-method-in-entra-id/); [Redmond Mag](https://redmondmag.com/articles/2026/07/14/microsoft-makes-passkeys-the-entra-id-default-as-identity-attacks-grow-stealthier.aspx)
- Forrester: Microsoft-provided SMS and voice are fully retired on **1 Feb 2027**. Every user must be on a phishing-resistant method (passkeys, Windows Hello, FIDO2) before then. — [Forrester](https://www.forrester.com/blogs/microsoft-makes-passkeys-default-what-identity-and-security-leaders-need-to-do/)
- Rollout start dates conflict: 1 Sep 2026 per BleepingComputer/ITPro, versus a podcast claiming passkey profiles would be auto-enabled in March 2026. — [BleepingComputer](https://www.bleepingcomputer.com/news/microsoft/microsoft-entra-id-gets-passkeys-default-authentication-starting-september/); [ITPro](https://www.itpro.com/security/microsoft-entra-id-passkey-default-authentication-dealine-september-2026)
- Passkey profiles (per-group rules, up to 10 per tenant) are GA. Device-bound options: Authenticator passkeys, Entra passkey on Windows, FIDO2 keys. — [Microsoft World Passkey Day 2026](https://www.microsoft.com/en-us/security/blog/2026/05/07/world-passkey-day-advancing-passwordless-authentication/); [Yubico](https://www.yubico.com/blog/rip-sms-microsoft-transitioning-to-passkeys-as-default-authentication-method-for-entra-id/)
- Google: the "Only security key" 2SV enforcement option accepts passkeys and physical keys alike. Google enforces 2SV on admin accounts. The "skip passwords" setting does not by itself enforce 2SV. Enroll users before enforcing, or they are locked out. These come from third-party guides; no Google primary page was retrieved. — [nhimg guide](https://nhimg.org/google-workspace-2sv-and-passkey-enforcement-guide); [GAT Labs](https://gatlabs.com/blogpost/google-workspace-multi-factor-authentication/)
- CISA's GWS baseline: phishing-resistant MFA SHALL be required for all users (1.1); SMS or voice SHALL NOT be used (1.3); new-user enrollment window 1 day to 1 week (1.4). — [commoncontrols.md](https://github.com/cisagov/ScubaGoggles/blob/main/scubagoggles/baselines/commoncontrols.md)
- MDDR 2025: phishing-resistant MFA prevents up to 99% of identity attacks (Microsoft claim). — [Microsoft On the Issues](https://blogs.microsoft.com/on-the-issues/2025/10/16/mddr-2025/)
- Sudbury 2025 shows push/code MFA intercepted in real time (prior research). — see threat_landscape.md

### Inferences
- Practical 2026 recipe for a no-IT org:
  1. Two FIDO2 keys for each admin (primary plus backup, stored at the rectory or office safe).
  2. Synced passkeys on phones for staff.
  3. Disable SMS/voice.
  4. On M365 Business Basic, use the authentication-methods policy (free) to remove SMS/voice and enable passkeys, accepting that per-app strength cannot be enforced without CA.
- Main operational risk is lockout and recovery. Small organizations need two super admins (CISA requires 2-8) and a documented break-glass procedure, or a passkey rollout becomes an outage.
- Childcare and front-desk staff often share devices. Device-bound passkeys on shared PCs are awkward, so per-person phones or keys are needed. Shared mailbox logins should be converted to delegated access (see §5).
- What the checker should report per user: MFA registered y/n; strongest method; weakest method still allowed; admins without phishing-resistant methods (critical).

### Gaps
- No independent data on passkey adoption in small nonprofits or schools.
- Could not confirm whether Microsoft's SMS retirement applies to tenants on Security Defaults, or whether passkey profiles need any license.
- Did not retrieve a primary source on SIM-swap prevalence (FBI IC3). Omitted rather than cited from memory.

---

## 5. Detecting child-sensitive records, and account hygiene (stale, alumni, shared, super-admin sprawl)

### Takeaway
A read-only checker can find *exposure* (public links, external shares, files owned by suspended or departed users) from metadata alone, without reading content. For "which files are sensitive," filename and metadata heuristics are the privacy-preserving first pass: IEP, 504, custody, counseling, incident, medical, allergy, SSN, immunization. Content inspection should be left to the platform's own DLP, which Workspace Education editions have, rather than pulling file bodies into a tool. Account hygiene data is mostly vendor-reported, but consistent: large shares of enabled accounts are inactive, and stale student accounts have been used as phishing launchpads.

### Cited Findings
**Drive/OneDrive exposure**
- The Drive API offers `drive.metadata.readonly` (view file metadata). Google classes it as restricted and advises the narrowest scope. — [Google: Choose Drive API scopes](https://developers.google.com/workspace/drive/api/guides/api-specific-auth)
- `files.list` / `permissions.list` show each permission's `type` (user, group, domain, anyone). This identifies "anyone with the link" and external-domain shares. — [DoControl](https://www.docontrol.io/blog/google-workspace-shared-drive-files-folders-shared-externally); [Drive files.list reference](https://developers.google.com/drive/api/v3/reference/files/list)
- An org-wide audit of every user's Drive traditionally needs a service account with DWD. Per-user audits can use Apps Script (DriveApp `anyoneWithLink` / `anyoneCanFind`). — [alulsh public Drive files](https://alulsh.github.io/2018/04/16/public-google-drive-files/); [ojensen5115](https://ojensen5115.github.io/musings/google-drive-public-file-audit)
- Google's Drive audit log events (Reports API, readable with `admin.reports.audit.readonly`) record sharing changes and visibility changes. This allows an admin-level exposure check *without* DWD and without listing every user's files. — [Drive log events](https://knowledge.workspace.google.com/admin/reports/drive-log-events)
- Workspace Education editions include DLP (content detectors) natively. — [ScubaGoggles commoncontrols.md §18](https://github.com/cisagov/ScubaGoggles/blob/main/scubagoggles/baselines/commoncontrols.md)

**Stale accounts and admin sprawl**
- Lepide 2026: 90% of organizations assessed had enabled inactive user accounts (vendor; sample not given). — [Lepide](https://www.lepide.com/research/state-of-identity-data-security-2026/key-10-findings/)
- Varonis (via secondary): 34% of internal accounts were inactive but enabled across more than 130 enterprises (unverified original). — [nhimg](https://nhimg.org/articles/dormant-office-365-users-create-hidden-access-paths-for-attackers/)
- The M365 admin center has no built-in stale-account report. Lighthouse (MSP tool) flags users inactive more than 6 months. — [office365itpros 2026-06-09](https://office365itpros.com/2026/06/09/find-inactive-accounts/); [Microsoft Learn: Lighthouse inactive users](https://learn.microsoft.com/en-us/microsoft-365/lighthouse/m365-lighthouse-manage-inactive-users)
- A years-old, still-active student Google mailbox was used to phish a district (prior research). — [IronScales](https://ironscales.com/threat-intelligence/student-google-account-apps-script-credential-phish)
- CISA: 2-8 super admins (GWS 6.2); admin accounts should be cloud-only and separate (6.1). — [commoncontrols.md](https://github.com/cisagov/ScubaGoggles/blob/main/scubagoggles/baselines/commoncontrols.md)
- CISA GWS 7.1: manage "conflicting" unmanaged consumer accounts created with the org domain. — [commoncontrols.md §7](https://github.com/cisagov/ScubaGoggles/blob/main/scubagoggles/baselines/commoncontrols.md)

### Inferences
- **Privacy-preserving sensitive-file detection design:**
  1. Use metadata only: title, mimeType, owner, last-modified, sharing permissions, parent folder name, and Drive labels if present.
  2. Match titles and folder paths against a small local keyword list: IEP, 504, evaluation, custody, court order, protective order, counseling, incident report, abuse, CPS/ACS, medical, allergy, immunization, SSN, birth certificate, tuition aid/FAFSA-like, pickup authorization.
  3. Output counts and file IDs, not titles, unless the admin opts in on-screen.
  4. Rank by exposure: "anyone with link," external domain, or owner suspended or departed.
  5. Never download content. For content scanning, recommend enabling the platform's DLP rules (Workspace Edu DLP; Purview on Business Premium).
- The sharing-event approach (Reports API Drive events, past 6 months) is the lowest-privilege org-wide exposure signal on Google. It misses files shared publicly more than 6 months ago, so pair it with an opt-in per-user or DWD scan.
- Hygiene checks a checker can do from Directory/Graph reads (Google `admin.directory.user.readonly` exposes lastLoginTime, 2SV enrolled/enforced and admin flags per the Directory API user resource; Graph `User.Read.All`/`AuditLog.Read.All`, but last sign-in may need P1):
  - accounts with no login in more than 90 days
  - prior-year student OUs still active
  - accounts with admin roles: count, and whether 2SV is enforced
  - shared or generic mailboxes with interactive sign-in enabled (frontdesk@, office@)
  - external forwarding rules
  - users with admin roles who also have mailboxes used daily
- Shared mailboxes with passwords are typical in childcare, where a front desk shares one login. They defeat per-person MFA and auditing.

### Gaps
- No prevalence data specific to schools, parishes or childcare for stale accounts, shared logins or super-admin counts. All figures are enterprise vendor surveys.
- Not verified: whether `drive.metadata.readonly`, via admin OAuth without DWD, can enumerate other users' files. Normally it cannot, and testing is needed.
- Not verified: Microsoft Graph licensing for `signInActivity` on Entra Free.

---

## 6. Design details for a safe read-only checker, and what existing tools lack

### Takeaway
Run the checker **locally** under the org's own admin, using **user-delegated OAuth with read-only scopes and a short-lived token**, and **store nothing off-device**. Avoid service accounts and DWD on Google, and avoid app registrations with secrets on M365, because each creates a persistent credential that is itself an attack path. Existing tools are strong for enterprises but assume E5/Enterprise Plus licensing, Windows/PowerShell, or expert interpretation. None encodes a license-aware, child-data-aware, plain-English view for a 15-seat parish school.

### Cited Findings
- ScubaGoggles' least-privilege scopes (all `.readonly` except `apps.licensing` and `apps.groups.settings`) are a ready-made Google scope list. It still requires Super Admin. — [Prerequisites.md](https://github.com/cisagov/ScubaGoggles/blob/main/docs/prerequisites/Prerequisites.md)
- ScubaGear Graph permissions for v1.8.0 include Directory.Read.All, Policy.Read.All and RoleManagement.Read.Directory, with Global Reader for interactive runs. Non-interactive SharePoint needs Sites.FullControl.All. — [permtrace](https://permtrace.com/blog/maester-scubagear-entra-id-security-baseline-testing); [ScubaGear permissions docs](https://github.com/cisagov/ScubaGear/tree/main/docs/prerequisites)
- Monkey365: PowerShell framework for M365, Entra ID and Azure. It "is designed to read configuration data and does not remediate." Some workloads need certificate-based app-only auth. — [Monkey365 README](https://raw.githubusercontent.com/silverhack/monkey365/main/README.md)
- CrowdStrike Reporting Tool for Azure (CRT, Dec 2020): finds hard-to-see permissions and config. It is meant to run as Global Reader, but some read-only functions need Global Admin. CISA lists it without endorsement. — [CrowdStrike CRT](https://www.crowdstrike.com/resources/community-tools/crt-crowdstrike-reporting-tool-for-azure/); [CISA listing](https://www.cisa.gov/resources-tools/services/crowdstrike-reporting-tool-crt)
- Maester: open-source, Pester-based, repeatable M365/Entra test suite that bundles SCuBA tests plus others (vendor says 360+ tests). Often run alongside ScubaGear. — [Senserva comparison](https://senserva.com/scuba-compliance-tools.html); [Maester marketplace](https://marketplace.microsoft.com/marketplace/apps/fortytwoio.maester)
- ScubaGear is a point-in-time assessment, not drift monitoring (vendor characterization). — [Senserva](https://senserva.com/best-microsoft-365-audit-tools.html)
- Microsoft recommends revoking refresh tokens (revokeSignInSessions) after device-code compromise. MFA alone does not evict an attacker who holds tokens and grants (also K12 SIX, prior research). — [Microsoft Storm-2372 blog](https://www.microsoft.com/en-us/security/blog/2025/02/13/storm-2372-conducts-device-code-phishing-campaign/)

### Inferences
**Auth model**
- Google: an installed-app OAuth client with PKCE (desktop or CLI), admin consents interactively, token held in memory only, scopes limited to the ScubaGoggles read-only set plus `admin.reports.audit.readonly` for token, login and Drive events.
  - Avoid `admin.directory.user.security`, the Directory tokens API scope. It can also *delete* tokens, so it is not read-only. Infer OAuth grants from Reports API "token" audit events instead (unverified that coverage is complete).
  - The admin must still create a GCP project and OAuth client. Provide a one-page walkthrough and tell them to delete the client after the run.
- M365: use a public client with device-code or auth-code-PKCE delegated sign-in as Global Reader, with delegated Graph scopes Directory.Read.All, Policy.Read.All, AuditLog.Read.All, RoleManagement.Read.Directory, Reports.Read.All, and Exchange Online read via Global Reader.
  - **Irony:** using device-code flow for the tool conflicts with recommending that orgs block device-code flow. Prefer auth-code + PKCE with a localhost redirect.
  - Afterwards, tell the admin how to remove the tool's enterprise-app consent.

**Data handling**
- Process in memory and emit a local HTML/JSON report. Redact UPNs and file titles by default, with on-screen reveal.
- No telemetry. If aggregate benchmarking is wanted, make it opt-in and limited to pass/fail per control ID, with no identifiers.
- Publish the scope list and a hash of the release.

**What to check (priority for this audience), with existing-tool coverage:**
1. Admin count and admin MFA strength. SCuBA covers it.
2. MFA strength for all users, and SMS/voice allowed. SCuBA covers it.
3. Third-party app consent policy plus inventory of granted apps with high-risk scopes: Mail.*, Files.ReadWrite.All, gmail, drive. SCuBA checks the policy, not the inventory of grants.
4. Device-code flow / legacy auth blocked (M365 CA). SCuBA partially, and license-gated.
5. Mail forwarding and inbox rules to external addresses. Covered by Exchange baseline / Gmail auto-forward setting; per-mailbox rule inventory not in SCuBA.
6. Stale accounts, prior-year students, suspended-but-still-sharing owners. Not in SCuBA.
7. Public or external Drive/OneDrive sharing of sensitive-named files. Not in SCuBA.
8. Google DWD grants and GCP service-account keys. SCuBA does not inventory DWD clients (gap).
9. Partner relationships (GDAP/DAP, Google resellers) and guest accounts. Partially in Maester and CRT.
10. Classroom settings: who can create and join classes, Classroom API consent. ScubaGoggles Classroom baseline.

**What existing tools lack for this audience**
- License-awareness, so findings fit Business Basic, Fundamentals or Nonprofits.
- Cross-platform, no-PowerShell execution (ScubaGear).
- An inventory of risky grants and DWD.
- Child-data exposure heuristics.
- Plain-language "do this next, in this order" guidance.
- Unified Google + Microsoft coverage: Maester, Monkey365, CRT and ScubaGear are Microsoft-only, and ScubaGoggles is Google-only. GAM can export most Google data but is an admin power tool with write capability, not an assessor.

### Gaps
- Did not verify Maester's or Monkey365's exact permission sets or current versions. CRT's maintenance status (it may be archived) was not checked.
- Did not verify GAM's (GAMADV-XTD3) read-only mode or minimal scopes.
- Did not confirm that Google Reports API token events give a complete inventory of current OAuth grants. They are events, not state, and limited to 6 months, so long-standing grants could be missed. This needs testing.
