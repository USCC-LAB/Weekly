from serializer import serializer
from serializer.prot import jsonlib


Serializer = serializer.Serializer(jsonlib.Json())

def json_serialize(dict_data):
    return Serializer.dumps(dict_data)


def json_deserialize(raw_data):
    return Serializer.loads(raw_data)
