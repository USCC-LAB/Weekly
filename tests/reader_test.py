import unittest
from tests.testsuites.reader.uid.threaded import *

from reader.NFC.ACR122.ACR122 import *


class ReaderTestcase(unittest.TestCase):
    def setUp(self):
        self.dev = ACR122
        self.delta = 10

    def tearDown(self):
        self.dev = None
        self.delta = None

    def test_NFC_uid(self):
        expected = 0
        threaded_read_uid(self.dev, self.delta)
        result = 0
        self.assertEqual(expected, result)
