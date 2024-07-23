from fastapi import HTTPException

from ..entity.v1.common_pb2 import request, response
from ..logger.logger import LoggerSingleton
from ..scraper import Scraper


class _Scrape:
    def __init__(self, logger: LoggerSingleton, scraper: Scraper):
        self.logger = logger
        self.scraper = scraper

    async def scrape_and_save(self, req: request):
        try:
            await self.scraper.scrape(req.url)

            return response(status_code=200, message="Started scraping {}".format(req.url))

        except Exception as e:
            self.logger.error(f"Error during scrape_and_save: {str(e)}")
            raise HTTPException(status_code=500, detail=str(e)) from e


def _new(logger: LoggerSingleton, scraper: Scraper) -> _Scrape:
    return _Scrape(logger, scraper)
