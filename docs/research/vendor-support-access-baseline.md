# Vendor support access: what vendors already say publicly

_November 24, 2026. This is the public-documentation baseline proposed in
[access-register-assumptions.md §5](access-register-assumptions.md#5-not-yet-tested-will-vendors-answer).
Before anyone sends the [access register](../kits/access-register.md)
questionnaire, we checked what eight vendors common in small schools,
childcare centers and parishes already say on their own public pages about
the four support-access questions. Google Workspace and Microsoft 365 are
included as a reference point._

## Headline

**None of the eight vendors publicly states any of the four controls for its
own staff.** Of 32 answers (8 vendors × 4 questions), 0 are stated, 6 are
partial, and 26 are not stated. One vendor, Flocknote, says the opposite of
question 1: its engineers "may also have access" to personal information "in
order to provide support," with no approval step mentioned.

The two reference platforms show the controls exist and can be described in
a sentence. Microsoft states all of them except how its engineers sign in,
but only on E5 or a compliance add-on. Google's per-request approval needs a
paid add-on, while its access logs are in Education Standard and Plus.

So the questionnaire isn't asking for something already answered in public.
For these vendors the honest starting value for every vendor-support row is
**"unknown"**, and the four questions are the only way to change it.

## The four questions

From [Part 2 of the access register](../kits/access-register.md#part-2-vendor-support-access-questionnaire):

1. **Off by default:** staff can reach customer data only after the customer
   approves, or can switch standing access off.
2. **Approved per request:** access is tied to one support ticket and ends
   automatically (time limit noted where stated).
3. **Phishing-resistant sign-in:** staff who can reach customer data must use
   passkeys or security keys. Plain "MFA" is recorded as partial.
4. **Logged and visible:** each staff access is logged and the customer can
   see the log (retention noted where stated).

**Scoring.** _Stated_ means the vendor's own page says it about its own
staff. _Partial_ means something related is said but falls short (general
"authorized personnel only", MFA without saying which kind, logs the customer
can't see, or documents too old to rely on). _Not stated_ means nothing on
the pages read. Controls described for the **customer's own users**, such as
role permissions or two-step sign-in for teachers and parents, don't count:
they answer a different question, and several vendor pages are easy to
misread this way.

## Vendors and why they were picked

| Vendor | Category | Why |
|---|---|---|
| PowerSchool | Student information system (SIS) | Largest K-12 SIS in North America; the 2024 breach came through a support login |
| FACTS (Nelnet) | SIS, tuition, giving | Widely used by Catholic and other private schools |
| Blackbaud | Private-school SIS, tuition, fundraising | Common in independent schools; 2020 breach |
| brightwheel | Childcare management | One of the most used childcare apps in the US |
| Procare Solutions | Childcare management | Long-established childcare billing and check-in software |
| ParishSOFT (Ministry Brands) | Parish management | Standard in many Catholic dioceses |
| Flocknote | Parish communication | Common parish email and text tool |
| ParentSquare | School–family communication | Widely used school messaging platform |
| Google Workspace | Reference | Holds most small organizations' email and files |
| Microsoft 365 | Reference | Same |

## Results

S = stated, P = partial, — = not stated. Details and sources follow the table.

| Vendor | 1. Off by default | 2. Per request | 3. Phishing-resistant | 4. Logged, visible |
|---|---|---|---|---|
| PowerSchool | — | — | — | — |
| FACTS | — | — | — | — |
| Blackbaud | P | P | — | P |
| brightwheel | — | — | P | — |
| Procare | P | — | — | — |
| ParishSOFT | — | — | — | — |
| Flocknote | — (says the opposite) | — | — | — |
| ParentSquare | P | — | — | — |
| _Microsoft 365 (E5)_ | _S, once turned on_ | _S: 4 hours_ | _—_ | _S_ |
| _Google Workspace_ | _S, with paid add-on_ | _S, with paid add-on_ | _—_ | _S, Education Standard/Plus_ |

No page from any of the ten mentions passkeys, FIDO or security keys for
staff.

### PowerSchool

- **1–2:** Not stated. The archived 2023 privacy statement says customer
  instructions "can be submitted through the PowerSchool support system,"
  which is about privacy requests, not staff access.
- **3:** Not stated for staff. The only MFA text is advice to schools: "MFA
  can be enabled as part of the SSO configuration."
  ([blog](https://www1.powerschool.com/blog/best-practices-improving-sis-cybersecurity/))
- **4:** Not stated. The archived statement says system events "are monitored
  by the creation of artifacts or metadata," with nothing on customer
  visibility. ([privacy, archived 2023](https://www1.powerschool.com/privacy/))
- **Note:** The [K-12 security comparison chart](https://www1.powerschool.com/security/edtech-partner-assessment/)
  has rows for MFA and audit logging, but its marks are images and can't be
  attributed to a vendor. The current privacy page returned a bot-protection
  page. A trust center wasn't found on the public site.

### FACTS

- **1, 2, 4:** Not stated.
- **3:** Not stated for staff. "Strong user authentication measures are
  employed ... including the use of complex passwords and multifactor
  authentication (MFA)" doesn't say whose accounts.
  ([blog](https://factsmgt.com/blog/a-commitment-to-data-security-for-k-12-schools-inside-look/))
  Staff get phishing simulations and training.
  ([trusted data security](https://factsmgt.com/trusted-data-security/))
- **Note:** The school-management and tuition security pages are the
  Australia/New Zealand versions.

### Blackbaud

- **1 (P):** "You effectually grant Blackbaud access to your data only by
  sending a copy of your database, providing Blackbaud with a database login
  ... or via remote access." ([data policy, 2016](https://webfiles-sc1.blackbaud.com/files/support/kb/datapolicy.pdf))
  This reads as customer-granted, but the policy is from 2016 and centers on
  database copies and installed products.
- **2 (P):** The same policy says the support login must begin with "BBSUPP"
  and that credentials are given by phone. No expiry is stated. How staff
  reach data in Blackbaud's cloud products isn't described.
- **3:** Not stated. The [trust center](https://trust.blackbaud.com/) says
  employees sign in through central SSO, with no mention of MFA.
- **4 (P):** "We use security information and event management (SIEM)
  software to store logs ... stored off-site for up to one year, and reviewed
  daily." ([K-12 security overview, 2019](https://webfiles-sc1.blackbaud.com/files/support/helpfiles/education/k12/whitepapers/k12securityoverview.pdf))
  These are Blackbaud's internal logs, not ones the school can see.
- **Note:** The trust center lists answers on access management and personnel
  security, but they only open inside its app, not as public pages.

### brightwheel

- **1, 2, 4:** Not stated. Admins get an email when a new admin is added,
  which is an alert, not an access log.
- **3 (P):** "Multi-factor authentication is required for all administrative
  access to the systems that process program data."
  ([security FAQ](https://help.mybrightwheel.com/en/articles/6363539-brightwheel-security-faqs))
  The best staff statement in the set, but it doesn't say which kind of MFA
  or whether it covers support staff.
- **Note:** The [privacy policy](https://mybrightwheel.com/privacy/) says
  customer data is "governed by the contracts," so the contract is the place
  to look.

### Procare Solutions

- **1 (P):** "Only people authorized to see your data can view it."
  ([data security guide, 2024](https://www.procaresoftware.com/wp-content/uploads/2024/03/PC_Guide_DataSecurity2_Feb24.pdf))
  It doesn't say who authorizes.
- **2, 4:** Not stated.
- **3:** Not stated for staff. MFA is offered to customers and is optional
  ("While optional for you and the families you serve, it is highly
  recommended", same guide).

### ParishSOFT (Ministry Brands)

- **1–4:** Not stated. Account-management guidance covers the parish's own
  users. ([best practices](https://support.parishsoft.com/hc/en-us/articles/42743364945691-Best-Practices-for-User-Account-Management))
- **Note:** The main security page lists Microsoft Azure's certifications
  (ISO 27001, SOC 2 and others) in place of ParishSOFT's own.
  ([Azure page](https://parishsoft.com/news/security-privacy-compliance-the-benefits-of-microsoft-azure))
  The register already warns that a cloud host's certificate doesn't answer
  these questions.

### Flocknote

- **1:** The [privacy policy](https://flocknote.com/privacy/) says "our team
  of engineers may also have access to other PII or information about actions
  taken by a user within the system in order to provide support to
  customers." This describes standing access with no customer approval
  mentioned.
- **2–4:** Not stated. Customer accounts are described as password-protected.

### ParentSquare

- **1 (P):** "Access controls to limit sensitive data to authorized
  ParentSquare personnel, with mandatory annual privacy training."
  ([security and compliance](https://www.parentsquare.com/platform/security-and-compliance/))
- **2–4:** Not stated. The trust center at trust.parentsquare.com showed no
  readable content.

### Reference: Microsoft 365 and Google Workspace

- **Microsoft Customer Lockbox:** "Customer Lockbox ensures that no one at
  Microsoft can access customer content to perform a service operation
  without the customer's explicit approval." Admins turn it on; requests
  expire after 12 hours unapproved; "the maximum period for the access
  permissions granted to the Microsoft engineer is 4 hours"; "All actions
  performed by a Microsoft engineer are logged in the audit log." Included
  with E5 (and A5/G5), or as a compliance add-on.
  ([Customer Lockbox](https://learn.microsoft.com/en-us/purview/customer-lockbox-requests),
  [Purview service description](https://learn.microsoft.com/en-us/office365/servicedescriptions/microsoft-365-service-descriptions/microsoft-365-tenantlevel-services-licensing-guidance/microsoft-purview-service-description))
  How engineers sign in isn't stated beyond "least privilege and just-in-time
  access."
- **Google Access Approvals:** "Require Google staff to get explicit approval
  before they access your covered data," approved one request at a time. It
  needs the paid Assured Controls add-on (Frontline Plus or
  Enterprise Plus). **Access Transparency** logs of "actions taken by Google
  staff when accessing user content" are included in Education Standard and
  Education Plus.
  ([Access Approvals](https://support.google.com/a/answer/12410469),
  [Access Transparency](https://support.google.com/a/answer/9230474),
  [Assured Controls](https://support.google.com/a/answer/13880647))

## What the pattern shows

1. **Silence, not refusal.** No vendor says its staff access is unrestricted
   or unlogged; they just don't say. That matches the NYC finding (3 of 890
   disclosures describe support access at all). The questionnaire is the
   first time most of these vendors will be asked.
2. **Customer-side controls fill the space.** Most security pages describe
   roles and two-step sign-in for the school's own staff and parents. A busy
   administrator can easily read these as answers to questions 1 and 3. The
   register's "how to read the answers" note should keep saying this
   plainly.
3. **The best public details are old or locked.** Blackbaud's clearest text
   is from 2016 and 2019. PowerSchool's readable privacy statement is the
   archived 2023 version. Blackbaud's and ParentSquare's trust centers don't
   show their answers publicly. Asking for current written answers, as the
   questionnaire does, is the right move.
4. **Phishing-resistant sign-in is absent everywhere.** Only brightwheel says
   anything about MFA for its own staff, and nobody, including Google and
   Microsoft, names passkeys or security keys for support staff. This is the
   control whose absence made the PowerSchool breach possible.
5. **Approval-before-access is a premium feature even at the top.** The
   small-vendor gap isn't surprising when the two biggest platforms charge
   extra for it.

## Limits

- Public pages only, read on November 24, 2026. Contracts, data agreements,
  SOC 2 reports and gated trust-center answers may say more, which is why the
  questionnaire asks for them.
- A "not stated" means we didn't find it on the pages listed, not that the
  control doesn't exist.
- Quotes are short excerpts; follow the links for context.

## Next step

The second test in §5 still stands: an organization that already uses some of
these vendors sends the questionnaire to 3–5 of them, and we record who
answers and how well. This baseline gives the comparison: every row starts at
"not stated."
