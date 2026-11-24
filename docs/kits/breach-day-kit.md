# Breach-day kit

For a school, parish, childcare center or youth program with no IT staff.
Prepare it on a calm day, print it, and keep **two copies in two places**
(for example, the office safe and the pastor's or director's home). On the day
something goes wrong, your email may be the thing that's broken, so this kit
must not live only in email or a shared drive.

It has four parts:

1. [Fill in before anything happens](#1-fill-in-before-anything-happens)
2. [The first hour](#2-the-first-hour): one decision tree per kind of incident
3. [Saving the evidence](#3-saving-the-evidence) before it disappears
4. [Letters to families](#4-letters-to-families), including what to do if
   criminals contact parents

---

## 1. Fill in before anything happens

### Who to call

| Who | Name | Phone (not email) |
|---|---|---|
| Our bank's fraud hotline | | |
| Our insurer's breach hotline (on the cyber policy, or the diocese's policy) | | |
| Whoever manages our email and accounts | | |
| A second admin who can sign in if the first can't | | |
| Our payroll provider | | |
| The diocese or network office (if we have one) | | |
| A lawyer we can call | | |
| FBI: file at **ic3.gov**; local field office phone | | |
| CISA: report at **cisa.gov/report**; 888-282-0870 | | |

Call the **insurer before hiring anyone**. Many policies only pay for
responders they approve.

### Where children's information lives

List every system that holds information about children or families: the
student or childcare system, tuition and financial-aid platform, email, shared
drives, pickup or attendance apps, photo galleries, parish directory, group
texting lists. Mark the ones holding the most sensitive records: counseling
notes, special-education or medical files, custody orders, safeguarding
reports.

| System | What it holds | Who is the admin | Most sensitive? |
|---|---|---|---|
| | | | |

### Emergency sign-in, sealed

Print backup codes for each admin account and seal them in an envelope with
this kit. Note where any spare security keys are. Re-check twice a year.

---

## 2. The first hour

Work through the matching tree. Write down what you do and when (use the log
sheet at the end).

### A. Someone's email account has been taken over

Signs: people receive strange emails from that account, the user is locked
out, new forwarding rules appear, or there are sign-ins from unexpected
places.

1. **Save the evidence first** (Part 3). Resetting the password can make it
   harder to see what happened.
2. Reset the password and **sign the account out everywhere**.
   Google Admin console: the user's page → Security → Sign-in cookies →
   Reset. Microsoft Entra admin center: the user → Revoke sessions.
3. Check the account for **forwarding rules and filters** the attacker added,
   and remove them.
4. Check for **apps the user approved** recently, and remove unknown ones.
5. Re-enroll the user in two-step sign-in, ideally with a passkey.
6. Warn the people the account emailed: a short note saying not to act on
   messages sent from it during the incident.
7. If the account handles money, also run tree B.

### B. Money was sent somewhere it shouldn't have been

The first hours decide whether the money comes back.

1. **Call the bank's fraud line now.** Ask for a wire recall or ACH reversal.
2. **File at ic3.gov today.** The FBI's Recovery Asset Team froze about 66%
   of the money in cases reported quickly enough in 2024.
3. Call the insurer's breach hotline.
4. Run tree A on whatever email account the request came through.
5. Do not pay a "corrected" invoice until the vendor is reached on a number
   already on file.

### C. A computer shows a ransom note or files won't open

1. **Unplug it from the network** (cable out, Wi-Fi off). Don't turn it off;
   responders may need what's in memory.
2. Don't pay and don't contact the attackers.
3. Call the insurer, then whoever manages your IT.
4. Check whether the shared drive or cloud folders that computer syncs are
   affected. Cloud services keep earlier versions: Microsoft OneDrive can
   restore a whole folder to how it was within the last 30 days, and Google
   Drive keeps earlier versions of files for a limited time.

### D. Criminals contact parents or students

Recent attacks on PowerSchool (2025) and a UK nursery chain (2025) went
straight to families after the organization was breached. Paying did not get
the data deleted.

1. Send families the **extortion letter** (Part 4) the same day.
2. Report the messages to ic3.gov and keep copies.
3. Call the insurer and, if one applies, your lawyer, about formal breach
   notices.
4. Find out which records were taken. Check the sensitive systems listed
   above first.

### E. A device or paper files are lost or stolen

1. Write down what was on it and whether it was encrypted and locked with a
   password.
2. Remotely sign it out or wipe it if you can (Google or Microsoft device
   management, or Find My).
3. Report a theft to the police and keep the report number.
4. Ask your lawyer or insurer whether families must be notified.

---

## 3. Saving the evidence

Logs disappear. Microsoft's free tier keeps sign-in history for **7 days**
(30 days with Entra ID P1); Google keeps most audit logs about 6 months. Small
organizations usually notice a problem weeks later, so **export logs on a
schedule**, not just on the day.

### Monthly (10 minutes)

**Google Workspace:** Admin console → Reporting → Audit and investigation →
**Login log events**, and also **Admin log events**. Set the date range to the
last month and choose **Export all** (to Sheets or CSV). Save to a folder that
only two admins can open.
([Google: Admin log events](https://support.google.com/a/answer/4579579))

**Microsoft 365:** Microsoft Entra admin center → Monitoring & health →
**Sign-in logs** → Download (CSV). Then Microsoft Purview portal → **Audit** →
new search for the last month → Export. Save as above.

### On breach day, before resetting anything

Export the same logs for the affected accounts covering the last 30 days, and
take screenshots of anything strange (forwarding rules, unknown apps, sign-in
locations). Note the time you took each.

---

## 4. Letters to families

Ask your lawyer or insurer whether you're legally required to send a formal
notice, and by when. New York, for example, requires notice to affected
residents within 30 days. These letters are plain-language companions, not a
substitute for any required notice.

### If someone contacts you claiming to have your child's information

> Dear families,
>
> On [date] we learned that [briefly: an outside party gained access to some of
> our records]. Some families may receive emails, texts or calls from people
> claiming to have their child's information and demanding money.
>
> **If you are contacted:**
> - Do not reply, click links, or pay. Paying does not guarantee anything is
>   deleted.
> - Keep the message and report it at **ic3.gov**, the FBI's Internet Crime
>   Complaint Center.
> - Tell us, so we can track what is happening: [contact].
>
> We are working with [our insurer / law enforcement / experts] and will
> update you by [date].
>
> [Name], [role]

### How to protect your child's credit (any breach involving children)

> A child's personal information can be misused for years before anyone
> notices, often when the child first applies for credit at 18. You can
> prevent this for free:
>
> **Freeze your child's credit.** For children under 16, parents can place a
> free credit freeze with each of the three credit bureaus: Equifax, Experian
> and TransUnion. Contact each one separately. Each will ask for proof of who
> you are and proof that you're the parent or guardian, such as the child's
> birth certificate. The FTC explains the steps at
> **consumer.ftc.gov** (search "credit freeze minors").
> ([FTC](https://consumer.ftc.gov/new-protections-available-minors-under-16))
>
> A freeze stops new accounts being opened in your child's name. It doesn't
> affect anything else, and you can lift it later.

---

## Incident log sheet

| Time | What happened or what we did | Who |
|---|---|---|
| | | |
| | | |
| | | |

_General guidance only, not legal advice or a security assessment. Menu names
change; if one differs, search the admin console for the setting's name._
