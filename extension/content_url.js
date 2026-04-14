function showPopup(result) {
    const box = document.createElement("div");

    box.style.position = "fixed";
    box.style.top = "50%";
    box.style.left = "50%";
    box.style.transform = "translate(-50%, -50%)";
    box.style.zIndex = "999999";
    box.style.padding = "20px";
    box.style.background = result.label === 1 ? "#ff4d4d" : "#2ecc71";
    box.style.color = "white";
    box.style.fontSize = "18px";
    box.style.borderRadius = "12px";
    box.style.boxShadow = "0 0 20px rgba(0,0,0,0.3)";
    box.innerHTML = `
        <b>${result.label === 1 ? "⚠ Phishing Site" : "✔ Safe Site"}</b><br>
        Probability: ${(result.probability * 100).toFixed(2)}%
    `;

    document.body.appendChild(box);

    setTimeout(() => box.remove(), 5000);
}

chrome.runtime.sendMessage(
    {
        type: "CHECK_URL",
        url: window.location.href
    },
    (response) => {
        if (response) showPopup(response);
    }
);