from telegram.ext import Application, MessageHandler, filters, ContextTypes
from telegram import Update

BOT_TOKEN = "8039872017:AAFYbOfc4OJDMVsF7eeAJuh-XXnNnJbKsw4"

async def log_file_id(update: Update, context: ContextTypes.DEFAULT_TYPE):
    msg = update.message
    if msg.document:
        print(f"📄 Document: {msg.document.file_name}")
        print(f"File ID: {msg.document.file_id}")
    elif msg.video:
        print(f"🎥 Video: {msg.video.file_name}")
        print(f"File ID: {msg.video.file_id}")
    else:
        print("Unsupported file type")

app = Application.builder().token(BOT_TOKEN).build()
app.add_handler(MessageHandler(filters.ALL, log_file_id))

app.run_polling()
