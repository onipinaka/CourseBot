# from telegram import Update, InlineKeyboardMarkup, InlineKeyboardButton
# from telegram.ext import ApplicationBuilder, CommandHandler, CallbackQueryHandler, ContextTypes

# # 🧠 Replace this with your real bot token from @BotFather
# BOT_TOKEN = "8039872017:AAFYbOfc4OJDMVsF7eeAJuh-XXnNnJbKsw4"

# # 🎥 Replace these with actual Telegram video file_ids (you get them by forwarding the video to @getidsbot or using a bot script)
# LECTURES = {
#     "Lecture 1": "BAACAgUAAxkBAAMBaHFCAXZdAXGUQy1EOxGuDTugiwADIBYAAgp5iVcAAd_TAAFoD97wNgQ",  # example
#     "Lecture 2": "BAACAgUAAxkBAAIBoWYxQJD2d4xQ_LgW7kYjYZu...",
#     "Lecture 3": "BAACAgUAAxkBAAIBomYxQJD3d4xQ_LgW7kYjYZu..."
# }

# # 🚀 /start handler — show lecture menu
# async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
#     keyboard = [
#         [InlineKeyboardButton(title, callback_data=title)]
#         for title in LECTURES
#     ]
#     reply_markup = InlineKeyboardMarkup(keyboard)
#     await update.message.reply_text("📚 Select a lecture:", reply_markup=reply_markup)

# # 🎯 Handle button clicks
# async def handle_lecture_selection(update: Update, context: ContextTypes.DEFAULT_TYPE):
#     query = update.callback_query
#     await query.answer()
#     lecture_title = query.data
#     video_file_id = LECTURES.get(lecture_title)

#     if video_file_id:
#         await query.message.reply_video(
#             video=video_file_id,
#             caption=f"🎬 {lecture_title}"
#         )
#     else:
#         await query.message.reply_text("❌ Video not found.")

# # 🧠 Main function
# def main():
#     app = ApplicationBuilder().token(BOT_TOKEN).build()

#     app.add_handler(CommandHandler("start", start))
#     app.add_handler(CallbackQueryHandler(handle_lecture_selection))

#     print("🤖 Bot is running...")
#     app.run_polling()

# if __name__ == "__main__":
#     main()

import asyncio
from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import ApplicationBuilder, CommandHandler, CallbackQueryHandler, ContextTypes

BOT_TOKEN = "8039872017:AAFYbOfc4OJDMVsF7eeAJuh-XXnNnJbKsw4"

# Replace these with your real file_ids
LECTURES = {
    "Lecture 1": "BQACAgUAAyEFAASsro-rAAMEaHFH-FHHuEupcLnhGPvpzigCU2YAArAYAALAbclWHF7Jw_t_GAw2BA",
    "Lecture 2": "BQACAgUAAyEFAASsro-rAAMFaHFH-ORts6fb8y7QOgABYGMOFs48AAKxGAACwG3JVjvsGDZoDn7sNgQ",
    "Lecture 3": "BQACAgUAAyEFAASsro-rAAMGaHFH-LO9EDbnyj3bRhpyRlX7qiQAArIYAALAbclWR1DAzg6Exng2BA"
}

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    print("📩 /start received")
    keyboard = [[InlineKeyboardButton(title, callback_data=title)] for title in LECTURES]
    reply_markup = InlineKeyboardMarkup(keyboard)
    await update.message.reply_text("📚 Select a lecture:", reply_markup=reply_markup)

async def handle_lecture_selection(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = update.callback_query
    await query.answer()
    title = query.data
    file_id = LECTURES.get(title)

    if file_id:
        sent_message = await query.message.reply_video(video=file_id, caption=f"🎬 {title}")
        chat_id = sent_message.chat.id
        message_id = sent_message.message_id

        # Schedule deletion after 2 hours (7200 seconds)
        asyncio.create_task(delete_after_delay(context, chat_id, message_id, delay=10))
    else:
        await query.message.reply_text("❌ Video not found.")

async def delete_after_delay(context: ContextTypes.DEFAULT_TYPE, chat_id: int, message_id: int, delay: int):
    try:
        await asyncio.sleep(delay)
        await context.bot.delete_message(chat_id=chat_id, message_id=message_id)
        print(f"🗑️ Deleted message {message_id} in chat {chat_id}")
    except Exception as e:
        print(f"⚠️ Error deleting message: {e}")

def main():
    app = ApplicationBuilder().token(BOT_TOKEN).build()
    app.add_handler(CommandHandler("start", start))
    app.add_handler(CallbackQueryHandler(handle_lecture_selection))
    print("🤖 Bot is running...")
    app.run_polling()

if __name__ == "__main__":
    main()
