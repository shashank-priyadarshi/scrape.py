from abc import abstractmethod
from typing import Any, Dict

from ..abstract import Database


class InMemory(Database):
    @abstractmethod
    def __init__(self):
        """
            Initializes a new instance of Relational.

            Args:
                db_path(str): DB connection string.
        """
        self._data: Dict[Any, Any] = {}

    def connect(self):
        pass

    def disconnect(self):
        pass

    def create(self, data: Any):
        item_id = len(self._data) + 1
        self._data[item_id] = data
        print(f"Created record with ID {item_id}: {data}")

    def read(self, identifier: Any) -> Any:
        return self._data.get(identifier)

    def update(self, identifier: Any, data: Any):
        if identifier in self._data:
            self._data[identifier] = data
            print(f"Updated record with ID {identifier}: {data}")
        else:
            raise KeyError(f"Record with ID {identifier} not found.")

    def delete(self, identifier: Any):
        if identifier in self._data:
            del self._data[identifier]
            print(f"Deleted record with ID {identifier}.")
        else:
            raise KeyError(f"Record with ID {identifier} not found.")
