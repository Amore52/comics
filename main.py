import random
import asyncio
import requests
import os

from telegram import Bot
from dotenv import load_dotenv


load_dotenv()
TELEGRAM_TOKEN = os.getenv('TELEGRAM_TOKEN')
CHAT_ID = os.getenv('CHAT_ID')
bot = Bot(token=TELEGRAM_TOKEN)


def get_random_comic():
    random_comic_number = random.randint(1, 2500)
    url = f"https://xkcd.com/{random_comic_number}/info.0.json"
    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
        image_url = data['img']
        alt_text = data['alt']
        return image_url, alt_text
    else:
        print(f"Ошибка: {response.status_code}")
        return None


async def send_comic_to_telegram():
    image_url, alt_text = get_random_comic()
    if image_url:
        image_response = requests.get(image_url)
        image_response.raise_for_status()
        await bot.send_photo(chat_id=CHAT_ID, photo=image_response.content, caption=alt_text)
        print("Комикс отправлен")


if __name__ == "__main__":
    asyncio.run(send_comic_to_telegram())
