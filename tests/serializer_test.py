import unittest
import os
from tests.testsuites.serializer.test_json import *


class SerializationTestcase(unittest.TestCase):
    def setUp(self):
        self.raw_data = "{\"name\":\"john\",\"age\":22,\"class\":\"mca\"}"
        self.dict_data = {'age': 22, 'class': 'mca', 'name': 'john'}

        self.tst = "__serializer_test.json"

    def tearDown(self):
        os.remove(self.tst) if os.path.isfile(self.tst) else True

    def test_json_serialize(self):
        expected = self.raw_data
        result = json_serialize(self.dict_data)
        self.assertDictEqual(json_deserialize(
            expected), json_deserialize(result))

    def test_json_deserialize(self):
        expected = self.dict_data
        result = json_deserialize(self.raw_data)
        self.assertDictEqual(expected, result)

    def test_json_write_read(self):
        expected = self.dict_data
        json_write(self.tst, self.dict_data)
        result = json_read(self.tst)
        self.assertDictEqual(expected, result)
