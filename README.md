

```markdown
# Multi-Intent Chatbot using Transformer Models
````
A Dockerized Flask web application for real-time user intent classification.  
This project fine-tunes transformer-based models (like BERT) to accurately categorize text queries into predefined intents, achieving **94% accuracy** on a custom dataset.

![Multi-Intent Chatbot Interface](https://github.com/7amitesh/Multi-Intent-Chatbot-using-Transformer-Based-Models/raw/main/Screenshot_2025-08-21_055136.png)
*The web interface showing an intent prediction for the query "book me a flight to Delhi".*

---
````
## 🚀 Features

- **Intent Classification:** Predicts user intent from short text phrases.
- **Transformer Backend:** Uses a fine-tuned Hugging Face transformer model for NLP.
- **Web GUI:** Simple browser interface for testing.
- **RESTful API:** Integration-ready API endpoint.
- **Dockerized:** Easily deployable with Docker.

## 🧠 How It Works

1. **User Input:** Type a query (e.g., "book me a flight to Delhi") in the web interface.
2. **Processing:** Flask backend tokenizes the text and feeds it into the model.
3. **Prediction:** Model calculates probabilities for each intent.
4. **Output:** Displays the most likely intent and confidence score.
````
## 📁 Project Structure

````

```bash
Multi-Intent-Chatbot-using-Transformer-Based-Models/
├── app.py                 # Main Flask application
├── models/                # Model files (git-ignored)
│   ├── config.json
│   ├── pytorch_model.bin
│   └── tokenizer.json
├── templates/             # HTML templates
│   └── index.html
├── static/                # CSS
│   └── style.css
├── test.py                # Script to test API
├── requirements.txt       # Python dependencies
├── Dockerfile             # Docker image definition
└── README.md              # Project documentation
````

## ⚡ Quick Start

### Prerequisites
- Docker
- Git

### 1. Clone the Repository
```bash
git clone https://github.com/7amitesh/Multi-Intent-Chatbot-using-Transformer-Based-Models.git
cd Multi-Intent-Chatbot-using-Transformer-Based-Models
````

### 2. Add Model Files

> **Important:** Model files are too large for GitHub.
> Download them from your source (Hugging Face, Google Drive, etc.) and place them in `models/`.

### 3. Build and Run with Docker

```bash
# Build image
docker build -t intent-classifier .

# Run container
docker run -p 5000:5000 intent-classifier
```

### 4. Access the App

Open your browser at: **[http://localhost:5000](http://localhost:5000)**
Type a query and click "Send" to see the predicted intent.

## 🔌 API Usage

**Endpoint:** `POST /predict`

**Example using `curl`:**

```bash
curl -X POST http://localhost:5000/predict \
  -H "Content-Type: application/json" \
  -d '{"text": "I need help resetting my password"}'
```

**Example Response:**

```json
{
  "intent": "password_reset",
  "confidence": 0.97
}
```

## 📊 Performance & Tech Details

* **Model:** Fine-tuned BERT-base-uncased
* **Accuracy:** 94% on \~2,000 sample test set
* **Framework:** PyTorch, Transformers, Flask
* **Deployment:** Docker container

## 👨‍💻 Author

**Amitesh Sharma**

* GitHub: [@7amitesh](https://github.com/7amitesh)
* LinkedIn: [Amitesh Sharma](https://www.linkedin.com/in/amitesh-sharma-7a28b421b/)
* Portfolio: \[Your Portfolio Link]

---

*Demonstrates NLP, model fine-tuning, and MLOps for production deployment.*

````

---

### ✅ How to Add an Image in GitHub README

1. Put your screenshot inside the repo (e.g., `Screenshot_2025-08-21_055136.png` in root folder).  
2. Use the **raw file URL** in Markdown like this:

```markdown
![Alt text](https://github.com/YourUsername/YourRepoName/raw/main/Screenshot_2025-08-21_055136.png)
````

* Replace `YourUsername` and `YourRepoName` with your actual GitHub username and repo.
* `raw/main/` ensures the image is fetched directly from the main branch.

---
