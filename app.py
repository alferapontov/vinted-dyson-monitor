import os
import random
import time
from datetime import datetime

from bot.client import VintedClient
from bot.filter import is_interesting
from bot.notifier import send_message
from bot.parser import extract_items
from bot.storage import load_seen_ids, save_seen_ids

SEARCH_URL = (
    "https://www.vinted.pt/catalog"
    "?search_text=dyson"
    "&currency=EUR"
    "&order=newest_first"
    "&page=1"
)

CHECK_INTERVAL_MIN = 170
CHECK_INTERVAL_MAX = 210

# true (по умолчанию) — бесконечный мониторинг
# false — одна проверка (для GitHub Actions)
RUN_FOREVER = os.getenv("RUN_FOREVER", "true").lower() == "true"


def check_once(client: VintedClient):
    html = client.fetch(SEARCH_URL)

    items = extract_items(html)

    seen_ids = load_seen_ids()

    new_items = []

    for item in items:
        if not is_interesting(item):
            continue

        if item["id"] not in seen_ids:
            new_items.append(item)

        seen_ids.add(item["id"])

    save_seen_ids(seen_ids)

    return new_items


def main():
    client = VintedClient()

    while True:

        print("\n" + "=" * 70)
        print(datetime.now().strftime("[%H:%M:%S] Checking..."))

        try:
            new_items = check_once(client)

            print(f"New matching items: {len(new_items)}")

            for item in new_items:
                url = f"https://www.vinted.pt{item['url']}"

                message = (
                    "🔥 New Dyson found!\n\n"
                    f"{item['title']}\n\n"
                    f"💶 {item['price']}\n\n"
                    f"{url}"
                )

                print(message)

                send_message(message)

        except Exception as e:
            print("Error:", e)

        # Для GitHub Actions выполняем только одну проверку
        if not RUN_FOREVER:
            break

        wait_time = random.randint(
            CHECK_INTERVAL_MIN,
            CHECK_INTERVAL_MAX,
        )

        print(f"\nSleeping {wait_time} seconds...\n")

        time.sleep(wait_time)


if __name__ == "__main__":
    main()