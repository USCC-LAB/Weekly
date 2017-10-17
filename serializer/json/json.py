import json


class Json:
    def dumps(data):
        if isinstance(data, dict):
            return json.dumps(data)

    def loads(data):
        if isinstance(data, str):
            return json.loads(data)
