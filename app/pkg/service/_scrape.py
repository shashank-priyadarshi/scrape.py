from fastapi import HTTPException

from ..abstract import Database, Notification
from ..entity.v1.common_pb2 import request, response
from ..logger.logger import LoggerSingleton
from ..scraper import Scraper


class _Scrape:
    def __init__(self, logger: LoggerSingleton, db: Database, notification: Notification, scraper: Scraper):
        self.logger = logger
        self.db = db
        self.notification = notification
        self.scraper = scraper

    async def scrape_and_save(self, req: request):
        try:
            self.logger.info(f"Starting scrape for URL: {req.url}")
            content = await self.scraper.scrape(req.url)
            self.logger.info(f"Scrape completed for URL: {req.url}, saving to database.")

            self.db.create({"url": req.url, "content": content})

            self.logger.info("Scrape result saved to database, sending notification.")
            self.notification.notify(f"Scraping of {req.url} completed.", "scraper-service", "admin")

            self.logger.info(f"Notification sent for URL: {req.url}.")
            return response(status_code=200, message="Scraped and saved successfully")

        except Exception as e:
            self.logger.error(f"Error during scrape_and_save: {str(e)}")
            raise HTTPException(status_code=500, detail=str(e)) from e


def _new(logger: LoggerSingleton, db: Database, notification: Notification, scraper: Scraper) -> _Scrape:
    return _Scrape(logger, db, notification, scraper)
