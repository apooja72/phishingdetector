let lastEmailId = null;

const observer = new MutationObserver(() => {
    const subjectEl = document.querySelector("h2.hP");  
    const bodyEl = document.querySelector("div.a3s.aiL, div.a3s");

    if (subjectEl && bodyEl) {
        const emailText = subjectEl.innerText + "\n" + bodyEl.innerText;

        const emailId = subjectEl.innerText + bodyEl.innerText.substring(0, 30);

        if (emailId !== lastEmailId) {
            lastEmailId = emailId;

            const oldPopup = document.getElementById("phishshield-popup");
            if (oldPopup) oldPopup.remove();

            analyzeEmail(emailText);
        }
    }
});

observer.observe(document.body, { childList: true, subtree: true });

function analyzeEmail(text) {
    fetch("http://localhost:5000/predict/email", {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({ text: text })
    })
    .then(res => res.json())
    .then(data => {
        showPopup(data.label, data.probability);
    });
}

function showPopup(label, prob) {
    const popup = document.createElement("div");
    popup.id = "phishshield-popup";

    popup.className = label === 1 ? "phishing" : "safe";

    popup.innerHTML = `
        <h3>${label === 1 ? "⚠️ Phishing Detected!" : "✔️ Safe Email"}</h3>
        <p><strong>Probability:</strong> ${(prob*100).toFixed(2)}%</p>
        <button id="phishshield-btn">OK</button>
    `;

    document.body.appendChild(popup);

    popup.querySelector("#phishshield-btn").onclick = () => popup.remove();
}