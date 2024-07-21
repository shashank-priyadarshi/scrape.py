from fastapi import HTTPException

from ..abstract import Database, Notification
from ..entity.v1.common_pb2 import request
from ..scraper import Scraper


class _Scrape:
    def __init__(self, db: Database, notification: Notification, scraper: Scraper):
        self.db = db
        self.notification = notification
        self.scraper = scraper

    async def scrape_and_save(self, req: request):
        try:
            content = await self.scraper.scrape(req.url)

            self.db.create({"url": req.url, "content": content})

            self.notification.notify(f"Scraping of {req.url} completed.", "scraper-service", "admin")

            return {"message": "Scraping and saving completed successfully."}

        except Exception as e:
            raise HTTPException(status_code=500, detail=str(e)) from e


def _new(db: Database, notification: Notification, scraper: Scraper) -> _Scrape:
    return _Scrape(db, notification, scraper)
