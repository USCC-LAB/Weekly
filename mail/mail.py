class mail:
    def __init__(self, prot, *argv):
        self.prot = prot(*argv)

    def login(self, account, passwd):
        self.prot.login(account, passwd)

<<<<<<< HEAD
<<<<<<< HEAD
    def send(self, frm, to, subject, content):
        self.prot.send(frm, to, subject, content)
=======
    def send(self, frm, to, subject, content, *attachments):
        self.prot.send(frm, to, subject, content, attachments)
>>>>>>> d3c9f75... Simplify send function and delete duplicate code
=======
    def send(self, frm, to, subject, content, *attachments):
        self.prot.send(frm, to, subject, content, attachments)
>>>>>>> origin/dev

    def quit(self):
        self.prot.quit()
