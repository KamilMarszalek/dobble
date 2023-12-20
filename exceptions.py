class SymbolsError(Exception):
    """Raised when there is an error related to symbols."""

    pass


class DiffLevelError(Exception):
    """Raised when there is an error related to difficulty level."""

    pass


class InvalidComputersAmount(Exception):
    """Raised when the number of computers is invalid."""

    pass


class EmptyNameError(Exception):
    """Raised when a name is empty."""

    pass
