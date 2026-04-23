const results = document.getElementById('results');

function renderGenerator(data) {
  results.innerHTML = `
    <div class="result-box">
      <h3>İçerik Fikirleri</h3>
      <ul>${data.ideas.map(item => `<li>${item}</li>`).join('')}</ul>
    </div>
    <div class="result-box">
      <h3>Caption Önerileri</h3>
      <ul>${data.captions.map(item => `<li>${item}</li>`).join('')}</ul>
    </div>
    <div class="result-box">
      <h3>Hashtagler</h3>
      <div class="chips">${data.hashtags.map(tag => `<span class="chip">${tag}</span>`).join('')}</div>
    </div>
    <div class="result-box">
      <h3>En İyi Paylaşım Saatleri</h3>
      <div class="chips">${data.best_times.map(time => `<span class="chip">${time}</span>`).join('')}</div>
    </div>
    <div class="result-box" style="grid-column: 1 / -1;">
      <h3>5 Günlük İçerik Planı</h3>
      <ul>${data.calendar.map(item => `<li><strong>${item.day}</strong> — ${item.format} — ${item.time}<br>${item.idea}</li>`).join('')}</ul>
    </div>
  `;
}

function renderAudit(data) {
  results.innerHTML = `
    <div class="result-box">
      <h3>@${data.username} Audit Skoru</h3>
      <div class="score">${data.score}/100</div>
      <p>Niş: ${data.niche}</p>
    </div>
    <div class="result-box">
      <h3>Güçlü Taraflar</h3>
      <ul>${data.strengths.map(item => `<li>${item}</li>`).join('')}</ul>
    </div>
    <div class="result-box">
      <h3>Geliştirme Alanları</h3>
      <ul>${data.improvements.map(item => `<li>${item}</li>`).join('')}</ul>
    </div>
    <div class="result-box">
      <h3>İçerik Sütunları</h3>
      <div class="chips">${data.content_pillars.map(item => `<span class="chip">${item}</span>`).join('')}</div>
    </div>
  `;
}

document.getElementById('generateBtn').addEventListener('click', async () => {
  const payload = {
    topic: document.getElementById('topic').value,
    platform: document.getElementById('platform').value,
    tone: document.getElementById('tone').value,
  };

  const response = await fetch('/api/generate', {
    method: 'POST',
    headers: { 'Content-Type': 'application/json' },
    body: JSON.stringify(payload)
  });

  const data = await response.json();
  renderGenerator(data);
});

document.getElementById('auditBtn').addEventListener('click', async () => {
  const payload = {
    username: document.getElementById('username').value,
    niche: document.getElementById('niche').value,
  };

  const response = await fetch('/api/audit', {
    method: 'POST',
    headers: { 'Content-Type': 'application/json' },
    body: JSON.stringify(payload)
  });

  const data = await response.json();
  renderAudit(data);
});
