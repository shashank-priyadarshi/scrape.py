from abc import ABC, abstractmethod


class Notification(ABC):
    @abstractmethod
    def notify(self, message: str, sender: str, recipient: str):
        """
        Send a notification message to a recipient.

        Args:
            message (str): The content of the notification.
            sender (str): The sender of the notification.
            recipient (str): The recipient of the notification.

        Raises:
            NotImplementedError: If the method is not overridden in a subclass.
        """
