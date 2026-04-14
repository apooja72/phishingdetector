function showEmailAlert(result) {
    const box = document.createElement("div");

    box.style.position = "fixed";
    box.style.top = "20px";
    box.style.right = "20px";
    box.style.zIndex = "999999";
    box.style.padding = "15px";
    box.style.background = result.label === 1 ? "#e74c3c" : "#27ae60";
    box.style.color = "white";
    box.style.borderRadius = "10px";
    box.style.fontSize = "14px";
    box.innerHTML = `
        <b>${result.label === 1 ? "Phishing Email" : "Safe Email"}</b><br>
        ${(result.probability * 100).toFixed(2)}%
    `;

    document.body.appendChild(box);

    setTimeout(() => box.remove(), 5000);
}

// Detect Gmail email body change
const observer = new MutationObserver(() => {

    const emailBody = document.querySelector(".a3s.aiL");

    if (emailBody && !emailBody.dataset.checked) {

        emailBody.dataset.checked = "true";

        chrome.runtime.sendMessage({
            type: "CHECK_EMAIL",
            text: emailBody.innerText
        }, (response) => {
            if (response) showEmailAlert(response);
        });
    }
});

observer.observe(document.body, {
    childList: true,
    subtree: true
});