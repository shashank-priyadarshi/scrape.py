from ..abstract import Notification


class _Console(Notification):
    def __init__(self):
        """Initializes a new instance of Console."""

    def notify(self, message: str, sender: str, recipient: str):
        try:
            print(f"Notification from {sender} to {recipient}: {message}")
        except Exception as e:
            print(f"Failed to log notification: {e}")
            raise


def _new() -> _Console:
    return _Console()
