from abc import abstractmethod

from ..abstract import Notification


class Email(Notification):
    @abstractmethod
    def __init__(self):
        """Initializes a new instance of Email."""

    def notify(self, message: str, sender: str, recipient: str):
        raise NotImplementedError
