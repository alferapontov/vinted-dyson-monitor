import os

import httpx
from dotenv import load_dotenv

load_dotenv()

BOT_TOKEN = os.getenv("TELEGRAM_BOT_TOKEN")
CHAT_ID = os.getenv("TELEGRAM_CHAT_ID")


def send_message(text: str):
    if not BOT_TOKEN or not CHAT_ID:
        raise RuntimeError("Не настроен TELEGRAM_BOT_TOKEN или TELEGRAM_CHAT_ID")

    url = f"https://api.telegram.org/bot{BOT_TOKEN}/sendMessage"

    response = httpx.post(
        url,
        json={
            "chat_id": CHAT_ID,
            "text": text,
            "disable_web_page_preview": False,
        },
        timeout=15,
    )

    response.raise_for_status()

if __name__ == "__main__":
    send_message("✅ Dyson Monitor подключён!")