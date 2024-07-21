from ..abstract import Notification
from ._console import _new as new_console
from ._email import _new as new_email


def new(notifier_type: str) -> Notification:
    """
    Factory function to create a Notifier instance based on the specified type.

    Args:
        notifier_type (str): The type of notifier to create ('console', 'email').

    Returns:
        Notification: An instance of a subclass of Notification.

    Raises:
        ValueError: If the specified notifier type is not supported.
    """

    notifier_switch = {
        'console': new_console,
        'email': new_email
    }

    try:
        return notifier_switch[notifier_type.lower()]()
    except KeyError as exc:
        raise ValueError(f'Database type {notifier_type} not supported.') from exc
