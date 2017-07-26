import unittest
from tests.mail_testsuite.dummy_mail.smtp.dummy import *

class mail_testcase(unittest.TestCase):
    def setUp(self):
        account = ''
        password = ''
        assert account != ''
        assert password != ''
<<<<<<< HEAD
        self.args = (account, password)
=======
        attachments = []

        self.args = (account, password, attachments)
>>>>>>> 289654f... Modify unittest function

    def tearDown(self):
        self.args = None

    def test_smtp_dummy(self):
        expected = 0
        result = smtp_dummy(*self.args)
        self.assertEqual(expected, result)
