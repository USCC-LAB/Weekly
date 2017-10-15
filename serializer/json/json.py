import json

class Json:
    def serialize(data):
        if type(data) is dict:
            return json.dumps(data)

    def deserialize(data):
        if type(data) is str:
            return json.loads(data)
