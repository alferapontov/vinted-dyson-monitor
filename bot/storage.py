import json
from pathlib import Path

DATA_FILE = Path("data/seen_items.json")


def load_seen_ids() -> set[str]:
    if not DATA_FILE.exists():
        return set()

    with open(DATA_FILE, "r", encoding="utf-8") as file:
        data = json.load(file)

    return set(data)


def save_seen_ids(ids: set[str]) -> None:
    DATA_FILE.parent.mkdir(exist_ok=True)

    with open(DATA_FILE, "w", encoding="utf-8") as file:
        json.dump(sorted(ids), file, indent=4)