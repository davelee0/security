# Access register: testing what it rests on

_November 24, 2026. Before piloting the [access register](../kits/access-register.md)
with a real organization, we tested the assumptions it depends on. If any were
wrong, the register would be solving the wrong problem or asking for something
nobody can provide._

| # | Assumption | Result |
|---|---|---|
| 1 | How vendor staff reach student data is invisible to schools | **Confirmed** in New York's public disclosures |
| 2 | The standard national data agreement doesn't already cover it | **Confirmed**: it covers employees and audits, not access controls |
| 3 | The controls we ask for are realistic for vendors to offer | **Confirmed**, with a caveat about Google and Microsoft |
| 4 | The register's rows can be filled in, by hand or by a read-only tool | **Mostly confirmed**, with two specific gaps |
| 5 | Vendors will actually answer the questionnaire | **Not yet tested**; needs real sends |

---

## 1. Vendor support access is invisible to schools

**Test.** NYC Public Schools publishes a disclosure for every outside party
that receives student data (see the [NYC 2-d study](../../research/nyc-2d/README.md)).
We searched the 890 non-research disclosures for any passage about support
staff or remote access (`research/nyc-2d/support_access.py`), found 24
candidates, and read each one.

**Result.**

- Most of the 24 describe vendor employees connecting to the vendor's *own*
  systems (VPNs, remote desktops), not support staff reaching a school's data.
- **Only 3 of 890 describe vendor support staff accessing customer data at
  all.** One says this happens only when an approved NYCPS staff member asks.
  One says "a small number of support staff have access to PII in order to
  make changes due to technical issues," with no approval step or logging
  described. One lists customer support as a purpose, without controls.
- **None mentions a time limit on support access or logs the district can
  see.**
- About 5 say employees need multi-factor authentication for remote access to
  production systems: the control whose absence enabled the PowerSchool
  breach.

**Why it matters.** This is New York, the strongest student-privacy regime in
the country, and the form simply doesn't ask. A school relying on these
disclosures cannot know whether a vendor's support path looks like
PowerSchool's.

## 2. The national data agreement doesn't cover it

**Test.** We read the full text of the Student Data Privacy Consortium's
National Data Privacy Agreement, version 2.2 (25 pages), the standard contract
used by thousands of US districts.

**Result.** It covers:

- **§4.3:** vendor employees with access must follow the agreement and sign
  confidentiality agreements;
- **§5.2:** an annual security audit, a copy of which the district can request;
- **§5.3:** adopting a recognized cybersecurity framework (NIST and others,
  Exhibit F).

It does **not** address: how vendor staff authenticate (the words
"authentication," "multi-factor," "remote" and "access control" don't
appear), whether the district approves access first, time limits, access logs
visible to the district, or how quickly departing staff and contractors lose
access.

**Change made.** The register's contract wording is now framed as an addendum
to the NDPA or any existing data agreement, and the questionnaire asks for
the §5.2 audit report where the NDPA applies.

## 3. The controls are realistic, but premium for the big platforms

**Test.** Do mainstream platforms already offer support access that is off by
default, approved per request, time-limited and logged?

**Result.**

- **Salesforce** lets customers grant support staff login access for a chosen
  period (from one day) and revoke it at any time, on its standard
  editions.
  ([Salesforce: Grant Login Access](https://help.salesforce.com/s/articleView?language=en_US&id=xcloud.granting_login_access.htm&type=5))
- **Microsoft** offers Customer Lockbox, which requires customer approval
  before Microsoft engineers access content, but only in Microsoft 365 E5 and
  Office 365 E5. It isn't in Business Premium or E3.
  ([Microsoft Purview service description](https://learn.microsoft.com/en-us/office365/servicedescriptions/microsoft-365-service-descriptions/microsoft-365-tenantlevel-services-licensing-guidance/microsoft-purview-service-description))
- **Google** offers Access Approvals only with the Assured Controls add-on,
  best on Enterprise Plus or Frontline Plus. Access Transparency logs are in
  higher editions, including Education Standard and Plus.
  ([Google: Access Approvals](https://support.google.com/a/answer/12410469),
  [Access Transparency](https://support.google.com/a/answer/9230474))

**Conclusion.** The model is proven and buildable, so asking edtech, childcare
and parish-software vendors for it is reasonable. The irony is that small
organizations can't buy it from the two platforms that hold most of their
data. The register now says so, and treats Google and Microsoft's own support
access as a row to note rather than a fixable gap.

## 4. The rows can be filled in, with two gaps

**Test.** For each kind of row, can a non-technical admin find it, and can the
planned read-only checker fill it automatically?

| Row | By hand | Automatically, read-only |
|---|---|---|
| Google admins | Admin console → Account → Admin roles | Yes: `admin.directory.rolemanagement.readonly` |
| Google connected apps | Admin console → Security → API controls | **Partial.** Listing app grants per user needs `admin.directory.user.security`, which can also delete them, so it isn't read-only. A read-only tool must rebuild the list from token audit events (`admin.reports.audit.readonly`), which cover about 6 months. |
| Microsoft admins | Microsoft 365 admin center → Roles | Yes: `RoleManagement.Read.Directory` |
| Microsoft connected apps | Entra admin center → Enterprise applications | Yes: `Application.Read.All` |
| Stale accounts (Microsoft) | Review each admin's activity | **Needs P1.** The last-sign-in date (`signInActivity`) requires Entra ID P1 and `AuditLog.Read.All`. On free or Business Basic tenants, stale admins must be found another way. |
| Vendor support, IT providers, devices | Contracts, invoices, asking the IT provider | No: these live outside the tenant |

Sources: [Google tokens.list](https://developers.google.com/admin-sdk/directory/reference/rest/v1/tokens/list),
[Google OAuth scopes](https://developers.google.com/identity/protocols/oauth2/scopes),
[Microsoft Graph user resource](https://learn.microsoft.com/en-us/graph/api/resources/user?view=graph-rest-1.0).

**Change made.** The register says which rows a tool can fill and which need a
person, and the checker's design must state these two gaps instead of
pretending to full coverage.

## 5. Not yet tested: will vendors answer?

The questionnaire is only useful if vendors answer it. That can't be tested
from public information. Two ways to test it before a full pilot:

1. **Public-documentation baseline:** for 8–10 vendors common in small
   schools, childcare and parishes, record what their public security or trust
   pages already say about the four questions. Cheap, and shows how often the
   answer is "not stated."
2. **A small real send:** an organization that already uses a vendor sends the
   questionnaire to 3–5 of them, and we record response rates and quality.
   This needs a willing organization, so it's the first step of a pilot.
