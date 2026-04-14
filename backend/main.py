from flask import Flask, request, jsonify
from flask_cors import CORS

from backend.prediction.url_predictor import URLPredictor
from backend.prediction.email_predictor import EmailPredictor
from backend.prediction.attachment_predictor import AttachmentPredictor
from backend.prediction.fusion import FusionEngine

app = Flask(__name__)
CORS(app)

# Load models ONCE at startup
url_predictor = URLPredictor()
email_predictor = EmailPredictor()
attachment_predictor = AttachmentPredictor()
fusion_engine = FusionEngine()


# ---------------------------
# URL PREDICTION ENDPOINT
# ---------------------------
@app.route("/predict/url", methods=["POST"])
def predict_url():
    data = request.json
    url = data.get("url", "")

    score = url_predictor.predict(url)

    return jsonify({
    "label": 1 if score > 0.5 else 0,
    "probability": float(score)
})


# ---------------------------
# EMAIL PREDICTION ENDPOINT
# ---------------------------
@app.route("/predict/email", methods=["POST"])
def predict_email():
    data = request.json
    email_text = data.get("text", "")

    score = email_predictor.predict(email_text)

    return jsonify({
    "label": 1 if score > 0.5 else 0,
    "probability": float(score)
})


# ---------------------------
# ATTACHMENT PREDICTION ENDPOINT
# ---------------------------
@app.route("/predict/attachment", methods=["POST"])
def predict_attachment():
    data = request.json
    filename = data.get("filename", "")

    score = attachment_predictor.predict(filename)

    return jsonify({
    "label": 1 if score > 0.5 else 0,
    "probability": float(score)
})


# ---------------------------
# FULL FUSION PREDICTION
# ---------------------------
@app.route("/predict/fusion", methods=["POST"])
def predict_fusion():
    data = request.json

    url = data.get("url")
    email = data.get("email")
    attachment = data.get("attachment")

    result = fusion_engine.compute(
        url=url,
        email=email,
        attachment=attachment
    )

    return jsonify(result)


# ---------------------------
# HEALTH CHECK
# ---------------------------
@app.route("/")
def home():
    return jsonify({
        "status": "running",
        "message": "Multi-Vector Phishing Detection API"
    })


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)