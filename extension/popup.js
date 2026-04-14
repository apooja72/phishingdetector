document.getElementById("scan").addEventListener("click", () => {

    const file = document.getElementById("file").files[0];

    if (!file) {
        alert("Select a file first");
        return;
    }

    chrome.runtime.sendMessage({
        type: "CHECK_ATTACHMENT",
        filename: file.name
    }, (res) => {

        document.getElementById("result").innerHTML =
            `<h4 style="color:${res.label === 1 ? 'red' : 'green'}">
                ${res.label === 1 ? "Phishing File" : "Safe File"}
            </h4>
            <p>Probability: ${(res.probability * 100).toFixed(2)}%</p>`;
    });
});