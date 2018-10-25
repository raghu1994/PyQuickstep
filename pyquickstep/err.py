

class QuickstepError(Exception):
    """Exception related to operation with MySQL."""


class Error(QuickstepError):
    """Exception that is the base class of all other error exceptions
    (not Warning)."""

class DatabaseError(Error):
    """Exception raised for errors that are related to the
    database."""

class ProgrammingError(DatabaseError):
    """Exception raised for programming errors, e.g. table not found
    or already exists, syntax error in the SQL statement, wrong number
    of parameters specified, etc."""