from flask import Flask
import threading
import time
import requests
from bs4 import BeautifulSoup
from telegram import Bot

app = Flask(__name__)

TELEGRAM_TOKEN = 'TU_WSTAW_TOKEN'
CHAT_ID = 'TU_WSTAW_CHAT_ID'

bot = Bot(token=TELEGRAM_TOKEN)

def track_olx():
    while True:
        try:
            url = "https://www.olx.pl/motoryzacja/maszyny-rolnicze/koparki/"
            response = requests.get(url)
            soup = BeautifulSoup(response.text, 'html.parser')
            first_offer = soup.find('div', {'data-cy': 'l-card'})
            if first_offer:
                title = first_offer.find('h6')
                if title:
                    bot.send_message(chat_id=CHAT_ID, text=f"Nowa oferta: {title.text.strip()}")
        except Exception as e:
            print(f"Błąd: {e}")
        time.sleep(600)

@app.route('/')
def home():
    return "Bot działa!"

if __name__ == '__main__':
    threading.Thread(target=track_olx).start()
    app.run(host='0.0.0.0', port=10000)
