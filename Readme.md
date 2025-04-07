# Kazakh Language Toxicity Classification 🧠💬

This project is part of a capstone work that focuses on detecting **toxic comments** in **Kazakh language** using machine learning and NLP techniques. The goal is to build a classifier that can distinguish between toxic and non-toxic content in social media platforms.

## 📌 Objectives

- Classify text comments as toxic or non-toxic.
- Translate and adapt English datasets to Kazakh using Google Translate API and Hugging Face models.
- Experiment with baseline models (TF-IDF + Logistic Regression).
- Prepare the data pipeline for future training with transformers.

## 🗃️ Datasets

- [Jigsaw Toxic Comment Classification Challenge](https://www.kaggle.com/competitions/jigsaw-toxic-comment-classification-challenge)
- [Hate Speech and Offensive Language Dataset](https://www.kaggle.com/datasets/mrmorj/hate-speech-and-offensive-language-dataset)
- Translations will be done using Google Translate API and Hugging Face MarianMT models.
- A native Kazakh dataset is discussed in [this IEEE paper](https://ieeexplore.ieee.org/document/10719327) (may be added later).

## 🧪 Model

Baseline model:
- **TF-IDF Vectorizer**
- **Logistic Regression**
- Accuracy: ~89%, F1-score: ~0.89

## 📁 Project Structure

```
├── data/
│   ├── raw/               # Original datasets
│   └── processed/         # Cleaned and balanced datasets
├── notebooks/             # Jupyter notebooks for EDA, modeling
├── scripts/               # Python scripts (optional automation)
├── models/                # Saved models (.pkl)
├── .gitignore
├── requirements.txt
└── README.md
```

## 🚀 Getting Started

```bash
git clone https://github.com/Ser1q/Kazakh_language_toxicity_classification.git
cd Kazakh_language_toxicity_classification
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
```

## 🧠 Future Plans

- Class-level toxic type classification (e.g., insult, threat)
- Translation quality evaluation
- Train transformer models (e.g., multilingual BERT)
- Web demo (Streamlit)

## 👨‍💻 Author

Serik Nuradil · [GitHub](https://github.com/Ser1q)

Capstone Project · 2025