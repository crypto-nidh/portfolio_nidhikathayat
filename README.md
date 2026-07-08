# Nidhi Kathayat — Portfolio (Flask + HTML/CSS/JS)

A dynamic portfolio site. Content lives in `data.py` (edit that file to update
your info — no HTML editing needed), and the contact form on the site sends
messages straight to your email using Python's `smtplib`, with every
submission also backed up in a local SQLite database (`contacts.db`).

## Project structure

```
portfolio_app/
├── app.py              Flask app + contact form + email sending
├── data.py              All site content (about, experience, projects, etc.)
├── requirements.txt
├── .env.example         Copy to .env and fill in your real values
├── templates/
│   └── index.html       Jinja template (loops over data.py)
├── static/
│   ├── style.css
│   └── script.js
└── contacts.db           Created automatically — backup of every message
```

## 1. Install & run locally

```bash
cd portfolio_app
python -m venv venv
source venv/bin/activate      # Windows: venv\Scripts\activate
pip install -r requirements.txt
cp .env.example .env
```

Now edit `.env` (see step 2 below for how to get a Gmail app password), then:

```bash
python app.py
```

Open **http://127.0.0.1:5000** — the contact form will actually send email.

## 2. Get a Gmail "App Password" (so the form can send mail)

Gmail blocks plain-password SMTP logins, so you need an **App Password**:

1. Turn on 2-Step Verification on your Google account (Google Account →
   Security → 2-Step Verification).
2. Go to https://myaccount.google.com/apppasswords
3. Create a new app password (name it e.g. "Portfolio Site").
4. Google gives you a 16-character password — put that in `.env` as
   `SMTP_PASS` (not your normal Gmail password).
5. Set `SMTP_USER` to the Gmail address you generated it for, and `TO_EMAIL`
   to the inbox you want messages delivered to (can be the same address, or
   a different one).

Not using Gmail? Any SMTP provider works (Outlook, Zoho, a transactional
service like SendGrid/Mailgun/Resend) — just change `SMTP_HOST` / `SMTP_PORT`
accordingly in `.env`.

## 3. How the contact form works

- Visitor fills the form → JS sends a POST to `/api/contact`.
- Flask validates the fields, checks a hidden honeypot field (blocks basic
  bots), and rate-limits repeat submissions from the same IP (45s cooldown).
- It emails you via SMTP **and** saves a row in `contacts.db`, so you never
  lose a message even if email delivery has an issue.
- The visitor sees an inline pixel-style success/error message — no page
  reload.

To read saved messages any time:

```bash
python -c "import sqlite3; c=sqlite3.connect('contacts.db'); print(c.execute('SELECT * FROM contacts').fetchall())"
```

## 4. Editing content

Everything text-based — your bio, experience, projects, certifications,
achievements, education — lives in **`data.py`**. Change the values there and
refresh the page; the template updates automatically.

## 5. Adding your own images

Placeholder pixel-art images are already in place so the site looks right
even before you add real photos. Just **replace these files with your own,
keeping the exact same filename**:

```
static/images/profile.png                     ← your photo (hero section)
static/images/projects/hazel-cli.png           ← Hazel CLI screenshot
static/images/projects/phishing-detector.png   ← Phishing detector screenshot
static/images/certs/cbtp.png                   ← CBTP certificate
static/images/certs/cnsp.png                   ← CNSP certificate
static/images/certs/c3sa.png                   ← C3SA certificate
static/images/certs/cti101.png                 ← CTI 101 certificate
```

Any image format works as long as the filename matches (or update the path
in `data.py` if you rename a file). Square-ish photos work best for
`profile.png`; 16:9 screenshots work best for project images.

Want to add more projects or certificates? Just add another entry to the
`PROJECTS` / `CERTIFICATIONS` list in `data.py` with its own `image` path,
then drop the matching file in `static/images/`.

## 5. Deploying

This needs a host that can run Python, not just static files (so plain
GitHub Pages / static Vercel won't work as-is). Good free/cheap options:

- **Render.com** — connect your GitHub repo, set it as a "Web Service",
  add your `.env` values under Environment, done.
- **Railway.app** — similar flow, one-click deploy from GitHub.
- **PythonAnywhere** — good for small always-on Flask apps.
- **Vercel** — supports Python via serverless functions, but you'd need to
  restructure `app.py` slightly into Vercel's function format; the Render/
  Railway route is simpler for a Flask app like this one.

Whichever you choose, set `SMTP_HOST`, `SMTP_PORT`, `SMTP_USER`, `SMTP_PASS`,
and `TO_EMAIL` as environment variables in that platform's dashboard (don't
upload your real `.env` file — keep secrets out of git).

## 6. Before going live — fill these in

In `data.py`:
- `SITE["linkedin"]`, `SITE["github"]`, `SITE["resume_url"]`
- `PROJECTS[i]["link"]` — real GitHub URLs for Hazel CLI and the phishing
  detector

In `.env`:
- Real SMTP credentials (see step 2)
