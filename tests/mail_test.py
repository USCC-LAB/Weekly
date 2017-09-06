import unittest
from tests.mail_testsuite.dummy_mail.smtp.dummy import SmtpDummy


class MailTestCase(unittest.TestCase):
    def setUp(self):
        account = ''
        password = ''
        attachments = []
        assert account != ''
        assert password != ''
        self.args = (account, password, attachments)

    def tearDown(self):
        self.args = None

    def test_smtp_dummy(self):
        expected = 0
        result = SmtpDummy(*self.args)
        self.assertEqual(expected, result)
