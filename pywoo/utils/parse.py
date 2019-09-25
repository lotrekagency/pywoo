import inspect
import re
import json
import pywoo.models

from datetime import datetime
from pywoo.utils.models import ApiSuperClass, ApiObject, ApiProperty

urls_classes = {}


class ClassParser:
    def __init__(self, url_class):
        self.url_class = url_class

    def __call__(self, cls, *args, **kwargs):
        attrs = cls.ro_attributes.union(cls.rw_attributes)

        if self.url_class in urls_classes:
            urls_classes[self.url_class][frozenset(attrs)] = cls
        else:
            urls_classes[self.url_class] = {frozenset(attrs): cls}
        return cls


def find_mapping(data, api, url):
    if '_links' in data:
        del data['_links']
    cls = None

    key_url = url.rpartition('/')[-1]
    for attrs, class_ in urls_classes[key_url].items():
        if attrs.issubset(set(data.keys())):
            cls = class_
            break

    if cls:
        if issubclass(cls, ApiObject):
            return cls(api, url, **data)
        elif issubclass(cls, ApiProperty):
            print(cls)
            return cls(**data)
    else:
        return data


def get_dict_data(data):
    data = data.__dict__
    return {key: (get_dict_data(value) if issubclass(type(value), ApiSuperClass) else value) for key, value in
            data.items() if not key.startswith("_") and not value is None}


def to_json(data):
    return get_dict_data(data)


def parse_date_time(date_time):
    return datetime.strptime(date_time, '%Y-%m-%dT%H:%M:%S').isoformat() if date_time else None


def from_json(data, api, url):
    return json.loads(data, object_hook=lambda d: find_mapping(d, api, url))
