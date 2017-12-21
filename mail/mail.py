class Mail:
    def __init__(self, prot, *argv):
        # Declaration
        self.__prot = None

        # Initialization
        self.__prot = prot(*argv)

    def login(self, account, passwd):
        self.__prot.login(account, passwd)

    def send(self, frm, to, subject, content, attachments=None):
        self.__prot.send(frm, to, subject, content, attachments)

    def quit(self):
        self.__prot.quit()
