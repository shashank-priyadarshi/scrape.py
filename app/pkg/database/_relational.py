from typing import Any, Dict

from ..abstract import Database


class _Relational(Database):
    def __init__(self, db_path: str):
        """Initializes a new instance of Relational.

        Args:
            db_path(str): DB connection string.

        """
        self.db_path = db_path
        self.connection = None

    def connect(self):
        raise NotImplementedError

    def disconnect(self):
        raise NotImplementedError

    def create(self, data: Dict[str, Any]):
        raise NotImplementedError

    def read(self, identifier: Any) -> Dict[str, Any]:
        raise NotImplementedError

    def update(self, identifier: Any, data: Dict[str, Any]):
        raise NotImplementedError

    def delete(self, identifier: Any):
        raise NotImplementedError


def _new() -> _Relational:
    return _Relational("")
