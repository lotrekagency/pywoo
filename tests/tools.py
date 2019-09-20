import json
import os

class MockResponse:
    def __init__(self, text, ok=True, status_code=200):
        self.text = text
        self.ok = ok
        self.status_code = status_code

    def json(self):
        return json.loads(self.text)


def mock_request(method, url, *args, **kwargs):
    file = open(os.path.join(*(['.', 'tests'] + ['resources'] + url.split("/") + [method.lower() + ".json"])), 'r')
    response = MockResponse(file.read())
    file.close()
    return response
