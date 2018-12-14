
from pyquickstep.error.error import Error


class DatabaseError(Error):
    """Exception raised for errors that are related to the database.
    It must be a subclass of Error."""


class DataError(DatabaseError):
    """Exception raised for errors that are due to problems with the
    processed data like division by zero, numeric value out of range,
     etc. It must be a subclass of DatabaseError."""


class OperationalError(DatabaseError):
    """Exception raised for errors that are related to the database's
    operation and not necessarily under the control of the programmer,
    e.g. an unexpected disconnect occurs, the data source name is not
    found, a transaction could not be processed, a memory allocation
    error occurred during processing, etc. It must be a subclass of
    DatabaseError."""


class IntegrityError(DatabaseError):
    """Exception raised when the relational integrity of the database
    is affected, e.g. a foreign key check fails. It must be a subclass
    of DatabaseError."""


class InternalError(DatabaseError):
    """Exception raised when the database encounters an internal error,
    e.g. the cursor is not valid anymore, the transaction is out of sync,
    etc. It must be a subclass of DatabaseError."""


class ProgrammingError(DatabaseError):
    """Exception raised for programming errors, e.g. table not found or
    already exists, syntax error in the SQL statement, wrong number of
    parameters specified, etc. It must be a subclass of DatabaseError."""


class NotSupportedError(DatabaseError):
    """Exception raised in case a method or database API was used which
    is not supported by the database, e.g. requesting a .rollback() on a
    connection that does not support transaction or has transactions turned
    off. It must be a subclass of DatabaseError."""