from ..abstract import Database, Notification
from ..logger.logger import LoggerSingleton
from ..scraper import Scraper
from ._scrape import _new as new_scrape


class Service:
    def __init__(self, logger: LoggerSingleton, db: Database, notifier: Notification, scraper: Scraper):
        self.scraper = new_scrape(logger, db, notifier, scraper)


def new(logger: LoggerSingleton, db: Database, notifier: Notification, scraper: Scraper) -> Service:
    return Service(logger, db, notifier, scraper)
