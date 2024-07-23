from ..abstract.database import Database
from ..logger.logger import LoggerSingleton
from ..scraper import Scraper
from ._auth import _new as new_auth
from ._scrape import _new as new_scrape


class Service:
    def __init__(self, logger: LoggerSingleton, db: Database, scraper: Scraper):
        self.auth = new_auth(logger, db)
        self.scraper = new_scrape(logger, scraper)


def new(logger: LoggerSingleton, db: Database, scraper: Scraper) -> Service:
    return Service(logger, db, scraper)
