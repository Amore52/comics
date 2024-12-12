import random
import requests
import os

from telegram import Bot
from dotenv import load_dotenv


MIN_COMICS_NUM = 1
MAX_COMICS_NUM = 2500


def get_random_comic():
    random_comic_number = random.randint(MIN_COMICS_NUM, MAX_COMICS_NUM)
    url = f"https://xkcd.com/{random_comic_number}/info.0.json"
    response = requests.get(url)
    if response.ok:
        comics_json = response.json()
        image_url = comics_json['img']
        alt_text = comics_json['alt']
        return image_url, alt_text
    else:
        return f"Ошибка: {response.status_code}"


def send_comic_to_telegram(bot, chat_id):
    image_url, alt_text = get_random_comic()
    if image_url:
        image_response = requests.get(image_url)
        image_response.raise_for_status()
        bot.send_photo(chat_id=chat_id, photo=image_response.content, caption=alt_text)
        return "Комикс отправлен"


def main():
    load_dotenv()
    TELEGRAM_TOKEN = os.getenv('TELEGRAM_TOKEN')
    CHAT_ID = os.getenv('CHAT_ID')
    bot = Bot(token=TELEGRAM_TOKEN)
    send_comic_to_telegram(bot, CHAT_ID)


if __name__ == "__main__":
    main()
