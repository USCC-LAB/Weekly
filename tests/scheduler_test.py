import unittest
from tests.scheduler_testsuite.order import *

class SchedulerTestcase(unittest.TestCase):
    def setUp(self):
        pass

    def tearDown(self):
        pass

    def test_order(self):
        expected = True
        result = iter_regist()
        self.assertEqual(expected, result)
