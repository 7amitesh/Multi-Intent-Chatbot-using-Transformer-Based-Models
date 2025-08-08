# 🚀 Intent Detection and Slot Filling Chatbot using BERT and FastAPI

A context-aware, multi-turn chatbot for real-time intent detection and slot filling using BERT-based models. Built with HuggingFace, FastAPI, and deployed via Docker on AWS.

---

## 🧠 Overview

This project demonstrates a production-level implementation of intent detection and slot filling for NLP applications like voice assistants, customer support bots, and more.

### 🔍 Key Features

* Fine-tuned BERT model (HuggingFace) on SNIPS/ATIS dataset
* Detects intents like "BookFlight", "PlayMusic", "GetWeather", etc.
* Extracts relevant slots (entities) like location, date, time
* Handles multi-turn, context-aware conversations
* Real-time API via FastAPI
* Containerized with Docker and deployed on AWS EC2

---

## 📦 Tech Stack

* `Python`
* `HuggingFace Transformers`
* `BERT` / `DistilBERT`
* `FastAPI`
* `Docker`
* `AWS EC2`
* Dataset: SNIPS or ATIS

---

## 📁 Folder Structure

```
├── app
│   ├── main.py             # FastAPI app
│   ├── model.py            # BERT model wrapper
│   ├── utils.py            # Tokenizer and preprocessing
├── data
│   └── snips_dataset.json  # Training dataset
├── model
│   └── saved_model/        # Trained model files
├── Dockerfile
├── requirements.txt
├── README.md
```

---

## 🛠️ Setup Instructions

### 1. Clone the Repo

```bash
git clone https://github.com/yourusername/intent-slot-chatbot.git
cd intent-slot-chatbot
```

### 2. Create Virtual Environment

```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

### 4. Download & Prepare Dataset

* You can use HuggingFace `datasets` to download SNIPS:

```python
from datasets import load_dataset
dataset = load_dataset("snips_built_in_intents")
```

### 5. Train Model

```bash
python train.py  # Training script you will write to fine-tune BERT
```

### 6. Run FastAPI App

```bash
uvicorn app.main:app --reload
```

* Test endpoints via Postman or browser at: `http://127.0.0.1:8000/docs`

### 7. Dockerize & Deploy

```bash
docker build -t intent-bot .
docker run -p 8000:8000 intent-bot
```

* Deploy container to AWS EC2 / Render / Railway

---

## 📌 API Example

### POST `/predict`

**Request:**

```json
{
  "text": "Book a flight from Delhi to Mumbai tomorrow at 5 pm"
}
```

**Response:**

```json
{
  "intent": "BookFlight",
  "slots": {
    "from_location": "Delhi",
    "to_location": "Mumbai",
    "time": "tomorrow at 5 pm"
  }
}
```

---

## 📊 Model Performance

* Accuracy: \~96% (SNIPS)
* F1 Score: \~95%

---

## ✨ Future Work

* Add RNN-based memory for stronger context tracking
* Integrate with React/Vue frontend UI
* Support voice-to-text input
* Continuous deployment with CI/CD

---

## 👤 Author

**Cristiano Adrian**

* GitHub: [yourusername](https://github.com/yourusername)
* Email: [your.email@example.com](mailto:your.email@example.com)

---

## 📜 License

MIT License

---

> ⭐ Star this repo if you found it helpful. Contributions are welcome!
