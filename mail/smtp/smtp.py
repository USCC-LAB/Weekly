import smtplib

class smtp:
    # smtp_obj =

    def __init__(self, *argv):
        if None != argv:
            self.smtp_obj = smtplib.SMTP_SSL(argv)
        else:
            self.smtp_obj = self.default_setup()

    # Set Gmail server as default
    def default_setup(self):
        return smtplib.SMTP_SSL('smtp.gmail.com', 465)

    def login(self, account, passwd):
        self.smtp_obj.login(account, passwd)

    def send(self, frm, to, subject, content):
        self.smtp_obj.sendmail(frm, to, subject + '\n' + content)

    def quit(self):
        self.smtp_obj.quit()
