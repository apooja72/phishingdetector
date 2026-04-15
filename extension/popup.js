document.getElementById("scanBtn").addEventListener("click", async () => {

  const fileInput = document.getElementById("fileInput");
  const resultDiv = document.getElementById("result");

  if (!fileInput.files.length) {
    resultDiv.textContent = "⚠️ Select file first";
    return;
  }

  const file = fileInput.files[0];

  try {
    const res = await fetch("http://localhost:5000/predict/attachment", {
      method: "POST",
      headers: {
        "Content-Type": "application/json"
      },
      body: JSON.stringify({ filename: file.name })
    });

    const data = await res.json();

    const pct = (data.probability * 100).toFixed(2);

    if (data.label === 1) {
      resultDiv.style.color = "red";
      resultDiv.textContent = `🚨 PHISHING (${pct}%)`;
    } else {
      resultDiv.style.color = "green";
      resultDiv.textContent = `✅ SAFE (${pct}%)`;
    }

  } catch (e) {
    resultDiv.textContent = "Backend not reachable";
  }
});