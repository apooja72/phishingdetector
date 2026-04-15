const BACKEND_PREDICT_URL = 'http://localhost:5000/predict/url';

function createOverlay() {
  const overlay = document.createElement('div');
  overlay.className = 'clickguard-overlay';
  overlay.innerHTML = `
    <div class="clickguard-card">
      <div class="clickguard-title">Checking URL...</div>
      <div class="clickguard-score" id="cg-score">Analyzing...</div>
      <div class="clickguard-url" id="cg-url"></div>
      <div class="clickguard-buttons">
        <button class="clickguard-btn clickguard-cancel" id="cg-cancel">Cancel</button>
        <button class="clickguard-btn clickguard-proceed" id="cg-proceed">Proceed</button>
      </div>
    </div>`;
  return overlay;
}

function showOverlay(url, predictionData, onProceed, onCancel) {
  const existing = document.querySelector('.clickguard-overlay');
  if (existing) existing.remove();

  const overlay = createOverlay();
  document.body.appendChild(overlay);
  overlay.querySelector('#cg-url').textContent = url;

  const scoreEl = overlay.querySelector('#cg-score');

  if (predictionData) {
    const pct = (predictionData.probability * 100).toFixed(1);

    if (predictionData.label === 1) {
      scoreEl.textContent = `Phishing — ${pct}%`;
      scoreEl.classList.add("cg-unsafe");
    } else {
      scoreEl.textContent = `Safe — ${pct}%`;
      scoreEl.classList.add("cg-safe");
    }
  }

  overlay.querySelector('#cg-cancel').onclick = () => {
    overlay.remove();
    if (onCancel) onCancel();
  };

  overlay.querySelector('#cg-proceed').onclick = () => {
    overlay.remove();
    if (onProceed) onProceed();
  };
}

async function fetchPrediction(url) {
  try {
    const res = await fetch(BACKEND_PREDICT_URL, {
      method: 'POST',
      headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify({ url })
    });

    return await res.json();
  } catch (e) {
    console.error(e);
    return null;
  }
}

document.addEventListener('click', async function (e) {

  let el = e.target;
  while (el && el.tagName !== 'A') el = el.parentElement;
  if (!el || !el.href) return;

  e.preventDefault();

  const href = el.href;

  showOverlay(href, null, () => {
    window.location.href = href;
  });

  const prediction = await fetchPrediction(href);

  showOverlay(href, prediction, () => {
    window.location.href = href;
  });
});