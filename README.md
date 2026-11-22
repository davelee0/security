# Security Basics for Small Nonprofits

A plain-language security checklist for small nonprofits, parishes and
small businesses that have no IT or security staff.

Most attacks on small organizations aren't clever. They use a reused
password, an unpatched website plugin or a convincing email about a
"changed bank account." This checklist covers the few habits that stop
most of them.

Started by Dave ([@davelee0](https://github.com/davelee0)) in November 2026. Work in progress.

## Who this is for

The volunteer, office manager or pastor who ends up "doing the IT."
No technical background needed.

## The checklist

### Accounts
- [ ] Turn on two-step sign-in (MFA) for email, banking, donations and
      your website. Prefer a passkey or security key over text messages.
- [ ] Use a password manager, and never reuse a password.
- [ ] Remove access the same day a staff member or volunteer leaves.
- [ ] Keep admin access to as few people as possible.

### Email and payments
- [ ] Confirm any request to change bank details or pay an invoice by
      calling a number you already have, never one in the email.
- [ ] Set up SPF, DKIM and DMARC for your domain so others can't easily
      send email as you.
- [ ] Take donations through a payment processor. Never store card
      numbers yourself.

### Devices
- [ ] Turn on automatic updates for computers, phones and browsers.
- [ ] Turn on disk encryption and a screen lock on every laptop.
- [ ] Replace devices that no longer get security updates.

### Website
- [ ] Keep your website platform, theme and plugins updated, and delete
      plugins you don't use.
- [ ] Make sure every page loads over HTTPS.
- [ ] Know who has admin access, and turn on MFA for each of them.

### Backups
- [ ] Back up important files automatically, with one copy offline or
      in a separate account.
- [ ] Test restoring a file at least twice a year.

### If something goes wrong
- [ ] Write down who to call: your bank, your website host, and someone
      who can help with a breach.
- [ ] Know how to reset passwords and sign everyone out of email.

## Check your own domain

[`checkup`](checkup/README.md) looks at your domain's public email and
website settings and tells you, in plain language, what to fix first.
It reads only public information.

```
python -m checkup yourparish.org
```

## Roadmap

See [docs/DIRECTION.md](docs/DIRECTION.md) for the reasoning behind
these priorities.

- [x] A self-assessment script for checking your own domain's email and
      website settings ([checkup](checkup/README.md))
- [ ] "Your first hour" guides for Google Workspace and Microsoft 365
- [ ] A one-page "something's wrong" plan
- [ ] Questions to ask before putting children's data in an app
- [ ] A read-only Workspace / Microsoft 365 check (MFA, admins, sharing)
- [ ] A one-page printable version

## Disclaimer

General guidance only, not a security assessment of your organization.

## License

This work is licensed under [CC BY 4.0](https://creativecommons.org/licenses/by/4.0/).
See [LICENSE](LICENSE).
