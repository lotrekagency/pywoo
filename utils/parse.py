import inspect
import sys
import json

mapping = {}

def map_models():
    modules = [key for key, value in sys.modules.items() if key.startswith("models.")]
    for module in modules:
        classes = inspect.getmembers(sys.modules[module], inspect.isclass)
        for _class in classes:
            for member in inspect.getmembers(_class[1]):
                if '__init__' in member:
                    _vars = frozenset([arg for arg in inspect.signature(member[1]).parameters.keys() if
                             arg != 'self' and arg != 'api'])
                    mapping[_vars] = _class[1]

def find_mapping(data, api):
    if '_links' in data:
        del data['_links']
    if 'href' in data or 'self' in data or 'collection' in data:
        return {}
    return mapping[frozenset(data.keys())](*data.values(), api)

def get_dict_data(data):
    data = data.__dict__
    keys_to_rename = [key for key in data.keys() if key.startswith("_")]
    for key in keys_to_rename:
        value = data[key]
        del data[key]
        data[key[1:]] = value
    return data

def from_json(data, api):
    return json.loads(data, object_hook=lambda d: find_mapping(d, api))

def to_json(data):
    return json.dumps(get_dict_data(data), default=get_dict_data)