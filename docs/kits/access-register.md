# Access register

One list of every person, vendor, app and device that can reach children's
information **without asking first**.

The biggest breaches of children's data mostly didn't come through a school's
own login. They came through access that was always on and that nobody was
watching:

- **PowerSchool (2024):** a former subcontractor's support login, protected by
  a password only, was used to export student records from customer
  databases.
- **Canvas (2026):** a support representative's session was taken over
  through a support ticket and used to pull data.
- **Kaseya (2021):** one attack on an IT-management tool reached customers of
  the IT firms that used it, including more than 100 kindergartens in New
  Zealand.
- Closer to home: a former volunteer who is still an admin, an app someone
  approved years ago, a camera recorder still on the installer's default
  password.

The register makes these doors visible. Fill it in once (about an hour), then
review it every quarter and whenever someone leaves or a vendor changes.

A spreadsheet version is in [access-register.csv](access-register.csv).

---

## Part 1. The register

One row for each way in. Five kinds of rows:

| Kind | Examples |
|---|---|
| **Person** | Every admin account in Google or Microsoft, the student or childcare system, tuition platform, website, bank |
| **Vendor support** | The vendor's own staff who can reach your data to help you (SIS, tuition, childcare app, parish software) |
| **IT provider** | A local IT firm or volunteer with remote-access tools on your computers |
| **App or integration** | Apps approved to read your email, drive or rosters; rostering links (Clever, ClassLink, Google Classroom sync); long-lived API keys |
| **Device** | Camera recorders, door-access controllers, visitor systems, copiers that store scans, the office router |

Columns:

| Column | What to write |
|---|---|
| Kind | Person, vendor support, IT provider, app, or device |
| Name | The person, vendor, app or device |
| What it can reach | Which systems and which children's information |
| How it gets in | Admin login, vendor support portal, remote-access tool, app permission, network |
| Protection | Password only / ordinary two-step / passkey or key / unknown |
| Always on? | Yes, or "only when we approve it" |
| Do we see when it's used? | Yes (where) / no / unknown |
| Still needed? | Yes / no: remove |
| Owner here | Who in our organization is responsible for this row |
| Last reviewed | Date |

**What to act on first:**

1. Any row marked **"Still needed: no."** Remove it this week.
2. Any **person** row with "password only" or "unknown." Turn on two-step
   sign-in; for money-movers and admins, use passkeys (see the
   [money-movers kit](money-movers.md)).
3. Any **vendor support** or **IT provider** row that is "always on" and
   unseen. Send the questionnaire below.
4. Any **device** row where nobody knows whether the default password was
   changed. Ask the installer, in writing.

### Where to find the rows

- **Google Workspace admins:** Admin console → Account → Admin roles → each
  role → Admins.
- **Google apps with access:** Admin console → Security → Access and data
  control → API controls → Manage third-party app access.
- **Microsoft 365 admins:** Microsoft 365 admin center → Roles → Role
  assignments.
- **Microsoft apps with access:** Microsoft Entra admin center → Enterprise
  applications.
- **Remote-access tools:** ask your IT provider for a written list, or look
  for tools such as ScreenConnect, TeamViewer, AnyDesk, Splashtop or Kaseya
  on office computers.
- **Vendors:** your contracts and invoices. Anyone you pay who holds student
  or family data belongs on the list.

A planned read-only account checker will fill the person and app rows
automatically for Google Workspace and Microsoft 365.

---

## Part 2. Vendor support-access questionnaire

Send this to every vendor marked "vendor support" or "IT provider." Four
questions, each with an answer you can check.

> Subject: Four questions about support access to our data
>
> Hello,
>
> We're reviewing who can access the information we hold about children and
> families. Please answer these four questions about how your staff, and any
> contractors you use, can access our data:
>
> 1. **Off by default.** Can your staff reach our data at any time, or only
>    after we approve a specific request? If at any time, can we switch that
>    off?
> 2. **Approved per request.** If access is granted, is it tied to a single
>    support ticket and does it end automatically? How long does it last?
> 3. **Phishing-resistant sign-in.** Do all staff and contractors who can
>    reach customer data sign in with phishing-resistant methods (passkeys or
>    security keys), not passwords or text-message codes alone?
> 4. **Logged and visible to us.** Is each access logged? Can we see the log,
>    and how long do you keep it?
>
> We'd also appreciate the date of your most recent independent security
> assessment (for example, a SOC 2 Type II report) and what it covered.
>
> Thank you,
> [Name], [role], [organization]

**How to read the answers:**

- "Yes, with how" is a good answer. "We take security seriously," or a
  certificate that belongs to their cloud host (for example, citing
  Microsoft Azure's certifications), doesn't answer the question.
- "MFA is available" is not the same as "MFA is required." Ask which.
- No answer after two weeks is an answer. Mark the row "unknown" and raise it
  at renewal.

---

## Part 3. Contract wording

Ask for this as an addendum at the next renewal. It turns the four questions
into commitments.

> **Support access to Customer Data.**
>
> (a) Vendor personnel and subcontractors shall not access Customer Data
> except to resolve a specific support request made or approved by Customer,
> and such access shall end when the request is resolved or after [72 hours],
> whichever is sooner.
>
> (b) All Vendor personnel and subcontractors able to access Customer Data
> shall authenticate using phishing-resistant multi-factor authentication.
>
> (c) Vendor shall log each access to Customer Data by its personnel or
> subcontractors, retain those logs for at least twelve (12) months, and
> provide them to Customer on request.
>
> (d) Vendor shall promptly disable access for any personnel or subcontractor
> who no longer requires it, and in any case within [24 hours] of the end of
> their engagement.
>
> (e) Within thirty (30) days of the end of the Agreement, Vendor shall delete
> Customer Data and provide written certification of deletion.

Bracketed values are suggestions to negotiate. A lawyer should review the
final wording; a large vendor may offer equivalent terms in its own form.

_General guidance only, not legal advice or a security assessment._
