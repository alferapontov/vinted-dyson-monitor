import re

MAX_PRICE = 250

ALLOWED_MODELS = {
    "v11",
    "v12",
    "v15",
}

EXCLUDED_WORDS = {
    "battery",
    "bateria",
    "filter",
    "filtro",
    "charger",
    "carregador",
    "dock",
    "support",
    "wall mount",
    "tube",
    "pipe",
    "head",
    "motorhead",
    "accessory",
    "accessories",
    "piece",
    "parts",
    "replacement",
}


def parse_price(price: str) -> float:
    price = price.replace("€", "")
    price = price.replace(",", ".")
    price = re.sub(r"[^0-9.]", "", price)
    return float(price)


def is_interesting(item: dict) -> bool:
    text = (
        f"{item['title']} "
        f"{item['brand']} "
        f"{item['subtitle']}"
    ).lower()

    # Только Dyson
    if "dyson" not in text:
        return False

    # Только V11 / V12 / V15
    if not any(model in text for model in ALLOWED_MODELS):
        return False

    # Исключаем аксессуары
    if any(word in text for word in EXCLUDED_WORDS):
        return False

    # Цена
    try:
        if parse_price(item["price"]) > MAX_PRICE:
            return False
    except Exception:
        return False

    return True