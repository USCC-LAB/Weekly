import unittest
from tests.mail_testsuite.dummy_mail.smtp.dummy import *

class mail_testcase(unittest.TestCase):
    def setUp(self):
        account = ''
        password = ''
        assert account != ''
        assert password != ''
        attachments = []
        if len(sys.argv) > 3:
            for i in range(3, len(sys.argv)):
                attachments.append(sys.argv[i])
        self.args = (account, password, attachments)

    def tearDown(self):
        self.args = None

    def test_smtp_dummy(self):
        expected = 0
        result = smtp_dummy(*self.args)
        self.assertEqual(expected, result)
