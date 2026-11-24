# Passkey recipe for the people who move money

*For the office manager of a small school, parish or childcare center. Checked against Google and Microsoft's own help pages in November 2026. Screens change; if a button has moved, search the help page linked under it.*

## Why bother

A fake login page can pass your password and your text or app code to the real site in real time, then keep you signed in as you. Ordinary two-step codes don't stop that. A passkey or security key does, because it checks which website it is talking to and won't answer a fake one.

In 2025 a phishing email reached Sudbury (Massachusetts) Public Schools' payroll staff. The local paper reports the attackers got into payroll and email accounts, could "intercept multi-factor authentication (MFA) codes", changed four employees' direct-deposit details, and diverted $12,825.50 over two pay cycles. ([Sudbury Weekly, May 7, 2026](https://sudburyweekly.com/sps-hit-by-payroll-cyberattack-in-2025-over-12000-diverted/))

You don't need to do this for everyone. Do it for the 2 to 5 people who can move money or change accounts.

## Step 1: Make the short list (15 minutes)

Write down everyone who can do any of these:

- send a payment, wire or ACH from the bank
- change payroll or direct-deposit details
- add or change a vendor's bank details
- act as an administrator of your email system (Google Workspace or Microsoft 365)

That is your list. Usually it's the bookkeeper, the office manager, the principal or pastor, and whoever does IT.

## Step 2: Buy keys (about $30 each, two per person)

Buy **two** security keys per person on the list: one to carry, one sealed in an envelope in the safe.

| Key | Listed price | Notes |
|---|---|---|
| Yubico Security Key NFC (USB-A) or Security Key C NFC (USB-C) | $29 each | Stores passkeys (FIDO2). [yubico.com](https://www.yubico.com/product/security-key-series/) |
| Google Titan Security Key | $30 (USB-A) or $35 (USB-C) | Stores passkeys. [PCMag review, May 2026](https://tech.yahoo.com/cybersecurity/articles/google-titan-security-key-100000396.html) |

Pick the plug that fits the computers people use. The NFC versions also tap against most phones.

A passkey saved on a phone or laptop also works, and costs nothing. Keys are recommended for this short list because they are easy to count, easy to store as a backup, and don't leave with a personal phone.

## Step 3: Find out which system and plan you have

- **Google:** sign in at admin.google.com. Your edition is under Menu > Billing > Subscriptions.
- **Microsoft:** sign in at entra.microsoft.com or admin.microsoft.com. Your licenses are under Billing > Your products.

Then follow Part A (Google) or Part B (Microsoft).

---

## Part A: Google Workspace

**What your edition gets.** Google's edition comparison pages list 2-Step Verification and security keys on Business Starter, Standard and Plus, and on Education Fundamentals, Standard and Plus. ([Business](https://knowledge.workspace.google.com/admin/getting-started/editions/compare-business-editions?hl=en), [Education](https://knowledge.workspace.google.com/admin/getting-started/editions/compare-education-editions?hl=en)) The setting below is the one that matters. *Not yet confirmed: the Nonprofits edition, and that every edition offers the "Only security key" choice (see the sources file).*

### A1. Put the short list in its own group

1. In the Admin console, go to **Menu > Directory > Organizational units** and create one called *Money movers*.
2. Move the people on your list into it (**Directory > Users**, select them, **Change organizational unit**).

This lets you make the stricter rule apply only to them. Google: "To apply the setting only to some users, at the side, select an organizational unit." ([Deploy 2-Step Verification](https://knowledge.workspace.google.com/admin/security/deploy-2-step-verification))

### A2. Have each person add both keys (before you enforce anything)

Sit with each person for 10 minutes:

1. They go to **myaccount.google.com > Security > 2-Step Verification**.
2. Add a **security key** (or passkey). Plug in key #1, touch it, name it "Carry".
3. Repeat with key #2, name it "Safe".
4. Have them sign out and back in with each key to prove both work.
5. Seal key #2 in an envelope with their name and the date. Put it in the safe.

### A3. Require keys for that group only

Go to **Menu > Security > Authentication > 2-step verification** (you need to be a super administrator). ([Google](https://knowledge.workspace.google.com/admin/security/deploy-2-step-verification))

1. On the left, select the **Money movers** unit.
2. Tick **Allow users to turn on 2-Step Verification**.
3. **Enforcement:** On.
4. **Methods:** choose **Only security key**. Google's page says this option accepts passkeys as well as security keys.
5. **Allow user to trust device:** leave off.
6. **2-Step Verification policy suspension grace period:** pick a short one (1 day). Google asks you to set this when you choose Only security key.
7. Click **Override**, then **Save**.

This step is what turns off the weaker fallbacks (text codes, phone calls, app prompts) for these people. If you skip it, a phisher can still ask for a text code.

### A4. Optional, for your super administrators: Advanced Protection

Google's Advanced Protection Program adds strict account recovery, deeper Gmail scanning and limits on outside apps. Turn on enrollment at **Menu > Security > Authentication > Advanced Protection Program**, select the unit, keep **Enable user enrollment**. ([Google](https://knowledge.workspace.google.com/admin/security/enable-user-enrollment-in-the-advanced-protection-program)) Worth it for the IT person; optional for the bookkeeper.

### A5. If someone loses a key

1. They use the sealed key #2 from the safe.
2. If both are gone, another administrator goes to **Directory > Users >** (their name) **> Security > 2-step verification > Get Backup Verification Codes** and reads them one code. Under Only security key, people can't make their own backup codes, and Google says they can enter an admin-generated one "during the grace period" you set in A3. So generate the code at the moment it's needed and have them add a new key right away; don't pre-print codes for the safe. ([Google](https://knowledge.workspace.google.com/admin/security/recover-an-account-protected-by-2-step-verification))
3. Only a super administrator can do this for another administrator, so **have two super administrators**, each with two keys.
4. Buy a replacement and remove the lost key from their account.

---

## Part B: Microsoft 365

### What's free and what costs money

- **Passkeys and security keys are free on every plan.** Microsoft: "Passkeys (FIDO2) are available in all Microsoft Entra ID editions, including Microsoft Entra ID Free. No extra licenses are required." ([Microsoft Learn](https://learn.microsoft.com/en-us/entra/identity/authentication/how-to-enable-passkey-fido2))
- **Requiring them costs money.** Forcing a person to use a passkey (and refusing app prompts and codes) is done with Conditional Access, and "to use Conditional Access, your tenant needs to have Microsoft Entra ID P1 license." ([Microsoft Learn](https://learn.microsoft.com/entra/identity/authentication/concept-authentication-strengths)) P1 is included in **Microsoft 365 Business Premium** and E3/E5 ([licensing page](https://learn.microsoft.com/en-gb/entra/identity/authentication/concept-mfa-licensing)), or sold alone at a listed $7.00 per user per month, paid yearly ([Microsoft pricing](https://www.microsoft.com/en-us/security/microsoft-entra-pricing)). For nonprofits, the free Business Premium grant ended in 2025; the project's research found Business Premium at about $5.50 per user per month after the nonprofit discount (*not re-checked on Microsoft's page*). Every person covered by a Conditional Access policy needs that license, so licensing just the short list keeps the cost to a few seats.
- **Free "security defaults"** turn on app-based MFA for everyone but can't require passkeys, and you can't customize them. ([Microsoft Learn](https://learn.microsoft.com/entra/fundamentals/security-defaults))

### The deadline that makes this timely

Microsoft is retiring its own text-message and voice-call codes:

- **September 1, 2026:** passkeys become the default sign-in experience and are switched on for people who use text or voice codes.
- **February 1, 2027:** Microsoft-provided text and voice codes end for all users except Global Administrators and outside users. Anyone whose only method is text or voice must register a passkey at sign-in; "This prompt is blocking."
- **July 1, 2027:** the same for Global Administrators and outside users.

This covers sign-in codes and self-service password reset, in Microsoft's public cloud (including GCC). Organizations that insist can pay a separate telephone provider to keep text codes. ([Microsoft Learn: SMS and voice retirement](https://learn.microsoft.com/en-au/entra/identity/authentication/concept-sms-voice-retirement), [FAQ](https://learn.microsoft.com/en-us/entra/identity/authentication/concept-sms-voice-retirement-faq))

So everyone has to move off text codes anyway. Moving the money movers to keys at the same time costs little extra.

### B1. Turn on passkeys (free, every plan)

You need at least the Authentication Policy Administrator role.

1. Go to **entra.microsoft.com > Entra ID > Security > Authentication methods > Policies**.
2. Select **Passkey (FIDO2)**.
3. On **Enable and Target**, turn it on and target a group containing your short list (or All users).
4. On **Configure**, set **Allow self-service set up** to Yes. Leave **Enforce key restrictions** off unless you know the key models.
5. Save.

([Microsoft Learn](https://learn.microsoft.com/en-us/entra/identity/authentication/how-to-enable-passkey-fido2)) Microsoft may show a banner asking you to opt in to "passkey profiles". That's fine; note that "after you opt in to enable passkey profiles, you can't opt out."

### B2. Have each person add both keys

Sit with each person:

1. Go to **mysignins.microsoft.com/security-info** and sign in.
2. **Add sign-in method > Choose a method > Passkey > Next.**
3. When asked where to save it, choose **Use another device** or **More options**, then **Security key**. Plug in key #1, set a PIN, touch it. Name it "Carry".
4. Repeat for key #2, name it "Safe". Seal it in the safe.

([Microsoft Learn](https://learn.microsoft.com/entra/identity/authentication/how-to-register-passkey-with-security-key)) Microsoft requires the person to have completed MFA in the last five minutes before adding a passkey.

### B3. Require keys for the short list (needs P1)

If you have Business Premium, or buy P1 for the short list:

1. **Make two emergency ("break-glass") admin accounts first.** Microsoft recommends "two cloud-only emergency access accounts permanently assigned the Global Administrator role." Give each a long password written down and sealed, plus its own key. ([Microsoft Learn](https://learn.microsoft.com/entra/fundamentals/security-defaults))
2. Go to **Entra ID > Conditional Access > Policies > New policy**. (You need at least the Conditional Access Administrator role.)
3. **Users:** include the short-list group (and the administrator roles). **Exclude** the two emergency accounts.
4. **Target resources:** All resources.
5. **Grant:** **Require authentication strength > Phishing-resistant MFA strength.**
6. **Enable policy: Report-only.** Save. Watch the sign-in logs for a week, then switch to **On**.

([Microsoft Learn](https://learn.microsoft.com/entra/identity/conditional-access/policy-admin-phish-resistant-mfa)) Microsoft warns that turning this on before people have registered keys "risks locking you out of your tenant."

**Watch out:** Conditional Access and security defaults can't both be on. Microsoft: organizations that use Conditional Access "must disable security defaults." If you turn security defaults off, add a Conditional Access policy requiring MFA for everyone else too, or the rest of your staff lose MFA.

### B4. Turn off text and voice codes for the short list

In **Entra ID > Authentication methods > Policies**, the policy has controls for **SMS** and **Voice calls**; exclude the short-list group from both (or turn them off for everyone once others have moved). ([Microsoft Learn](https://learn.microsoft.com/en-us/entra/identity/authentication/how-to-authentication-methods-manage)) Microsoft warns that disabling a method people already use means they must register a new one, so do this after B2.

### B5. No P1? Do this much anyway

Without P1 you can't force keys, but you can still:

- turn on passkeys (B1) and give the short list keys (B2),
- turn off SMS and voice for them (B4),
- ask them to always choose the key at sign-in.

That removes text codes, but a phisher could still talk someone into approving an app prompt. Say so plainly to the organization so they can decide on P1.

### B6. If someone loses a key

1. They use the sealed key #2.
2. If both are gone, an administrator can issue a Temporary Access Pass so they can register a new key (Microsoft names this as the way to register passwordless methods safely).
3. Remove the lost key from their Security info.

---

## What keys don't stop

Two tricks get around even a passkey, because the person signs in on the *real* site:

- **"Enter this code" phishing (device code).** A fake meeting invite asks the person to type a code at the genuine Microsoft sign-in page, which hands the attacker a session. Microsoft's free security defaults block this; with P1, add a Conditional Access policy that blocks device code flow.
- **"Allow this app to access your account."** An approved app keeps access until someone removes it. On both systems, turn off users' ability to approve outside apps themselves and have an administrator approve them.

Tell the short list: if a sign-in screen asks you to type a code someone sent you, or to allow an app you didn't install, stop and call the office.

## Step 4: The recovery envelope (both systems)

For each person, one sealed envelope in the safe holds:

- their second key, labeled
- the date it was sealed and who sealed it

For the organization, one more envelope holds the two emergency/super-admin account names and passwords, and their keys.

Check the envelopes once a year, at the same time you update the access list.

## Step 5: Ten-minute check that it worked

- [ ] Each person on the list has two keys registered, and both have been tested.
- [ ] Google: the Money movers unit shows **Only security key**. Microsoft: the Conditional Access policy is **On**, not report-only.
- [ ] Text and voice codes are off for these people.
- [ ] Two administrators can recover each other.
- [ ] The envelopes are in the safe.

---

*Sources and anything not yet confirmed: see [the fact check](../research/money-movers-fact-check-2026-11.md).*
