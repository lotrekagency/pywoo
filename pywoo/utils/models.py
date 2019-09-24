from abc import ABC
from collections.abc import Mapping

from pywoo.utils.exceptions import WriteOnlyException, ReadOnlyException


class ApiSuperClass(Mapping, ABC):
    ro_attributes = {}
    wo_attributes = {}
    rw_attributes = {}

    def __init__(self, **kwargs):
        self._storage = kwargs

    def __getitem__(self, key):
        if not key in self.wo_attributes:
            return self._storage[key]
        raise WriteOnlyException(key)

    def __getattr__(self, item):
        return self.__getitem__(item)

    def __setitem__(self, key, value):
        if not key in self.ro_attributes:
            self._storage[key] = value
        else:
            raise ReadOnlyException(key)

    def __setattr__(self, key, value):
        self.__setitem__(key, value)

    def __iter__(self):
        return iter(self._storage)

    def __len__(self):
        return len(self._storage)

    def get_raw_data(self):
        return self._storage


class ApiObject(ApiSuperClass, ABC):
    def __init__(self, api, url, **kwargs):
        super().__init__(**kwargs)
        self._api = api
        self._url = url


class ApiProperty(ApiSuperClass, ABC):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)


class MetaData(ApiProperty):
    ro_attributes = {'id'}
    rw_attributes = {'key', 'value'}
