from serializer import serializer
from serializer.prot import jsonlib


def json_serialize(dict_data):
    Serializer = serializer.Serializer(jsonlib.Json())
    return Serializer.dumps(dict_data)


def json_deserialize(raw_data):
    Serializer = serializer.Serializer(jsonlib.Json())
    return Serializer.loads(raw_data)
