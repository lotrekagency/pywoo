import inspect
import re
import json
import pywoo.models 

from datetime import datetime
from pywoo.utils.models import ApiSuperClass, ApiObject

mapping = {}
urls_classes = {}

class ClassParser(object):
    def __init__(self, url=None, other_func=[], url_class=""):
        self.url = url
        self._other_func = other_func
        self.url_class = url_class
        
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
        if self.url_class:
            urls_classes[self.url_class] = cls
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

def to_json(data):
    return get_dict_data(data)

def parse_date_time(date_time):
    return datetime.strptime(date_time, '%Y-%m-%dT%H:%M:%S').isoformat() if date_time else None

def from_json(data, api, url):
    url_obj = url.rpartition('/')[-1]
    return urls_classes[url_obj](data, api, url)
    #return json.loads(data, object_hook=lambda d: find_mapping(d, api, url))

