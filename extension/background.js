async function callAPI(endpoint, payload) {
    try {
        const res = await fetch(`http://localhost:5000${endpoint}`, {
            method: "POST",
            headers: { "Content-Type": "application/json" },
            body: JSON.stringify(payload)
        });

        return await res.json();
    } catch (err) {
        return { error: "Backend not reachable" };
    }
}

// URL check
chrome.runtime.onMessage.addListener((req, sender, sendResponse) => {

    if (req.type === "CHECK_URL") {
        callAPI("/predict/url", { url: req.url }).then(sendResponse);
        return true;
    }

    if (req.type === "CHECK_EMAIL") {
        callAPI("/predict/email", { text: req.text }).then(sendResponse);
        return true;
    }

    if (req.type === "CHECK_ATTACHMENT") {
        callAPI("/predict/attachment", { filename: req.filename }).then(sendResponse);
        return true;
    }
});