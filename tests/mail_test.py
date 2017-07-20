import unittest
from tests.mail_testsuite.dummy_mail.smtp.dummy import *

class mail_testcase(unittest.TestCase):
    def setUp(self):
        account = ''
        password = ''
        self.args = (account, password)

    def tearDown(self):
        self.args = None

    def test_smtp_dummy(self):
        expected = 0
        result = smtp_dummy(*self.args)
        self.assertEqual(expected, result)
