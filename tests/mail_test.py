import unittest
from tests.mail_testsuite.dummy_mail.smtp.dummy import *

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
