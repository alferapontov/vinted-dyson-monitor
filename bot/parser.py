from bs4 import BeautifulSoup


def extract_items(html: str):
    soup = BeautifulSoup(html, "html.parser")

    items = []

    cards = soup.select("div.new-item-box__container")

    for card in cards:

        item_id = card.get("data-testid", "").replace("product-item-id-", "")

        brand = card.select_one("[data-testid$='--description-title']")
        subtitle = card.select_one("[data-testid$='--description-subtitle']")
        price = card.select_one("[data-testid$='--price-text']")
        link = card.select_one("a[data-testid$='--overlay-link']")
        image = card.select_one("img")

        title = ""
        url = ""

        if link:
            title = link.get("title", "").strip()
            url = link.get("href", "")

        items.append(
            {
                "id": item_id,
                "title": title,
                "brand": brand.text.strip() if brand else "",
                "subtitle": subtitle.text.strip() if subtitle else "",
                "price": price.text.strip() if price else "",
                "url": url,
                "image": image.get("src") if image else "",
            }
        )

    return items