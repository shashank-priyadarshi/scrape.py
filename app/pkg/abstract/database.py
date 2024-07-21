from abc import ABC, abstractmethod
from typing import Any


class Database(ABC):
    @abstractmethod
    def connect(self):
        """
        Establish a connection to the database.

        This method must be implemented by subclasses to set up a connection
        to the database. It should handle any necessary connection setup.

        Raises:
            NotImplementedError: If the method is not overridden in a subclass.
        """

    @abstractmethod
    def disconnect(self):
        """
        Close the connection to the database.

        This method must be implemented by subclasses to properly close the
        connection to the database and clean up any resources.

        Raises:
            NotImplementedError: If the method is not overridden in a subclass.
        """

    @abstractmethod
    def create(self, data: Any):
        """
        Create a new record in the database.

        Args:
            data (Any): The data to insert into the database. The format of the data
                        depends on the type of database (e.g., key-value, SQL query, JSON).

        Raises:
            NotImplementedError: If the method is not overridden in a subclass.
        """

    @abstractmethod
    def read(self, identifier: Any) -> Any:
        """
        Read a record from the database by its identifier.

        Args:
            identifier (Any): The identifier of the record to retrieve. The format
                              of the identifier depends on the type of database.

        Returns:
            Any: The record data. The format of the data depends on the type of database.

        Raises:
            NotImplementedError: If the method is not overridden in a subclass.
        """

    @abstractmethod
    def update(self, identifier: Any, data: Any):
        """
        Update an existing record in the database.

        Args:
            identifier (Any): The identifier of the record to update.
            data (Any): The new data for the record. The format of the data depends
                        on the type of database.

        Raises:
            NotImplementedError: If the method is not overridden in a subclass.
        """

    @abstractmethod
    def delete(self, identifier: Any):
        """
        Delete a record from the database by its identifier.

        Args:
            identifier (Any): The identifier of the record to delete.

        Raises:
            NotImplementedError: If the method is not overridden in a subclass.
        """

    def __enter__(self):
        """
        Enter the runtime context related to this object.

        This method is called when the `with` statement is executed. It should
        establish a connection to the database and return the instance.

        Returns:
            AbstractDatabase: The instance of the class.

        Raises:
            Exception: If there is an error while establishing the connection.
        """
        self.connect()
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        """
        Exit the runtime context related to this object.

        This method is called when the `with` statement exits. It should close
        the connection to the database and handle any necessary cleanup.

        Args:
            exc_type (type): The type of the exception raised, if any.
            exc_val (Exception): The exception instance, if any.
            exc_tb (traceback): The traceback object, if any.

        Returns:
            bool: False if exceptions should not be suppressed, True if they should be.

        Raises:
            Exception: If there is an error while closing the connection.
        """
        self.disconnect()
        return False
