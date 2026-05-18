import os
from threading import Thread
from flask import Flask
from telegram import Update
from telegram.ext import (
    Application,
    CommandHandler,
    ContextTypes,
)

TOKEN = os.getenv("BOT_TOKEN")

web = Flask(__name__)

@web.route("/")
def home():
    return "Bot Online ✅"

def run_web():
    web.run(host="0.0.0.0", port=10000)

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("✅ Telegram Bot Online!")

app = Application.builder().token(TOKEN).build()

app.add_handler(CommandHandler("start", start))

Thread(target=run_web).start()

print("Bot Started")

app.run_polling()
