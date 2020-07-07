"""
This module contains classes, functions and global variables used for translating JSON objects into model objects
and viceversa, and **should not be touched** when using pywoo.
"""

import json

from datetime import datetime
from pywoo.utils.models import ApiSuperClass, ApiObject, ApiProperty, ApiActiveProperty

urls_classes = {}


class ClassParser:
    """
    Class used for parsing models classes.

    *Nothing to see here.*
    """
    def __init__(self, url_class):
        self.url_class = url_class

    def __call__(self, cls, *args, **kwargs):
        attrs = cls._ro_attributes.union(cls._rw_attributes)

        if self.url_class in urls_classes:
            urls_classes[self.url_class][frozenset(attrs)] = cls
        else:
            urls_classes[self.url_class] = {frozenset(attrs): cls}
        return cls


def find_mapping(data, api, url):
    """
    Function used for matching model classes to JSON objects coming from Woocommerce REST API.

    :param data: JSON data
    :type data: dict, list
    :param api: :class:`~pywoo.Api` object
    :type api: pywoo.Api
    :param url: Woocommerce REST API url used for retrieving data
    :type url: str
    :rtype: object
    """
    if '_links' in data:
        del data['_links']
    cls = None

    key_url = url.rpartition('/')[-1]
    for attrs, class_ in urls_classes[key_url].items():
        if attrs.issubset(set(data.keys())):
            cls = class_
            break

    for key in data.keys():
        if key.startswith("date") and isinstance(data[key], str):
            data[key] = parse_date_time(data[key])

    if cls:
        if issubclass(cls, ApiObject):
            return cls(api, url, **data)
        elif issubclass(cls, ApiActiveProperty):
            return cls(api, **data)
        elif issubclass(cls, ApiProperty):
            return cls(**data)
    else:
        return data


def to_dict(data):
    """
    Function used to transform data models objects in JSON (``dict``, ``list``) data.

    :param data: object data
    :type data: str
    :rtype: list, dict
    """
    if issubclass(type(data), ApiSuperClass):
        dict_data = data.__dict__
        return {key: to_dict(value) for key, value in dict_data.items() if
                not key.startswith("_") and value is not None}
    elif type(data) == datetime:
        return data.strftime('%Y-%m-%dT%H:%M:%S')
    elif type(data) == list:
        return [to_dict(d) for d in data]
    elif type(data) == dict:
        return {key: to_dict(value) for key, value in data.items()}
    return data


def parse_date_time(date_time):
    """
    Function used to parse datetime strings coming from Woocommerce REST API.

    :param date_time: datetime string in ``%Y-%m-%dT%H:%M:%S`` format
    :type date_time: str
    :rtype: datetime.datetime
    """
    if date_time and isinstance(date_time, str):
        for pattern in ['%Y-%m-%dT%H:%M:%S', '%Y-%m-%d %H:%M:%S.%f']:
            try:
                return datetime.strptime(date_time, pattern)
            except ValueError:
                pass
    return None


def from_json(data, api, url):
    """
    Function used to load JSON data into models objects.

    :param data: JSON data
    :type data: dict, list
    :param api: :class:`~pywoo.Api` object
    :type api: pywoo.Api
    :param url: Woocommerce REST API url used for retrieving data
    :type url: str
    :rtype: object
    """
    return json.loads(data, object_hook=lambda d: find_mapping(d, api, url))
