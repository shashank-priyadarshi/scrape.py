from ..abstract import Database, Notification


class Scraper:
    def __init__(self, database: Database, notification: Notification):
        self.database = database
        self.notification = notification


def new(database: Database, notification: Notification) -> Scraper:
    """
    Factory function to create a Scraper instance with initialized Database and Notification.

    Returns:
        Scraper: An instance of Scraper with initialized dependencies.
    """
    return Scraper(database, notification)
