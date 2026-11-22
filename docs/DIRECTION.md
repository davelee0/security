# Direction: what would actually make these organizations safer

A proposal, written November 2026, for discussion. Nothing here is settled.

## The problem, stated plainly

A parish school office, a childcare center or a youth program holds
some of the most sensitive data there is: children's names, birthdays,
addresses, medical and allergy notes, custody arrangements, photos,
tuition and payroll records. It's usually protected by one busy person
who also does enrollment, or by a volunteer, and nobody whose job is security.

## What actually goes wrong

Ranked by how often it hurts small organizations, not by how dramatic it sounds:

1. **Impersonation and payment fraud.** Email "from the principal" asking
   the bookkeeper to update a vendor's bank details. A fake tuition
   invoice sent to parents. A "pastor" asking for gift cards. Year after
   year, business email compromise is among the biggest sources of
   reported losses in the FBI's Internet Crime Reports, and it needs no
   technical skill.
2. **Account takeover.** One staff member's reused password leads into
   Google Workspace or Microsoft 365, which now holds *everything*:
   enrollment spreadsheets, shared drives, the email used to reset every
   other account.
3. **Oversharing, not hacking.** A Google Sheet of student medical
   notes shared as "anyone with the link." A public sign-up form whose
   responses are visible. Photos with full names on a public page. This
   is probably the most common way children's data actually leaks from
   small organizations, and no attacker is involved.
4. **Vendors.** Student information systems, childcare apps, donation
   platforms. When a large vendor is breached, as with the PowerSchool
   breach disclosed in early 2025, every school using it is exposed. The
   school can't fix the vendor, but it can choose carefully, turn on MFA
   for admin accounts, and avoid uploading more than it needs.
5. **The website.** Outdated WordPress plugins get small-organization
   sites defaced, filled with spam, or used to skim donation pages.
6. **Ransomware.** Real, but less likely for an organization that keeps
   everything in the cloud. More relevant to schools with an old file
   server in a closet.

## Pushing back on the starting assumptions

**"AI is shifting security toward defenders; we need to bring those tools
to small orgs."** For big institutions the bottleneck is analyst time,
so AI helps. For a parish school the bottleneck is that *nobody spends
even one hour on this*. The protective features already exist and are
mostly free: MFA, DKIM, sharing controls and security dashboards are
built into Google Workspace and Microsoft 365, and agencies like CISA
offer free guidance and services. What's missing is a trusted person who
translates, prioritizes and follows up. So the most useful AI here is
*for the helper*: explaining a finding, drafting the email to the website
host, turning a DMARC report into a sentence. Not an autonomous agent
poking at their systems.

**"A checklist."** Seventeen equal-looking checkboxes stall people. Put
three things first and give the exact clicks for their platform. Nearly
all of these organizations run on Google Workspace or Microsoft 365, so
platform-specific steps beat generic advice every time.

**"Their data is on their computers."** It's mostly in SaaS accounts and
vendor apps now. That means security is about *identity and
configuration* (who can sign in, what's shared, which settings are on)
more than networks and firewalls. It also means the highest-value tools
are read-only configuration checks run *by the organization's own admin*.

**"Nonprofits, parishes and small businesses."** Too wide for one person
to do well. I'd start narrow, with Catholic parish schools and
childcare/youth programs, because:

- You care most about it, and that sustains a free project.
- **Dioceses are a force multiplier.** One diocese can reach dozens of
  schools and parishes, and many already provide shared email or IT.
- **The culture already exists.** Since the Dallas Charter, every diocese
  runs a Safe Environment program, with training, background checks and
  a shared conviction that protecting children is everyone's job. Digital
  safety fits naturally inside that frame: protecting a child's records
  is part of protecting the child. That framing will land better than
  "cybersecurity."

Everything stays open and usable by anyone; the focus is just where you
spend your own time.

**"Build tools to learn security."** Tools teach some of it. Sitting with
three real organizations (with permission) and helping them fix things
will teach you more, and will tell you which tools are worth building.

**Trust and care are the real assets.** Security advice carries weight. A
few non-negotiables:

- Written permission before looking at anything that isn't public.
- **Never commit findings about a real organization to this public
  repository.** A list of which schools have weak email security is a
  target list. (`.gitignore` already blocks report files.)
- Be honest about uncertainty. The checkup tool says "couldn't check"
  rather than guessing, for this reason.

## Proposed direction: three layers

### 1. Guides: the first hour
- **"Your first hour" for Google Workspace and for Microsoft 365**: the
  five settings that matter most, with exact click paths. Enforce MFA for
  everyone (admins first); keep two super-admins and no more; restrict
  external sharing of Drive/OneDrive; turn on DKIM and DMARC; set up
  account recovery.
- **One-page "something's wrong" plan**: who to call, how to sign
  everyone out, how to reset passwords, what to tell parents.
- **Questions to ask a vendor** before putting children's data in an
  app: MFA, data export and deletion, breach notification, where the
  data lives.
- **A "children's data" sharing audit guide**: how to find files shared
  publicly in Drive/OneDrive and lock them down.

### 2. Tools: read-only, run by or for the organization
1. **Domain checkup** (built in this PR): public email and website
   settings, explained in plain language. Uses only public information.
2. **Workspace / Microsoft 365 posture check** (next): run by the
   organization's own admin with their own credentials, read-only. How
   many accounts have MFA, how many admins exist, whether external
   sharing is open, which files are shared publicly. This is the
   highest-impact tool, because it measures the things that matter most
   (items 2 and 3 above), and they're invisible from outside.
3. **Monthly re-check**: a scheduled run of the checkup that flags
   regressions (the exit code already supports this).

### 3. Program: learn from real organizations
- **Pilot with three organizations** you know: a parish, a school, a
  childcare center. Run the checkup, walk through the first-hour guide
  with them, write down every place they get stuck. Their confusion is
  the roadmap.
- **Measure outcomes, not activity**: MFA enforced (yes/no), admin
  count, DMARC policy, publicly shared files found and fixed. Keep these
  numbers privately, in aggregate.
- **Then approach a diocese** with a working toolkit and three stories.

## Why the domain checkup first

To be honest: it's not the single highest-impact control. Enforced MFA is.
But it's the right *first build*, because:

- **It's safe by construction.** It reads only public DNS and loads the
  public homepage, the same information every mail server and browser
  sees. No credentials, no permission questions, no risk of breaking
  anything.
- **It targets the biggest dollar losses.** DMARC is what stops
  scammers sending email that looks like it's from you.
- **It opens conversations.** "Can I run a free five-minute check on
  your domain?" is an easy yes, and the report leads naturally to "now
  let's turn on MFA."
- **It teaches fundamentals**: DNS, email authentication, TLS
  certificates, and the discipline of not over-claiming.
- **It sets the pattern** (Finding → plain-language report → JSON) that
  the Workspace posture check will reuse.

The Workspace check needs OAuth setup and a test tenant, and is best
built alongside a pilot organization that wants it.
