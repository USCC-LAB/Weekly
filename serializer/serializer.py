class Serializer:
    def __init__(self, serialize_obj):
        # Declaration
        self.serialize_obj = None

        # Initialization
        self.setUp(serialize_obj)

    def setUp(self, serialize_obj):
        self.serialize_obj = serialize_obj

    def dumps(self, data):
        return self.serialize_obj.dumps(data)

    def loads(self, data):
        return self.serialize_obj.loads(data)

    def write(self, path, data):
        return self.serialize_obj.write(path, data)

    def read(self, data):
        return self.serialize_obj.read(data)

    def append(self, path, data):
        return self.serialize_obj.append(path, data)
