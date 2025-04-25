import streamlit as st
from transformers import BertTokenizerFast, BertForSequenceClassification
import torch
# from pathlib import Path

@st.cache(allow_output_mutation=True)
def load_model():
    repo_id = "nar9k/toxicity-bert-en"
    tokenizer = BertTokenizerFast.from_pretrained(repo_id)
    model = BertForSequenceClassification.from_pretrained(repo_id)
    return tokenizer, model

tokenizer, model = load_model()

# st.markdown(f"Model loaded from `{Path('./models/final_model').resolve().as_posix()}`")

def classify_text(text):
    inputs = tokenizer(text, return_tensors="pt", truncation=True, padding=True)
    with torch.no_grad():
        outputs = model(**inputs)
    logits = outputs.logits
    probs = torch.softmax(logits, dim=1)
    return probs[0].tolist()

# Streamlit UI
st.title("🧠 Toxic Comment Classifier")
text = st.text_area("Enter a comment to classify:", height=100)
label = "Placeholder"
if st.button("Classify"):
    if text.strip() == "":
        st.warning("Please enter a comment.")
    else:
        prob = classify_text(text)
        st.markdown(f"**Non-Toxic Probability:** `{prob[0]:.4f}`")
        st.markdown(f"**Toxic Probability:** `{prob[1]:.4f}`")
        label = "🧼 Non-Toxic" if prob[0] > prob[1] else "☣️ Toxic"
        st.success(f"Predicted Label: **{label}**")
