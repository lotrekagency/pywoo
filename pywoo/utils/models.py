from pywoo.utils.exceptions import WriteOnlyException, ReadOnlyException


class ApiSuperClass(object):
    ro_attributes = set()
    wo_attributes = set()
    rw_attributes = set()

    def __init__(self, **kwargs):
        self.__dict__ = kwargs

    def __setattr__(self, key, value):
        if not key in self.ro_attributes:
            return super().__setattr__(key, value)
        else:
            raise ReadOnlyException(key)

    def __getattr__(self, item):
        if not item in self.wo_attributes:
            return super().__getattr__(item)
        else:
            raise WriteOnlyException(item)


class ApiObject(ApiSuperClass):
    def __init__(self, api, url, **kwargs):
        super().__init__(**kwargs)
        self._api = api
        self._url = url


class ApiActiveProperty(ApiSuperClass):
    def __init__(self, api, **kwargs):
        super().__init__(**kwargs)
        self._api = api


class ApiProperty(ApiSuperClass):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)


class MetaData(ApiProperty):
    ro_attributes = {'id'}
    rw_attributes = {'key', 'value'}
