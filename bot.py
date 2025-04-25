from flask import Flask
from threading import Thread
from telegram.ext import Updater, CommandHandler
import os

# Twój token z Rendera (przez zmienną środowiskową)
TOKEN = os.getenv("BOT_TOKEN")

# Flask app, żeby Render widział otwarty port
app = Flask('')

@app.route('/')
def home():
    return "Bot działa!"

def run_flask():
    app.run(host='0.0.0.0', port=8080)

# Funkcja startowa dla Telegram bota
def start(update, context):
    update.message.reply_text("Cześć! Jestem gotowy do działania.")

def run_telegram():
    updater = Updater(TOKEN, use_context=True)
    dp = updater.dispatcher
    dp.add_handler(CommandHandler("start", start))
    updater.start_polling()
    updater.idle()

# Odpal Flask i bota jednocześnie
if __name__ == '__main__':
    Thread(target=run_flask).start()
    run_telegram()
