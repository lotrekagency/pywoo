import inspect
import re
import json
import pywoo.models

from datetime import datetime
from pywoo.utils.models import ApiSuperClass, ApiObject


urls_classes = {}


class ClassParser:
    def __init__(self, url_class=None):
        self.url_class = url_class

    def __call__(self, cls, *args, **kwargs):
        attrs = cls.ro_attributes.union(cls.wo_attributes).union(cls.rw_attributes)

        if self.url_class:
            urls_classes[self.url_class] = {frozenset(attrs): cls}
        return cls


def find_mapping(data, api, url):
    if '_links' in data:
        del data['_links']
    try:
        cls = None

        for attrs, class_ in urls_classes[url].items():
            print(data.keys(), attrs)
            if set(data.keys()).issubset(attrs):
                cls = class_
                break

        if cls:
            if issubclass(cls, ApiObject):
                return cls(api, url, **data)
            else:
                return cls(**data)
        else:
            return data
    except KeyError:
        return dict(zip(data.keys(), data.values()))


def get_dict_data(data):
    data = data.__dict__
    return {key: (get_dict_data(value) if issubclass(type(value), ApiSuperClass) else value) for key, value in
            data.items() if not key.startswith("_") and not value is None}


def to_json(data):
    return get_dict_data(data)


def parse_date_time(date_time):
    return datetime.strptime(date_time, '%Y-%m-%dT%H:%M:%S').isoformat() if date_time else None


def from_json(data, api, url):
    url_obj = url.rpartition('/')[-1]
    return json.loads(data, object_hook=lambda d: find_mapping(d, api, url_obj))
