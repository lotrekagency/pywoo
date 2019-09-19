import os
from unittest.mock import Mock
from requests import Response


def mock_request(method, url):
    file = open(os.path.join(*(['resources'] + url.split("/") + [method.lower() + ".json"])), 'rb')
    response = Mock(spec=Response)
    response.status_code = 200
    response.raw = file.read()
    return response
