import unittest
import json
from tests.testsuites.serializer.test_json import *


class SerializationTestcase(unittest.TestCase):
    def setUp(self):
        self.raw_data = "{\"name\":\"john\",\"age\":22,\"class\":\"mca\"}"
        self.dict_data = {'age': 22, 'class': 'mca', 'name': 'john'}

        assert self.raw_data != ''
        assert self.dict_data != None

    def test_json_serialize(self):
        expected = self.raw_data
        result = json_serialize(self.dict_data)
        self.assertDictEqual(json_deserialize(
            expected), json_deserialize(result))

    def test_json_deserialize(self):
        expected = self.dict_data
        result = json_deserialize(self.raw_data)
        self.assertDictEqual(expected, result)
