class mail:
    def __init__(self, prot, *argv):
        self.prot = prot(*argv)

    def login(self, account, passwd):
        self.prot.login(account, passwd)

    def send(self, frm, to, subject, content, *attachments):
        self.prot.send(frm, to, subject, content, attachments)

    def quit(self):
        self.prot.quit()
