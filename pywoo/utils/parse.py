import inspect
import re
import json
from datetime import datetime
from pywoo.utils.models import ApiSuperClass, ApiObject

mapping = {}


class ClassParser(object):
    def __init__(self, url=None, other_func=[]):
        self.url = url
        self._other_func = other_func

    def __call__(self, cls, *args, **kwargs):
        setattr(cls.__init__, "_url", self.url)

        funcs = self._other_func + [cls.__init__]

        for func in funcs:
            vars = [re.sub(r"_$", "", arg) for arg in inspect.signature(func).parameters.keys()
                    if arg != 'self' and arg != 'api' and arg != 'url']
            vars = frozenset(vars)
            if vars in mapping:
                mapping[vars].append(cls)
            else:
                mapping[vars] = [cls]

        return cls


def find_mapping(data, api, url):
    if '_links' in data:
        del data['_links']
    try:
        list_cls = mapping[frozenset(data.keys())]
        cls = type

        if len(list_cls) == 1:
            cls = list_cls[0]
        else:
            for mapped_cls in list_cls:
                regex_url = getattr(mapped_cls.__init__, "_url", "")
                if re.match(regex_url, url):
                    cls = mapped_cls
                    break

        if issubclass(cls, ApiObject):
            return cls(*data.values(), api, url)
        else:
            return cls(*data.values())
    except KeyError:
        return dict(zip(data.keys(), data.values()))


def get_dict_data(data):
    data = data.__dict__
    return {key: (get_dict_data(value) if issubclass(type(value), ApiSuperClass) else value) for key, value in data.items() if not key.startswith("_") and not value is None}


def from_json(data, api, url):
    print(url)
    print(re.split('/', url)[-1])
    #return json.loads(data, object_hook=lambda d: find_mapping(d, api, url))


def to_json(data):
    return get_dict_data(data)


def parse_date_time(date_time):
    return datetime.strptime(date_time, '%Y-%m-%dT%H:%M:%S').isoformat() if date_time else None
