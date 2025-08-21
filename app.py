from flask import Flask, request, jsonify, render_template
from transformers import AutoTokenizer, AutoModelForSequenceClassification
import torch

# Path to your saved model
MODEL_PATH = "models/"

# Load model & tokenizer
tokenizer = AutoTokenizer.from_pretrained(MODEL_PATH)
model = AutoModelForSequenceClassification.from_pretrained(MODEL_PATH)

app = Flask(__name__)

# Home page for GUI
@app.route("/", methods=["GET"])
def home():
    return render_template("index.html")

# Prediction API
@app.route("/predict", methods=["POST"])
def predict():
    data = request.json
    text = data.get("text", "")
    if not text:
        return jsonify({"error": "No text provided"}), 400

    inputs = tokenizer(text, return_tensors="pt", truncation=True, padding=True)
    with torch.no_grad():
        outputs = model(**inputs)
        probs = torch.softmax(outputs.logits, dim=-1)
        pred_id = torch.argmax(probs, dim=1).item()
        label = model.config.id2label[pred_id]
        confidence = probs[0][pred_id].item()

    return jsonify({"intent": label, "confidence": confidence})

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
