# XKCD Telegram Bot

Этот проект представляет собой Telegram-бота, который случайным образом выбирает комиксы с сайта [XKCD](https://xkcd.com/) и отправляет их в чат Telegram. Бот использует API сайта XKCD для получения информации о комиксах, а затем отправляет изображение и описание в указанный чат.

## Требования

Для запуска этого проекта вам потребуется:

- Python 3.12 или выше
- Установленные библиотеки: `requests`, `python-telegram-bot`, `python-dotenv`
- Аккаунт в Telegram и создание бота с использованием [BotFather](https://core.telegram.org/bots#botfather)
- Получение токена бота и идентификатора чата

## Установка

1. Клонируйте репозиторий:
   ```
   git clone https://github.com/amore52/comics.git
   cd comics

2. Создайте и активируйте виртуальное окружение:
    ```
    python -m venv .venv
    source .venv/bin/activate  # Для macOS/Linux
    .\.venv\Scripts\activate   # Для Windows
    ```
3. Установите зависимости:
    ```
   pip install -r requirements.txt
   ```
4. Создайте файл .env в корневой директории проекта и добавьте в него следующие переменные:
    ```
   TELEGRAM_TOKEN=your_telegram_bot_token
    CHAT_ID=your_telegram_chat_id
   ```
- Получите `TELEGRAM_TOKEN` через BotFather.
- Получите `CHAT_ID`, добавив вашего бота в нужный чат и написав в него сообщение. После этого можно использовать методы Telegram API, чтобы получить `chat_id`.

## Запуск
После того как вы настроили все зависимости и файл `.env`, вы можете запустить бота:
```
python main.py
```
Бот случайным образом выберет комикс с сайта xkcd и отправит его в указанный чат Telegram.
