import unittest
from tests.testsuites.roulette.person_on_duty import *

class RouletteTestcase(unittest.TestCase):
    def setUp(self):
        self.cands = ('Yen', 'Jacky', 'Haha')

    def tearDown(self):
        self.cands = None

    def test_shift_policy(self):
        expected = True
        result = person_on_duty(self.cands)
        self.assertEqual(expected, result)
