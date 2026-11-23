# Your first hour: Google Workspace

For the person who "does the IT" at a parish, school, childcare center or
small nonprofit that uses Google Workspace (your email ends in your own
domain, like `office@stmarys.org`, and you sign in to Gmail with it).

Five steps, in order. Each one says **why** in a sentence, **where** to
click, and **what can go wrong**. You don't need to finish in one sitting;
step 1 takes a couple of weeks to roll out to everyone.

> **Menus move.** These paths were checked against Google's help pages in
> November 2026. If a menu looks different, search the linked help page
> title in the Admin console's search bar, which finds settings by name.

**Not sure you use Google Workspace?** Run the [checkup](../../checkup/README.md)
on your domain: it tells you who handles your email.

**Everyone uses personal @gmail.com addresses?** Then there's no Admin
console, and no way to remove access when someone leaves. Moving to your
own Workspace is the biggest upgrade available to you. It can be free:

- Schools: Google Workspace for Education Fundamentals, through [Google for Education](https://edu.google.com/).
- Nonprofits, including many churches: [Google for Nonprofits](https://www.google.com/nonprofits/).
  Most US Catholic parishes are covered by the USCCB group exemption
  rather than their own IRS letter; Google has a page for exactly that
  case: [You are a church with group exemption](https://support.google.com/nonprofits/answer/9932981).
  Ask your diocese first, since some provide Workspace for their parishes.

---

## Before you start (5 minutes): don't lock yourself out

You'll be changing sign-in settings, so first make sure there's a way
back in if something goes wrong.

1. Sign in at [admin.google.com](https://admin.google.com). If you can't
   get in, you aren't an admin; find out who is.
2. **Make sure two different people are super admins.** If you're the
   only one and you lose your phone, recovering the whole organization
   can take days. ([Google's admin best practices](https://support.google.com/a/answer/9011373))
3. On your own admin account, add a **recovery phone and email** and
   **print backup codes**. Keep them somewhere physical and safe, like
   the office safe, not in a file in the same account.
   ([Add recovery information](https://support.google.com/a/answer/3033063))

Google now requires two-step sign-in on admin accounts itself, so
setting it up on yours now saves a surprise later.
([About 2SV enforcement for admins](https://support.google.com/a/answer/16271818))

---

## Step 1. Turn on two-step sign-in for everyone

**Why:** A stolen password is the most common way into an organization's
email, and from email into everything else. Two-step sign-in (2SV) stops
nearly all of those attempts.

**Where:** Admin console → **Security → Authentication → 2-step verification**

1. Check **Allow users to turn on 2-Step Verification** and save. This
   alone changes nothing for anyone; it just makes it possible.
2. **Tell people before you enforce it.** Send an email (template below)
   asking everyone to turn it on within two weeks.
3. Set **Enforcement** to **On from** a date about two weeks out.
4. Set a **New user enrollment period** of about a week, so new staff
   can sign in once to set it up.
5. Under methods, allow passkeys, security keys and the Google prompt
   on a phone. Avoid text-message codes if you can: they're the weakest
   method. If an older volunteer has no smartphone, a security key
   (about $25) is the simplest option of all.

**Check progress:** **Reporting → User reports → Security** shows who has
2SV turned on. Nudge whoever hasn't before the date.

**What can go wrong:** Anyone who hasn't enrolled by the enforcement date
can't sign in until an admin helps. You can generate backup codes for
them (**Directory → Users →** their name **→ Security**). Google's guide:
[Avoid account lockouts when 2SV is enforced](https://support.google.com/a/answer/9176805).

<details>
<summary>Email template</summary>

> Subject: Please turn on two-step sign-in by [date]
>
> To protect our [families'/students'/parishioners'] information, we're
> turning on two-step sign-in for every account. After you type your
> password, you'll confirm it's really you with your phone or a key.
>
> Please set it up before [date]: go to myaccount.google.com/security,
> click "2-Step Verification", and follow the steps. It takes about
> five minutes. After [date], accounts without it won't be able to sign in.
>
> If you don't have a smartphone or get stuck, reply to this email and
> I'll help.
</details>

---

## Step 2. Know exactly who has access

**Why:** Former staff, old volunteers and shared passwords are open
doors. An admin account in the wrong hands controls everything.

**Where:** Admin console → **Directory → Users**

1. Go through the list. **Suspend** anyone who has left: suspending
   blocks sign-in but keeps their email and files. Make "suspend on the
   last day" a standing rule.
2. **Replace shared passwords.** If three people sign in to
   `office@stmarys.org` with one password, make it a
   [Google Group](https://support.google.com/a/answer/9400082) or use
   [mail delegation](https://support.google.com/mail/answer/138350)
   so each person uses their own account with their own two-step sign-in.
   (Delegation must first be allowed under **Apps → Google Workspace →
   Gmail → User settings → Mail delegation**;
   [details](https://support.google.com/a/answer/7223765).)

Then go to **Account → Admin roles**, click **Super Admin**, and look at
who's listed.

3. Keep **two or three** super admins: different people, all of whom
   you trust and who actually need it. Remove the rest, or give them a
   smaller role.
4. Ideally, super admins use a separate admin account (for example
   `admin-maria@stmarys.org`) only for admin work, and their everyday
   account for email. That keeps the most powerful account away from
   phishing emails.

---

## Step 3. Stop children's information leaking through sharing

**Why:** The most common way student and family data actually leaks is
a spreadsheet shared as "anyone with the link": an allergy list, a
pickup authorization sheet, an enrollment form's responses. No hacker
needed. The link gets forwarded, posted, or found.

**Where:** Admin console → **Apps → Google Workspace → Drive and Docs →
Sharing settings → Sharing options**

1. Turn on the **warning when files are shared outside your
   organization**. This catches most accidents.
2. Strongly consider turning **off** the option that lets people make
   files **visible to anyone with the link**. People inside your
   organization can still share with each other, and with specific
   outside people by email address.
3. If your console shows **Trust rules** instead of these options,
   Google has moved this setting to the **Rules** page.
   ([Trust rules for Drive sharing](https://support.google.com/a/answer/10621317))

**Finding files that are already public is harder than it should be.**
The Admin console's **Reporting → Audit and investigation → Drive log
events** (filter **Visibility** → **Shared externally**) shows sharing
*events*, but not every file's current state, and what's logged depends
on your edition. ([Investigate file sharing](https://support.google.com/a/answer/7584076))
A simple step that works everywhere: ask each staff member to spend ten
minutes opening their spreadsheets and forms that contain children's
information, clicking **Share**, and making sure it says **Restricted**
or your organization's name.

> A read-only tool to list every publicly shared file is on this
> project's [roadmap](../DIRECTION.md).

**If you run a school:** put students and staff in separate
[organizational units](https://support.google.com/a/answer/4352075) so
you can give students stricter settings. For example, students can't
share outside the school or email outside it. Google for Education's
help pages cover the age-based settings for users under 18.

---

## Step 4. Stop people sending email pretending to be you

**Why:** Fake email "from the principal" or "from the parish office"
asking someone to pay an invoice or change bank details is the most
expensive scam small organizations face. Two settings make it much harder.

1. **Turn on DKIM** (Google leaves it off by default):
   Admin console → **Apps → Google Workspace → Gmail → Authenticate
   email**. Click **Generate new record**, add the record it shows you
   at your domain host (wherever you bought your domain), then click
   **Start authentication**. It can take up to 48 hours to start
   working; if it says "Not authenticating", check the record and try
   again the next day. ([Set up DKIM](https://support.google.com/a/answer/174124))
2. **Add a DMARC record** at your domain host, about two days after
   DKIM is working. First create a Google Group (for example
   `dmarc-reports@`) to receive the reports, so they don't flood anyone's
   inbox. Then start with `v=DMARC1; p=none; rua=mailto:dmarc-reports@yourdomain.org`
   and tighten it to `p=quarantine`, then `p=reject`, over a few weeks.
   ([Set up DMARC](https://support.google.com/a/answer/2466580),
   [recommended rollout](https://support.google.com/a/answer/10032473))
3. Run the [checkup](../../checkup/README.md) afterwards. It tells you
   what's working and what's left.

Even with all this, keep the human rule: **confirm any request to
change bank details or send money by calling a number you already have.**

---

## Step 5. Make sure someone hears the alarm

**Why:** Google already detects suspicious sign-ins, leaked passwords
and accounts sending spam. That only helps if the alert reaches a person.

**Where:** Admin console → **Rules**

1. Look at the **system-defined** alert rules (things like suspicious
   login, leaked password, user suspended for suspicious activity).
2. Make sure their email notifications go to an address someone reads,
   ideally two people.
3. Glance at **Security → Alert center** once a month.

---

## You're done with the first hour

- [ ] Two super admins, each with recovery info and backup codes
- [ ] Two-step sign-in allowed, announced, and enforced from a date
- [ ] Former staff suspended; no shared passwords
- [ ] Two or three super admins, no more
- [ ] External-sharing warning on; "anyone with the link" off or restricted
- [ ] Staff checked their own files containing children's information
- [ ] DKIM on; DMARC record added
- [ ] Alert emails go to someone who reads them

**Next:** Google's own [security checklist for small businesses](https://support.google.com/a/answer/9211704)
goes further. Revisit this page once a year, and whenever your office
manager changes.

---

_General guidance only, not a security assessment of your organization.
Licensed [CC BY 4.0](https://creativecommons.org/licenses/by/4.0/): share
and adapt freely with credit._
