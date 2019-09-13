import json

from api import mapping


def find_mapping(data, api):
    if '_links' in data:
        del data['_links']
    return mapping[data.keys()](*data.values(), api)


def get_dict_data(data):
    data = data.__dict__
    keys_to_rename = [key for key in data.keys() if key.startswith("_")]
    for key in keys_to_rename:
        value = data[key]
        del data[key]
        data[key[1:]] = value
    return data


class ApiObject:
    def __init__(self, api):
        self._api = api

    @staticmethod
    def from_json(data, api):
        return json.loads(data, object_hook=lambda d: find_mapping(d, api))

    @staticmethod
    def to_json(data):
        return json.dumps(get_dict_data(data), default=get_dict_data)


class MetaData:
    def __init__(self, id=None, key=None, value=None):
        self._id = id
        self.key = key
        self.value = value

    @property
    def id(self):
        return self._id
