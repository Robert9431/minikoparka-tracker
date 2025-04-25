from flask import Flask, request
from telegram import Bot, Update
from telegram.ext import Dispatcher, CommandHandler
import os

TOKEN = os.getenv("BOT_TOKEN")
bot = Bot(token=TOKEN)

app = Flask(__name__)
dispatcher = Dispatcher(bot, None, workers=0)

# Komenda start
def start(update, context):
    update.message.reply_text("Bot działa!")

dispatcher.add_handler(CommandHandler("start", start))

@app.route(f"/{TOKEN}", methods=["POST"])
def webhook():
    update = Update.de_json(request.get_json(force=True), bot)
    dispatcher.process_update(update)
    return "ok"

@app.route('/')
def index():
    return "Bot jest aktywny"

if __name__ == '__main__':
    bot.set_webhook(url=f"https://<TWOJA-NAZWA>.onrender.com/{TOKEN}")
    app.run(host="0.0.0.0", port=10000)
