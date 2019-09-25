from abc import ABC
from collections.abc import Mapping

from pywoo.utils.exceptions import WriteOnlyException, ReadOnlyException


class ApiSuperClass:
    ro_attributes = set()
    wo_attributes = set()
    rw_attributes = set()

    def __init__(self, **kwargs):
        self.__dict__ = kwargs

    def __setattr__(self, key, value):
        return super().__setattr__(key, value)

    def __getattr__(self, item):
        return super().__getattr__(item)


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
