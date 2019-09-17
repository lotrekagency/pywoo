class ApiObject:
    def __init__(self, api, url):
        self._api = api
        self._url = url


class MetaData:
    def __init__(self, id=None, key=None, value=None):
        self._id = id
        self.key = key
        self.value = value

    @property
    def id(self):
        return self._id
