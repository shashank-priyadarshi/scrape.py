class Scraper:
    def __init__(self):
        pass

    async def scrape(self, url: str):
        print(f"url: {url}")
        return {}


def new() -> Scraper:
    """
    Factory function to create a Scraper instance with initialized Database and Notification.

    Returns:
        Scraper: An instance of Scraper with initialized dependencies.
    """
    return Scraper()
