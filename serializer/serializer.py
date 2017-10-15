class Serializer:
    def __init__(self, serialize_obj):
        # Declaration
        self.serialize_obj = None

        # Initialization
        self.setUp(serialize_obj)
    
    def setUp(self, serialize_obj):
        self.serialize_obj = serialize_obj

    def serialize(self, data):
        return self.serialize_obj.serialize(data)

    def deserialize(self, data):
        return self.serialize_obj.deserialize(data)
