class Serializer:
    def __init__(self, serialize_obj):
        self.serialize_obj = serialize_obj

    def serialize(self, data):
        return self.serialize_obj.serialize(data)

    def deserialize(self, data):
        return self.serialize_obj.deserialize(data)
