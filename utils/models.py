class ApiObject:
    def __init__(self, api):
        self._api = api


class MetaData:
    def __init__(self, id=None, key=None, value=None):
        self._id = id
        self.key = key
        self.value = value

    @property
    def id(self):
        return self._id
