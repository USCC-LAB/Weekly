from serializer import serializer
from serializer.prot import jsonlib


Serializer = serializer.Serializer(jsonlib.Json())

def json_serialize(dict_data):
    return Serializer.dumps(dict_data)


def json_deserialize(raw_data):
    return Serializer.loads(raw_data)

def json_write(path, dict_data):
    return Serializer.write(path, dict_data)

def json_read(path):
    return Serializer.read(path)

def json_append(path, dict_data):
    return Serializer.append(path, dict_data)
