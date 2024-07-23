import httpx

from ..abstract import Database, Notification
from ..logger.logger import LoggerSingleton


class Scraper:
    def __init__(self, logger: LoggerSingleton, db: Database, notifier: Notification):
        self.logger = logger
        self.db = db
        self.notifier = notifier

    async def scrape(self, url: str):
        self.logger.info(f"Starting to scrape URL: {url}")

        async with httpx.AsyncClient() as client:
            try:
                response = await client.get(url)
                response.raise_for_status()
                self.logger.info(f"Successfully scraped URL: {url}")
                self.db.create(response)
                self.notifier.notify("scraped url {}".format(url), "scraper", "console")
                return {"url": url, "content": response.text}
            except httpx.HTTPStatusError as http_err:
                self.logger.error(f"HTTP error occurred: {http_err}")
                return {"url": url, "error": str(http_err)}
            except Exception as err:
                self.logger.error(f"Unknown error occurred: {err}")
                return {"url": url, "error": str(err)}


def new(logger: LoggerSingleton, db: Database, notifier: Notification) -> Scraper:
    """
    Factory function to create a Scraper instance with initialized Database and Notification.

    Returns:
        Scraper: An instance of Scraper with initialized dependencies.
    """
    return Scraper(logger, db, notifier)
