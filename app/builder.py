from pkg.api.api import new as new_routers
from pkg.database import new as new_database
from pkg.logger.logger import LoggerSingleton
from pkg.notification import new as new_notifier
from pkg.scraper import new as new_scraper
from pkg.service import new as new_services


class Builder:
    def __init__(self, db_type: str, notification_type: str, scraper_type: str):
        """
        Initialize the Builder with types for each component.

        Args:
            db_type (str): The type of database (e.g., 'inmem', 'file', 'relational').
            notification_type (str): The type of notification (e.g., 'console', 'email').
            scraper_type (str): The type of scraper (e.g., 'basic', 'advanced').
        """
        self._db_type = db_type
        self._notification_type = notification_type
        self._scraper_type = scraper_type

        # Initialize singleton instances
        self.logger = get_logger()
        self.db = self.get_db()
        self.notifier = self.get_notification()
        self.scraper = get_scraper()
        self.service = self.get_services()
        self.routers = self.get_routers()

    def get_db(self):
        """
        Initialize and return the database based on the provided type.

        Returns:
            Database: An instance of the specified database type.
        """
        return new_database(self._db_type)

    def get_notification(self):
        """
        Initialize and return the notification system based on the provided type.

        Returns:
            Notification: An instance of the specified notification type.
        """
        return new_notifier(self._notification_type)

    def get_services(self):
        """
        Initialize and return the services based on the provided type.

        Returns:
            Service: An instance of the specified service type.
        """
        return new_services(self.logger, self.db, self.notifier, get_scraper())

    def get_routers(self):
        """
        Initialize and return the API routers.

        Returns:
            Router: The configured API routers.
        """
        return new_routers(self.logger, self.service).v1routes


def get_logger():
    return LoggerSingleton().get_logger()


def get_scraper():
    """
    Initialize and return the scraper based on the provided type.

    Returns:
        Scraper: An instance of the specified scraper type.
    """
    return new_scraper()
