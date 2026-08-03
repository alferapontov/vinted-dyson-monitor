import httpx


class VintedClient:
    def fetch(self, url: str) -> str:
        with httpx.Client(
            headers={
                "User-Agent": (
                    "Mozilla/5.0 "
                    "(Windows NT 10.0; Win64; x64) "
                    "AppleWebKit/537.36 "
                    "(KHTML, like Gecko) "
                    "Chrome/138.0 Safari/537.36"
                )
            },
            timeout=15,
        ) as client:
            response = client.get(url)
            response.raise_for_status()
            return response.text