class ReadOnlyException(Exception):
    def __init__(self, key):
        super().__init__(f'{key} attribute is read-only')


class WriteOnlyException(Exception):
    def __init__(self, key):
        super().__init__(f'{key} attribute is write-only')
