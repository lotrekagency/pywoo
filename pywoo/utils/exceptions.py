class ReadOnlyException(Exception):
    """
    Exception raised when trying to edit a readonly attribute.

    *Nothing to see here.*
    """
    def __init__(self, key):
        super().__init__(f'{key} attribute is read-only')


class WriteOnlyException(Exception):
    """
    Exception raised when trying to read a writeonly attribute.

    *Nothing to see here.*
    """
    def __init__(self, key):
        super().__init__(f'{key} attribute is write-only')
