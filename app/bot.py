from transformers import BertTokenizerFast, BertForSequenceClassification
import torch
from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, MessageHandler, filters, ContextTypes

# Load model and tokenizer
tokenizer = BertTokenizerFast.from_pretrained('./models/final_model')
model = BertForSequenceClassification.from_pretrained('./models/final_model')
model.eval()

# Inference function
def classify(text):
    inputs = tokenizer(text, return_tensors='pt', truncation=True, padding=True)
    with torch.no_grad():
        outputs = model(**inputs)
    logits = outputs.logits
    pred = torch.argmax(logits, dim=1).item()
    return "🚫 Toxic" if pred == 1 else "✅ Non-toxic"

# Bot reply function
async def handle_message(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user_text = update.message.text
    label = classify(user_text)
    await update.message.reply_text(label)

# Start bot
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("Hi! Send me a message and I’ll check if it’s toxic.")

# Main application
def main():
    app = ApplicationBuilder().token("7554626468:AAGZ0YGbH5AX2sTFnEBvLuLl1fwpXchq8vA").build()
    app.add_handler(CommandHandler("start", start))
    app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, handle_message))
    app.run_polling()

if __name__ == "__main__":
    main()
