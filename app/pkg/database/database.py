from ..abstract.database import Database
from ._file import _new as new_file
from ._inmem import _new as new_inmem
from ._relational import _new as new_relational


def new(database_type: str) -> Database:
    """
    Factory function to create a Database instance based on the specified type.

    Args:
        database_type (str): The type of database to create ('file', 'inmem', 'relational').

    Returns:
        Database: An instance of a subclass of Database.

    Raises:
        ValueError: If the specified database type is not supported.
    """

    database_switch = {
        'file': new_file,
        'inmem': new_inmem,
        'relational': new_relational,
    }

    try:
        return database_switch[database_type.lower()]()
    except KeyError as exc:
        raise ValueError(f'Database type {database_type} not supported.') from exc
