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

    def write(self, path, data):
        with open(path, 'w') as fd:
            return json.dump(data, fd) if self.__isDict(data) else True

    def read(self, path):
        with open(path, 'r') as fd:
            return json.load(fd)

    def append(self, path, data):
        with open(path, 'a') as fd:
            return json.dump(data, fd) if self.__isDict(data) else True
