import json


class Json:
    def __init__(self):
        # Helper functions
        self.__isDict = lambda var: isinstance(var, dict)
        self.__isStr = lambda var: isinstance(var, str)

    def dumps(self, data):
        return json.dumps(data) if self.__isDict(data) else None

    def loads(self, data):
        return json.loads(data) if self.__isStr(data) else None
