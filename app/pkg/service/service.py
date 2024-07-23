from ..logger.logger import LoggerSingleton
from ..scraper import Scraper
from ._scrape import _new as new_scrape


class Service:
    def __init__(self, logger: LoggerSingleton, scraper: Scraper):
        self.scraper = new_scrape(logger, scraper)


def new(logger: LoggerSingleton, scraper: Scraper) -> Service:
    return Service(logger, scraper)
