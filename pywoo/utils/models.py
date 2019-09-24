from abc import ABC
from collections.abc import Mapping

from pywoo.utils.exceptions import WriteOnlyException, ReadOnlyException


class ApiSuperClass:
    ro_attributes = set()
    wo_attributes = set()
    rw_attributes = set()

    def __init__(self, **kwargs):
        self.__dict__ = kwargs

    def __getattr__(self, item):
        return self.__dict__['__dict__'][item]

    def __setattr__(self, key, value):
        self.__dict__['__dict__'][key] = value

    def __iter__(self):
        return iter(self._storage)

    def __len__(self):
        return len(self._storage)

    def get_raw_data(self):
        return self._storage


class ApiObject(ApiSuperClass):
    def __init__(self, api, url, **kwargs):
        super().__init__(**kwargs)
        self.__dict__['_api'] = api
        self.__dict__['_url'] = url


class ApiProperty(ApiSuperClass):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)


class MetaData(ApiProperty):
    ro_attributes = {'id'}
    rw_attributes = {'key', 'value'}
