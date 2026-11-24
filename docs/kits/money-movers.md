# Money-movers kit

For the two to five people at a school, parish, childcare center or youth
program who can **move money or change who gets paid**: the bookkeeper, the
business manager, the pastor or director who approves payments, and whoever
administers email.

Most money lost by small organizations isn't lost to ransomware. It's lost to
email fraud: a fake "we've changed our bank account" from a vendor, or a
payroll redirect after someone's email is taken over. Email and payment fraud
makes up roughly 58–60% of small-business cyber insurance claims, and single
school incidents have run from $1.3M to $4.9M. This kit closes the two doors
those attacks use: **the sign-in** and **the payment change**.

Allow one afternoon for Part 1 and one staff meeting for Part 2.

---

## Part 1. Give the money-movers sign-in that can't be phished

### Why ordinary two-step sign-in isn't enough for these people

Phishing kits now put a fake login page between the user and the real site.
The user types their password and code, the kit passes both through in real
time, and the attacker keeps the logged-in session. In Sudbury,
Massachusetts (2025), attackers did exactly this and redirected payroll.

**Passkeys and hardware security keys stop this.** The key checks which
website it's talking to, so a fake site gets nothing it can use. Text-message
codes, voice calls and app prompts don't have that check.

### What you need

- The list of money-movers and admins (usually 2–5 names).
- For each person, either a phone or computer that supports passkeys, or a
  hardware security key. Buy **two keys per person** (one daily, one locked
  away as a spare). Keys that support FIDO2 typically cost $25–$50 each.

### Google Workspace

1. **Put the money-movers in their own group or organizational unit**, so
   stricter settings apply only to them.
2. **Have each person add a passkey or security key** at
   myaccount.google.com → Security → Passkeys and security keys.
3. **Require it.** Admin console → Security → Authentication → 2-step
   verification. For the money-movers' group, set the allowed method to
   **Only security key**. This option accepts passkeys as well as hardware
   keys. ([Google: Deploy 2-Step Verification](https://support.google.com/a/answer/9176657))
4. **Generate backup codes for each person and lock them away.** Under "Only
   security key," users can't create their own backup codes; an admin has to.
5. Optional: let them **skip the password** and sign in with the passkey
   alone. Admin console → Security → Authentication → Passwordless.
   ([Google: Allow users to skip passwords](https://support.google.com/a/answer/13529161))

### Microsoft 365

1. **Turn on passkeys.** Microsoft Entra admin center → Authentication
   methods → Policies → **Passkey (FIDO2)** → enable it for the money-movers'
   group. This works on every Microsoft tier, including the free one.
   ([Microsoft: Enable passkeys](https://learn.microsoft.com/en-us/entra/identity/authentication/how-to-authentication-passkeys-fido2))
2. **Have each person register a passkey or key** at mysignins.microsoft.com
   → Security info → Add sign-in method.
3. **Remove the weaker methods for these people.** In the same Authentication
   methods policies, turn off SMS and voice call for the money-movers' group.
   A passkey only protects someone if the attacker can't fall back to a
   weaker method.
4. **Forcing passkeys requires Conditional Access**, which needs Microsoft
   Entra ID P1 (included in Microsoft 365 Business Premium). You don't need
   it for the whole organization: license only the money-movers. At nonprofit
   pricing, Business Premium is listed at about $5.50 per user per month.
   Then create a Conditional Access policy that requires the built-in
   **Phishing-resistant MFA** authentication strength for that group.
   ([Microsoft: Authentication strengths](https://learn.microsoft.com/en-us/entra/identity/authentication/concept-authentication-strengths))

Microsoft has signaled it will retire text-message and voice codes as
Microsoft-managed MFA methods; one industry analysis puts the date at
February 1, 2027. Check Microsoft's current announcements, but moving the
money-movers now gets ahead of it either way.

### Check that it worked

- Ask each person to sign in on a new browser. They should be asked for the
  passkey or key, and nothing weaker should be offered.
- In Google, Reporting → User reports → Security shows each user's 2-step
  verification methods. In Microsoft, the user's Authentication methods page
  in the Entra admin center lists what's registered.

---

## Part 2. The payment-change rule

Adopt this as a written rule, signed by whoever approves payments. Post it
where the bookkeeper works.

> **Any request to change where we send money is treated as possible fraud
> until confirmed.** This includes a vendor's new bank account, an employee's
> new direct-deposit account, or an "urgent" payment request from a leader.
>
> 1. **Hold.** No change or urgent payment takes effect the day it's
>    requested.
> 2. **Call back** on a phone number we already have on file. Never use a
>    number, link or contact given in the request itself.
> 3. **Use the code word.** For our own staff and leaders, the caller must
>    give our pre-agreed code word. A familiar voice is not proof: voices can
>    now be cloned from a few seconds of audio.
> 4. **Second approver.** A second named person approves the change before it
>    takes effect.
> 5. **Tell the old contact.** After any bank-detail change, send a notice to
>    the vendor's or employee's previous email address on file, so a fraud is
>    noticed quickly.
>
> No one, including the pastor, principal or board chair, can waive this rule
> by email, text or phone.

### Ask your bank

Call the bank's business or treasury services line and ask:

- Do you offer **ACH positive pay** or **ACH debit blocks**? (Typically
  $20–$75 per month per account.)
- Can you require **dual approval** for new payees and wires in online
  banking?
- What is your **fraud hotline**, and how fast can you recall a wire?

Write the fraud hotline into the [breach-day kit](breach-day-kit.md).

If you use a payroll provider such as ADP or Paychex, ask whether it notifies
employees when their direct-deposit details change. ADP does; confirm for
yours.

### If money has already gone

Speed matters more than anything else. In 2024 the FBI's Recovery Asset Team
froze about 66% of the money in cases reported quickly enough.

1. **Call your bank's fraud line now** and ask for a wire recall.
2. **File at ic3.gov**, the FBI's Internet Crime Complaint Center, the same
   day.
3. **Call your insurer's breach hotline** before hiring anyone.
4. Then follow the [breach-day kit](breach-day-kit.md).

---

## Part 3. Practice saying no: a 10-minute drill

Rules fail under pressure. The drill makes the script automatic. Copy the
prompt below into Claude (or a similar assistant), and let the bookkeeper
practice. It works best once a quarter, and right before tuition and payroll
deadlines.

```text
You are helping the bookkeeper at a small school practice resisting payment
fraud. Play a caller or emailer who wants a payment change. Pick one scenario
at random each round:
 - a long-time vendor whose "bank changed" and who needs this month's invoice
   paid to the new account today;
 - the principal or pastor, calling from "a conference," who needs an urgent
   wire sent before end of day and can't talk long;
 - a staff member asking to move their direct deposit before Friday's payroll.

Be realistic and persistent, and use pressure (urgency, authority, mild
guilt), but never ask for passwords. Stay in character until the bookkeeper
either (a) follows our rule: hold, call back on the number on file, ask for
the code word, second approver; or (b) gives in.

Then step out of character and give short feedback: what they did well, the
moment the pressure worked, and the exact sentence they could use next time.
Keep each round under five exchanges.
```

The drill only practices the script. It never touches real accounts, and it
shouldn't be given real names, account numbers or the actual code word.

---

## One-page checklist

- [ ] Money-movers and admins listed (2–5 people)
- [ ] Two passkeys or keys per person, spare locked away
- [ ] Google: "Only security key" for their group, backup codes stored
- [ ] Microsoft: passkeys on, SMS and voice off for their group; Conditional
      Access with phishing-resistant strength (Business Premium for them only)
- [ ] Payment-change rule signed and posted
- [ ] Code word agreed and shared in person, never by email
- [ ] Bank asked about positive pay, dual approval and the fraud hotline
- [ ] First drill done; next one on the calendar

_General guidance only, not a security assessment. Menu names change; if one
differs, search the admin console for the setting's name._
