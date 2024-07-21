from ..abstract import Database, Notification
from ..scraper import Scraper
from ._scrape import _new as new_scrape


class Service:
    def __init__(self, db: Database, notifier: Notification, scraper: Scraper):
        self.scraper = new_scrape(db, notifier, scraper)


def new(db: Database, notifier: Notification, scraper: Scraper) -> Service:
    return Service(db, notifier, scraper)
