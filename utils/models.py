class ApiObject:
    def __init__(self, api):
        self._api = api


class MetaData(ApiObject):
    def __init__(self, id, key, value, api):
        super().__init__(api)
        self._id = id
        self.key = key
        self.value = value

    @property
    def id(self):
        return self._id
