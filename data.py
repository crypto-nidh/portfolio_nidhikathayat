# All portfolio content lives here. Edit this file to update the site —
# nothing in templates/index.html needs to change.

SITE = {
    "name": "Nidhi Kathayat",
    "role": "Web Application Security & VAPT",
    "email": "nidhikathayat03@gmail.com",
    "linkedin": "#",   # TODO: add your LinkedIn URL
    "github": "#",     # TODO: add your GitHub URL
    "resume_url": "#", # TODO: link to a hosted resume PDF
    "photo": "images/profile.png",  # put your photo at static/images/profile.png
}

STATS = [
    {"icon": "🏆", "value": "6", "label": "CTF Results"},
    {"icon": "📜", "value": "4", "label": "Certifications"},
    {"icon": "🐛", "value": "7+", "label": "Vuln Classes"},
]

ABOUT = {
    "paragraphs": [
        "I'm <b>Nidhi Kathayat</b>, a Computer Science undergrad at Poornima University and a cybersecurity practitioner focused on Web Application Security and VAPT.",
        "My experience comes from CTFs and applied labs — hunting <b>SQL Injection, XSS, IDOR and CSRF</b> through recon and manual testing in Burp Suite, then documenting every finding as a clear, structured PoC report.",
        "I approach every target with an attacker's mindset: understand how a system is meant to work, then find where that assumption breaks.",
    ],
    "tools": ["BURP SUITE", "NMAP", "METASPLOIT", "PYTHON", "BLOODHOUND", "ZAP"],
    "skill_columns": [
        {"title": "WEB SECURITY", "skills": ["OWASP TOP 10", "AUTH BYPASS", "RACE COND.", "PRIV. ESC."]},
        {"title": "VAPT", "skills": ["ENUMERATION", "EXPLOITATION", "PoC REPORTS", "ACTIVE DIR."]},
        {"title": "SCRIPTING & PLATFORMS", "skills": ["PYTHON", "BASH", "SQL", "KALI", "DOCKER", "GIT"]},
    ],
    "cards": [
        {"idx": "01", "title": "RECON", "text": "Mapping the attack surface before a single payload is sent."},
        {"idx": "02", "title": "EXPLOIT", "text": "Turning logic flaws into working, repeatable proof."},
        {"idx": "03", "title": "REPORT", "text": "Structured PoCs a developer can act on same-day."},
        {"idx": "04", "title": "HARDEN", "text": "Mitigations that hold up under retest."},
    ],
}

EXPERIENCE = [
    {
        "date": "SEP 2025 — DEC 2025",
        "title": "CTF Developer Intern (Web Security)",
        "company": "RAZZIFY",
        "bullets": [
            "Designed vulnerable web challenges modeled on real-world attack techniques, including SQL Injection, XSS, and IDOR.",
            "Performed manual testing and exploitation across challenge environments to validate difficulty and realism.",
            "Documented attack methodology and mitigation strategies in structured writeups for participants.",
            "Simulated real-world web vulnerabilities for hands-on exploitation, applying an attacker's mindset to how systems break.",
        ],
    }
]

PROJECTS = [
    {
        "title": "Hazel CLI",
        "sev_label": "AI × PENTEST",
        "sev_class": "sev-high",
        "image": "images/projects/hazel-cli.png",
        "paragraphs": [
            "AI-powered terminal assistant for pentesters — intercepts commands, flags dangerous patterns, and auto-suggests the next tool from scan output (Nmap → Gobuster).",
            "Multi-provider AI fallback (Groq, Gemini, OpenRouter, Ollama) with typo correction and a rule-based danger detection engine, plus auto-generated pentest writeups from session history.",
        ],
        "tags": ["PYTHON", "CLI", "AUTOMATION"],
        "link": "#",
    },
    {
        "title": "Phishing Email Detection",
        "sev_label": "ML × SOC",
        "sev_class": "sev-med",
        "image": "images/projects/phishing-detector.png",
        "paragraphs": [
            "ML-based phishing detection system built with Scikit-learn, analyzing URL patterns, sender metadata, and email content.",
            "Stress-tested accuracy against common bypass techniques, applying feature extraction and behavioral analysis aligned to SOC-level phishing investigation workflows.",
        ],
        "tags": ["PYTHON", "SCIKIT-LEARN", "ML"],
        "link": "#",
    },
]

CERTIFICATIONS = [
    {"status": "done", "name": "CBTP", "issuer": "Certified Blue Team Practitioner — SecOps Group", "image": "images/certs/cbtp.png"},
    {"status": "done", "name": "CNSP", "issuer": "SecOps Group", "image": "images/certs/cnsp.png"},
    {"status": "done", "name": "C3SA", "issuer": "CyberWarFare Labs", "image": "images/certs/c3sa.png"},
    {"status": "done", "name": "CTI 101", "issuer": "ARCX", "image": "images/certs/cti101.png"},
    {"status": "progress", "name": "CEH", "issuer": "Certified Ethical Hacker", "image": None},
    {"status": "progress", "name": "CPENT", "issuer": "Certified Penetration Testing Professional", "image": None},
]

ACHIEVEMENTS = [
    {"rank": "#5", "title": "OWASP HACKER'S GAMBIT 2025", "detail": "National ranking, Team GenZCTF"},
    {"rank": "#2", "title": "VECTORCTF", "detail": "TryHackMe"},
    {"rank": "#27", "title": "CYBERNEONGEN CTF", "detail": "Solo entry"},
    {"rank": "#26", "title": "TRYHACKME INDUSTRIAL CTF", "detail": "Solo entry"},
    {"rank": "TOP 30", "title": "ACEHACK 5.0", "detail": "Hackathon"},
    {"rank": "#15", "title": "SHAKTI CTF", "detail": "Among women participants, #54 overall"},
]

EDUCATION = {
    "degree": "B.Tech, Computer Science & Engineering",
    "school": "POORNIMA UNIVERSITY, JAIPUR",
    "years": "2024 — 2028",
}
