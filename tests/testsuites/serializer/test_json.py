from serializer import serializer
from serializer.json import json


def json_serialize(dict_data):
    Serializer = serializer.Serializer(json.Json)
    return Serializer.serialize(dict_data)


def json_deserialize(raw_data):
    Serializer = serializer.Serializer(json.Json)
    return Serializer.deserialize(raw_data)
