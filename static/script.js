// theme toggle
const themeToggle = document.getElementById('themeToggle');
themeToggle.addEventListener('click', () => {
  const body = document.body;
  const isDay = body.getAttribute('data-theme') === 'day';
  body.setAttribute('data-theme', isDay ? 'night' : 'day');
  themeToggle.textContent = isDay ? '🌙' : '☀️';
  setTimeout(paintClouds, 50);
});

// mobile nav
const navToggle = document.getElementById('navToggle');
const navLinks = document.getElementById('navLinks');
navToggle.addEventListener('click', () => navLinks.classList.toggle('open'));
navLinks.querySelectorAll('a').forEach(a => a.addEventListener('click', () => navLinks.classList.remove('open')));

// generate pixel cloud shadow list (u = 8px grid)
function cloudShadow(color) {
  const u = 8;
  const cells = [];
  const rows = [
    { y: 0, cols: [3, 4, 5, 6] },
    { y: 1, cols: [1, 2, 3, 4, 5, 6, 7, 8] },
    { y: 2, cols: [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10] },
    { y: 3, cols: [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11] },
    { y: 4, cols: [1, 2, 3, 4, 5, 6, 7, 8, 9, 10] },
  ];
  rows.forEach(r => r.cols.forEach(c => cells.push(`${c * u}px ${r.y * u}px 0 0 ${color}`)));
  return cells.join(',');
}

const cloudLayer = document.getElementById('cloudLayer');
const cloudDefs = [
  { top: '8%', scale: 1.1, duration: 48 },
  { top: '18%', scale: 0.7, duration: 60 },
  { top: '4%', scale: 0.9, duration: 70 },
  { top: '26%', scale: 0.55, duration: 40 },
  { top: '14%', scale: 1.3, duration: 85 },
];
function paintClouds() {
  const c = getComputedStyle(document.body).getPropertyValue('--cloud').trim();
  cloudLayer.innerHTML = '';
  cloudDefs.forEach((d, i) => {
    const el = document.createElement('div');
    el.className = 'cloud';
    el.style.top = d.top;
    el.style.setProperty('--s', d.scale);
    el.style.boxShadow = cloudShadow(c || '#ffffff');
    el.style.animationDuration = d.duration + 's';
    el.style.animationDelay = (-i * 7) + 's';
    cloudLayer.appendChild(el);
  });
}
paintClouds();

// stars
const starsEl = document.getElementById('stars');
for (let i = 0; i < 70; i++) {
  const s = document.createElement('div');
  s.className = 'star';
  const size = Math.random() < 0.15 ? 4 : (Math.random() < 0.5 ? 3 : 2);
  s.style.width = size + 'px';
  s.style.height = size + 'px';
  s.style.left = Math.random() * 100 + '%';
  s.style.top = Math.random() * 72 + '%';
  s.style.animationDelay = (Math.random() * 2.4) + 's';
  s.style.animationDuration = (1.8 + Math.random() * 1.6) + 's';
  starsEl.appendChild(s);
}

// shooting stars
const shootLayer = document.getElementById('shootingLayer');
const shootDefs = [
  { top: '10%', left: '70%', delay: 0 },
  { top: '22%', left: '45%', delay: 3 },
  { top: '6%', left: '30%', delay: 7 },
];
shootDefs.forEach(d => {
  const el = document.createElement('div');
  el.className = 'shooting-star';
  el.style.top = d.top;
  el.style.left = d.left;
  el.style.animationDelay = d.delay + 's';
  shootLayer.appendChild(el);
});

// ---------------- contact form ----------------
const form = document.getElementById('contactForm');
const statusEl = document.getElementById('formStatus');
const submitBtn = document.getElementById('submitBtn');

if (form) {
  form.addEventListener('submit', async (e) => {
    e.preventDefault();

    const name = form.name.value.trim();
    const email = form.email.value.trim();
    const message = form.message.value.trim();
    const website = form.website.value; // honeypot

    statusEl.classList.remove('show', 'ok', 'err');

    if (!name || !email || !message) {
      statusEl.textContent = '⚠ Please fill in all fields.';
      statusEl.classList.add('show', 'err');
      return;
    }

    submitBtn.disabled = true;
    const originalText = submitBtn.textContent;
    submitBtn.textContent = 'SENDING...';

    try {
      const res = await fetch('/api/contact', {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({ name, email, message, website }),
      });
      const data = await res.json();

      statusEl.textContent = (data.success ? '✓ ' : '⚠ ') + data.message;
      statusEl.classList.add('show', data.success ? 'ok' : 'err');

      if (data.success) {
        form.reset();
      }
    } catch (err) {
      statusEl.textContent = '⚠ Something went wrong. Please try emailing directly.';
      statusEl.classList.add('show', 'err');
    } finally {
      submitBtn.disabled = false;
      submitBtn.textContent = originalText;
    }
  });
}
