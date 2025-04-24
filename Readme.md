# 🧠 Kazakh/English Toxic Comment Classifier

A machine learning project for classifying toxic comments using BERT, with a modern UI powered by Streamlit and moderation capabilities via Telegram bot.

## 📌 Overview
This project uses a fine-tuned BERT model to detect toxic comments in English. Users can:
- Interactively classify comments via a **Streamlit web app**
- Automatically monitor group chats using a **Telegram moderation bot**

Future versions will also support **Kazakh** language, currently in development.

---

## 🚀 Features

### ✅ Streamlit Web App
- Enter any English comment to detect toxicity
- Visualize predictions, confidence scores, and classification results

### ✅ Telegram Bot
- Monitors group chat messages
- Detects and reports toxic content automatically

> 💬 Support for Kazakh text and Telegram moderation in Kazakh is planned for a future release.

---

## 📂 Project Structure
```
Kazakh Toxic Comments/
├── app/
│   └── streamlit_app.py          # Streamlit UI app
├── bot.py                        # Telegram moderation bot (ignored in git)
├── models/
│   └── final_model/              # Trained BERT model (ignored in git)
├── notebooks/                    # Training logs and experiments
├── data/                         # Processed datasets
├── requirements.txt              # Required libraries
├── .gitignore                    # Excludes large files and secrets
└── README.md                     # You're here
```

---

## ⚙️ Setup Instructions

### 1. Clone the repo
```bash
git clone https://github.com/yourusername/kazakh-toxic-comment-classifier.git
cd kazakh-toxic-comment-classifier
```

### 2. Create environment
```bash
conda create -n toxic-env python=3.11
conda activate toxic-env
pip install -r requirements.txt
```

### 3. Run Streamlit app
```bash
cd app
streamlit run streamlit_app.py
```

### 4. Run Telegram bot (optional)
```bash
python bot.py
```

---

## 🔒 Security & .gitignore
The following files are excluded from Git:
- Model checkpoints (`*.safetensors`, `*.pt`)
- API secrets and credentials (`gcp_key.json`, `bot.py`)
- Checkpoint folders (`notebooks/results/`)

---

## 📊 Model Performance

| Class       | Precision | Recall | F1-score | Support |
|-------------|-----------|--------|----------|---------|
| Non-Toxic   | 0.94      | 0.93   | 0.94     | 4132    |
| Toxic       | 0.93      | 0.94   | 0.94     | 4022    |
| **Accuracy**|           |        | **0.94** | 8154    |
| Macro Avg   | 0.94      | 0.94   | 0.94     | 8154    |
| Weighted Avg| 0.94      | 0.94   | 0.94     | 8154    |

---

## 🌾 Roadmap
- [x] English toxic comment detection
- [x] Streamlit front-end interface
- [x] Telegram bot integration
- [ ] Kazakh language dataset integration
- [ ] Streamlit + Telegram multilingual support

---

## 🤝 Contribution
Pull requests and collaborations are welcome!
Feel free to fork and suggest new features — especially for Kazakh datasets 💬

---

## 📜 License
MIT License. See `LICENSE` file for more details.

