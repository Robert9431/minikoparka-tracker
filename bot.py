import requests
import time
from bs4 import BeautifulSoup
import telegram

TELEGRAM_TOKEN = 'TU_WKLEJ_SWÓJ_TOKEN'
TELEGRAM_CHAT_ID = '7898261739'

OLX_URL = "https://www.olx.pl/motoryzacja/maszyny-rolnicze/minikoparki/"
CENA_MIN = 15000
CENA_MAX = 80000

bot = telegram.Bot(token=TELEGRAM_TOKEN)
widziane_ogloszenia = set()

def sprawdz_olx():
    headers = {"User-Agent": "Mozilla/5.0"}
    response = requests.get(OLX_URL, headers=headers)
    soup = BeautifulSoup(response.text, 'html.parser')

    for offer in soup.find_all('div', class_='css-1sw7q4x'):
        link_tag = offer.find('a')
        if link_tag:
            link = "https://www.olx.pl" + link_tag.get('href')
            title = offer.find('h6').text.strip() if offer.find('h6') else 'Brak tytułu'
            price_text = offer.find('p').text if offer.find('p') else '0'
            price_text = price_text.replace('zł', '').replace(' ', '').replace(',', '.')
            try:
                price = float(price_text)
            except ValueError:
                price = 0

            if link not in widziane_ogloszenia and CENA_MIN <= price <= CENA_MAX:
                widziane_ogloszenia.add(link)
                bot.send_message(chat_id=TELEGRAM_CHAT_ID,
                                 text=f"Nowa koparka!\n{title}\nCena: {price} zł\n{link}")

while True:
    sprawdz_olx()
    time.sleep(300)
