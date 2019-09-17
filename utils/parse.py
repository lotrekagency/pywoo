import inspect
import re
import sys
import json
from datetime import datetime

mapping = {}


def map_models():
    modules = [key for key, value in sys.modules.items() if key.startswith("models.")]
    for module in modules:
        classes = inspect.getmembers(sys.modules[module], inspect.isclass)
        for _class in classes:
            for member in inspect.getmembers(_class[1]):
                if '__init__' in member:
                    _vars = frozenset([re.sub(r"_$", "", arg) for arg in inspect.signature(member[1]).parameters.keys()
                                       if arg != 'self' and arg != 'api'])
                    if _vars in mapping:
                        print("Same frozenset mapped more than one time!", _vars)
                    mapping[_vars] = _class[1]


def find_mapping(data, api, url):
    if '_links' in data:
        del data['_links']
    try:
        return mapping[frozenset(data.keys())](*data.values(), api, url)
    except KeyError:
        print(data.keys(), "frozenset NOT FOUND")
        return dict(zip(data.keys(), data.values()))


def get_dict_data(data):
    data = data.__dict__
    keys_to_rename = [key for key in data.keys() if key.startswith("_")]
    for key in keys_to_rename:
        value = data[key]
        del data[key]
        data[key[1:]] = value
    data.pop('id', None)
    return data


def from_json(data, api, url):
    return json.loads(data, object_hook=lambda d: find_mapping(d, api, url))


def to_json(data):
    return get_dict_data(data)


def parse_date_time(date_time):
    return datetime.strptime(date_time, '%Y-%m-%dT%H:%M:%S').isoformat() if date_time else None
