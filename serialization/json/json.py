from serialization import singleton
import json

class Json(singleton.SingletonMixin):
    def serialize(data):
        if type(data) is dict:
            return json.dumps(data)



