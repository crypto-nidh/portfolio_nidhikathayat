import os
import re
import sqlite3
import smtplib
import time
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from datetime import datetime, timezone

from flask import Flask, render_template, request, jsonify
from dotenv import load_dotenv

import data

load_dotenv()

app = Flask(__name__)

# ---------------- config (from .env) ----------------
SMTP_HOST = os.getenv("SMTP_HOST", "smtp.gmail.com")
SMTP_PORT = int(os.getenv("SMTP_PORT", "465"))
SMTP_USER = os.getenv("SMTP_USER", "")
SMTP_PASS = os.getenv("SMTP_PASS", "")
TO_EMAIL = os.getenv("TO_EMAIL", data.SITE["email"])

DB_PATH = os.path.join(os.path.dirname(__file__), "contacts.db")
EMAIL_RE = re.compile(r"^[^@\s]+@[^@\s]+\.[^@\s]+$")

# very simple in-memory rate limit: {ip: last_submit_timestamp}
_last_submit = {}
RATE_LIMIT_SECONDS = 45


def init_db():
    conn = sqlite3.connect(DB_PATH)
    conn.execute(
        """
        CREATE TABLE IF NOT EXISTS contacts (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            email TEXT NOT NULL,
            message TEXT NOT NULL,
            created_at TEXT NOT NULL,
            emailed INTEGER NOT NULL DEFAULT 0
        )
        """
    )
    conn.commit()
    conn.close()


def save_to_db(name, email, message, emailed: bool):
    conn = sqlite3.connect(DB_PATH)
    conn.execute(
        "INSERT INTO contacts (name, email, message, created_at, emailed) VALUES (?, ?, ?, ?, ?)",
        (name, email, message, datetime.now(timezone.utc).isoformat(), int(emailed)),
    )
    conn.commit()
    conn.close()


def send_email(name, email, message):
    if not SMTP_USER or not SMTP_PASS:
        raise RuntimeError("SMTP_USER / SMTP_PASS not configured in .env")

    msg = MIMEMultipart()
    msg["From"] = SMTP_USER
    msg["To"] = TO_EMAIL
    msg["Reply-To"] = email
    msg["Subject"] = f"Portfolio contact form — {name}"

    body = (
        f"New message from your portfolio contact form:\n\n"
        f"Name: {name}\n"
        f"Email: {email}\n\n"
        f"Message:\n{message}\n"
    )
    msg.attach(MIMEText(body, "plain"))

    with smtplib.SMTP_SSL(SMTP_HOST, SMTP_PORT) as server:
        server.login(SMTP_USER, SMTP_PASS)
        server.sendmail(SMTP_USER, TO_EMAIL, msg.as_string())


@app.route("/")
def home():
    return render_template(
        "index.html",
        site=data.SITE,
        stats=data.STATS,
        about=data.ABOUT,
        experience=data.EXPERIENCE,
        projects=data.PROJECTS,
        certifications=data.CERTIFICATIONS,
        achievements=data.ACHIEVEMENTS,
        education=data.EDUCATION,
    )


@app.route("/about")
def about():
    return render_template("about.html", site=data.SITE, about=data.ABOUT)


@app.route("/experience")
def experience():
    return render_template("experience.html", site=data.SITE, experience=data.EXPERIENCE)


@app.route("/projects")
def projects():
    return render_template("projects.html", site=data.SITE, projects=data.PROJECTS)


@app.route("/certifications")
def certifications():
    return render_template(
        "certifications.html",
        site=data.SITE,
        certifications=data.CERTIFICATIONS,
        achievements=data.ACHIEVEMENTS,
    )


@app.route("/contact")
def contact_page():
    return render_template("contact.html", site=data.SITE)


@app.route("/api/contact", methods=["POST"])
def contact():
    payload = request.get_json(silent=True) or {}

    name = (payload.get("name") or "").strip()
    email = (payload.get("email") or "").strip()
    message = (payload.get("message") or "").strip()
    honeypot = (payload.get("website") or "").strip()  # hidden field, humans leave it empty

    # honeypot triggered -> silently pretend success, do nothing
    if honeypot:
        return jsonify({"success": True, "message": "Thanks for reaching out!"})

    if not name or not email or not message:
        return jsonify({"success": False, "message": "Please fill in name, email and message."}), 400

    if not EMAIL_RE.match(email):
        return jsonify({"success": False, "message": "That email address doesn't look right."}), 400

    if len(message) > 5000:
        return jsonify({"success": False, "message": "Message is too long."}), 400

    ip = request.headers.get("X-Forwarded-For", request.remote_addr) or "unknown"
    now = time.time()
    if ip in _last_submit and now - _last_submit[ip] < RATE_LIMIT_SECONDS:
        return jsonify({"success": False, "message": "You're sending messages too fast — try again shortly."}), 429
    _last_submit[ip] = now

    emailed = False
    email_error = None
    try:
        send_email(name, email, message)
        emailed = True
    except Exception as e:  # noqa: BLE001
        email_error = str(e)

    # always keep a local backup, even if email sending failed
    save_to_db(name, email, message, emailed)

    if emailed:
        return jsonify({"success": True, "message": "Message sent! I'll get back to you soon."})

    # message is safely stored even though email failed
    app.logger.error("Email send failed: %s", email_error)
    return jsonify({
        "success": True,
        "message": "Message received and saved. (Email delivery is still being set up.)",
    })


init_db()

if __name__ == "__main__":
    app.run(debug=False, port=5000)
