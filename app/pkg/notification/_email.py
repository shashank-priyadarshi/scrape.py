from ..abstract import Notification


class _Email(Notification):
    def __init__(self):
        """Initializes a new instance of Email."""

    def notify(self, message: str, sender: str, recipient: str):
        raise NotImplementedError


def _new() -> _Email:
    return _Email()
