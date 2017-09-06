class Mail:
    """
    This module is to send email by google smtp.
    You can use this module to send email.
    """

    def __init__(self, prot, *argv):
        self.prot = prot(*argv)

    def login(self, account, passwd):
        self.prot.login(account, passwd)

    def send(self, frm, to, content):
        self.prot.send(frm, to, content)

    def quit(self):
        self.prot.quit()
