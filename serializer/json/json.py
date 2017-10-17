import json


class Json:
    def serialize(data):
        if isinstance(data, dict):
            return json.dumps(data)

    def deserialize(data):
        if isinstance(data, str):
            return json.loads(data)
