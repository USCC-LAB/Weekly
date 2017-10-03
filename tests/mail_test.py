import unittest
from tests.testsuites.mail.dummy_mail.smtp_dummy import *

class MailTestcase(unittest.TestCase):
    def setUp(self):
        account = ''
        password = ''
        assert account != ''
        assert password != ''
        self.args = (account, password)

    def tearDown(self):
        self.args = None

    def test_smtp_dummy(self):
        expected = 0
        result = smtp_dummy(*self.args)
        self.assertEqual(expected, result)
