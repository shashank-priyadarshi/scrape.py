from abc import abstractmethod

from ..abstract import Notification


class Console(Notification):
    @abstractmethod
    def __init__(self):
        """Initializes a new instance of Console."""

    def notify(self, message: str, sender: str, recipient: str):
        try:
            print(f"Notification from {sender} to {recipient}: {message}")
        except Exception as e:
            print(f"Failed to log notification: {e}")
            raise
