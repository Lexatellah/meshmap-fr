(async function () {
  const map = L.map('map').setView([46.6, 2.4], 5);
  L.tileLayer('https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png', {
    maxZoom: 19,
    attribution: '&copy; OpenStreetMap'
  }).addTo(map);

  const listEl = document.getElementById('network-list');
  const statsEl = document.getElementById('stats');

  let networks = [];
  try {
    const r = await fetch('/api/networks');
    networks = await r.json();
  } catch (e) {
    statsEl.textContent = 'Erreur de chargement des données.';
    return;
  }

  const markers = L.featureGroup().addTo(map);
  networks.forEach(n => {
    const m = L.marker([n.lat, n.lon]).addTo(markers);
    m.bindPopup(
      `<strong>${escapeHtml(n.name)}</strong><br>` +
      `${escapeHtml(n.city)}<br>` +
      `<a href="/network/${n.id}">Détails</a>`
    );
  });

  if (networks.length) {
    map.fitBounds(markers.getBounds().pad(0.2));
  }

  const totalNodes = networks.reduce((s, n) => s + (n.nodes || 0), 0);
  statsEl.textContent = `${networks.length} réseau(x) référencé(s) · ${totalNodes} nœud(s) cumulé(s)`;

  listEl.innerHTML = networks.map(n =>
    `<li><a href="/network/${n.id}">${escapeHtml(n.name)}</a> — ${escapeHtml(n.city)} · ${n.nodes || 0} nœuds</li>`
  ).join('');

  function escapeHtml(s) {
    return String(s ?? '').replace(/[&<>"']/g, c => ({
      '&': '&amp;', '<': '&lt;', '>': '&gt;', '"': '&quot;', "'": '&#39;'
    }[c]));
  }
})();