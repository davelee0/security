# Sources and fact check

Checked November 24, 2026 against the pages below. "Confirmed" means read on the primary source. Anything else is flagged.

## Corrections to the build-decision page

| Claim on the build page | What the sources say |
|---|---|
| Microsoft retires text and voice codes on Feb 1, 2027 | **Partly right.** Feb 1, 2027 for most users; **July 1, 2027 for Global Administrators and outside users**. It's Microsoft-provided delivery that ends; organizations can pay a telephone provider to keep SMS. Public cloud incl. GCC; other clouds later. |
| "On Microsoft, license only those few for the paid tier" | **Needs nuance.** Passkeys are free on every plan. Only *forcing* them (Conditional Access) needs Entra ID P1. Whether an org may license just a few users for P1 while using Conditional Access was **not confirmed**. Conditional Access also requires turning off security defaults, which affects everyone. |
| Sudbury, MA 2025: "attackers got past MFA in real time and diverted payroll" | **Overstated.** Source says attackers could "intercept multi-factor authentication (MFA) codes"; it doesn't say real-time relay. Amount was **$12,825.50**, four employees' direct deposits, and a specialist approved the changes without verifying. It is as much a payment-change lesson as a passkey one. |
| North Dakota district ~$4.9M, 2026 | **Confirmed with nuance.** Dickinson Public Schools; ~$4.92M lost (local news); $4,856,578.51 seized by federal prosecutors, held pending court order. |
| Ohio parish $1.75M, 2019 | **Confirmed** by Catholic News Service; FBI confirms BEC but gives no figure. |
| Keys about $25-50 each | **Confirmed:** $29 (Yubico), $30-35 (Google Titan). |

## Confirmed facts and where

Microsoft
- SMS/voice retirement dates, scope (MFA and SSPR), blocking passkey prompt: [Learn: retirement](https://learn.microsoft.com/en-au/entra/identity/authentication/concept-sms-voice-retirement) (updated 2026-09-23/11-13), [FAQ](https://learn.microsoft.com/en-us/entra/identity/authentication/concept-sms-voice-retirement-faq) (2026-11-04), [Security blog, 2026-07-13](https://www.microsoft.com/en-us/security/blog/2026/07/13/microsoft-entra-id-security-updates-passkeys-are-the-default-authentication-method-in-entra-id/)
- Passkeys free on all editions; admin click path; "can't opt out" of passkey profiles; MFA within 5 minutes before registering: [Learn: enable passkeys](https://learn.microsoft.com/en-us/entra/identity/authentication/how-to-enable-passkey-fido2) (2026-05-15)
- User registration steps: [Learn: register passkey with security key](https://learn.microsoft.com/entra/identity/authentication/how-to-register-passkey-with-security-key) (2026-07-06)
- Conditional Access needs P1: [Learn: authentication strengths](https://learn.microsoft.com/entra/identity/authentication/concept-authentication-strengths) (2025-10-24)
- Business Premium / E3 include P1: [Learn: MFA licensing](https://learn.microsoft.com/en-gb/entra/identity/authentication/concept-mfa-licensing) (2025-03-04)
- P1 listed at $7.00/user/month, annual: [Microsoft Entra pricing](https://www.microsoft.com/en-us/security/microsoft-entra-pricing)
- Phishing-resistant CA policy steps, report-only, exclude break-glass: [Learn: policy](https://learn.microsoft.com/entra/identity/conditional-access/policy-admin-phish-resistant-mfa) (2026-03-24)
- Security defaults can't be customized, must be disabled for CA, two emergency accounts: [Learn: security defaults](https://learn.microsoft.com/entra/fundamentals/security-defaults) (2026-10-16)
- SMS and Voice call controls in the Authentication methods policy: [Learn: manage methods](https://learn.microsoft.com/en-us/entra/identity/authentication/how-to-authentication-methods-manage) (2026-01-15)

Google
- 2SV click path, OU scoping, Methods incl. "Only security key", grace period: [Deploy 2SV](https://knowledge.workspace.google.com/admin/security/deploy-2-step-verification)
- Advanced Protection settings and click path: [Enable enrollment](https://knowledge.workspace.google.com/admin/security/enable-user-enrollment-in-the-advanced-protection-program), [Protect users](https://knowledge.workspace.google.com/admin/security/protect-users-with-the-advanced-protection-program) (2026-11-10)
- Admin backup codes, User management privilege, super admin for admins: [Recover an account](https://knowledge.workspace.google.com/admin/security/recover-an-account-protected-by-2-step-verification) (2026-11-10)

Payment fraud guidance
- [FBI IC3 PSA I-091124-PSA, Sept 11, 2024](https://www.ic3.gov/PSA/2024/PSA240911): $55.5B exposed loss 2013-2023; verify changes via secondary channels; recall and file at ic3.gov.
- [Nacha BEC Response Action Plan, 2024](https://www.nacha.org/system/files/2024-07/Business%20Email%20Compromise%20Action%20Plan.pdf): out-of-channel confirmation, callback on known number, dual control, activity alerts.

Incidents
- [Sudbury Weekly, 2026-05-07](https://sudburyweekly.com/sps-hit-by-payroll-cyberattack-in-2025-over-12000-diverted/)
- [Valley News Live, 2026-02-10](https://www.valleynewslive.com/2026/02/11/north-dakota-school-district-loses-nearly-5-million-sophisticated-email-scam/); [U.S. Attorney ND, 2026-04-30](https://www.justice.gov/usao-nd/pr/north-dakota-fbi-and-us-attorneys-office-recover-48-million-dollars-scammed-dickinson)
- [America / CNS, 2019-04-30](https://www.americamagazine.org/faith/2019/04/30/hackers-infiltrate-ohio-parishs-email-system-steal-175-million); [FBI Cleveland, 2019-04-30](https://www.fbi.gov/contact-us/field-offices/cleveland/news/press-releases/st-ambrose-catholic-parish-was-a-victim-of-a-business-email-compromise-scheme)

Keys
- [Yubico Security Key series](https://www.yubico.com/product/security-key-series/): $29, FIDO2 passkeys.
- [PCMag review via Yahoo, 2026-05-30](https://tech.yahoo.com/cybersecurity/articles/google-titan-security-key-100000396.html): Titan $30/$35.

## Not confirmed (check before publishing)

1. **Google editions.** The edition tables (2SV and security keys on all Business and Education editions) were read through a summary of a truncated page, not verbatim. Nonprofits edition not checked. No page stated which editions offer "Only security key" enforcement.
2. **Google: passkeys count under "Only security key."** From a summary of the deploy page, not verbatim text.
3. **Google: how the grace period works for admin backup codes.** The recovery page says users can enter an admin-generated code "during the grace period." The guide reads that as "generate the code when it's needed," and so drops the existing kit's advice to pre-generate codes for the safe. Test on a real tenant.
4. **Microsoft: licensing only some users for P1** while Conditional Access is on. The project's research cites a community answer that every user covered by a Conditional Access policy needs P1, which supports licensing just the few; Microsoft's own pages read here don't say. Nonprofit Business Premium at about $5.50/user/month also comes from the research notes and wasn't re-checked.
5. **Microsoft: exact toggle path to turn off SMS and Voice call.** The page confirms the controls exist; the step-by-step was cut off.
6. **Microsoft: Temporary Access Pass for key recovery** is mentioned on the CA policy page as a way to register passwordless methods; the TAP setup page itself was not read.
7. **Bank products** (Positive Pay, ACH debit blocks) are listed as questions to ask, not as facts; the Nacha plan doesn't mention them.
8. **Device-code phishing and app consent** (the "What keys don't stop" section) rest on the project's research notes; the security defaults page confirms security defaults block device code flow.

## Consistency with the project's own research

Checked against `docs/research/technical-cyber-defense-research-tree.md` and `research_notes/Technical cyber defense research tree/` (email_payment_fraud.md, identity_cloud_tenants.md). Aligned the payment rule with the research's 48-hour hold and "tell the old contact" step. The research notes themselves flag that Sudbury's "intercepted MFA" was never confirmed as real-time relay, which matches this check; the existing money-movers kit and threat_landscape notes overstated it.
