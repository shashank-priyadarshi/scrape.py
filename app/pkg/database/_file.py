from typing import Any

from ..abstract import Database


class _File(Database):
    def __init__(self):
        pass

    def connect(self):
        # open file
        raise NotImplementedError

    def disconnect(self):
        # close file
        raise NotImplementedError

    def create(self, data: Any):
        raise NotImplementedError

    def read(self, identifier: Any) -> Any:
        raise NotImplementedError

    def update(self, identifier: Any, data: Any):
        raise NotImplementedError

    def delete(self, identifier: Any):
        raise NotImplementedError


def _new() -> _File:
    return _File()
