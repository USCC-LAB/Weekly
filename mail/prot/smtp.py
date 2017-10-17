import smtplib


class Smtp:
    def __init__(self, *argv):
        # Declaration
        self.__smtp_obj = None

        # Initialization
        if () != argv:
            self.__smtp_obj = smtplib.SMTP_SSL(*argv)
        else:
            self.__smtp_obj = self.default_setup()

    # Set Gmail server as default
    def default_setup(self):
        return smtplib.SMTP_SSL('smtp.gmail.com', 465)

    def login(self, account, passwd):
        self.__smtp_obj.login(account, passwd)

    def send(self, frm, to, subject, content):
        self.__smtp_obj.sendmail(
            frm, to, 'Subject:' + subject + '\n' + content)

    def quit(self):
        self.__smtp_obj.quit()
