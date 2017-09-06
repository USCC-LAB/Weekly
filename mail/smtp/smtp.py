import smtplib


class Smtp:

    def __init__(self, *argv):
        if () != argv:
            self.smtp_obj = smtplib.SMTP_SSL(*argv)
        else:
            # Set Gmail server as default
            self.smtp_obj = smtplib.SMTP_SSL('smtp.gmail.com', 465)

    def login(self, account, passwd):
        """
        You need login by gmail account.
        """
        self.smtp_obj.login(account, passwd)

    def send(self, frm, to, content):
        """
        <to> must be a list
        """
        self.smtp_obj.sendmail(frm, to, content)

    def quit(self):
        """
        Terminate the <smtp_obj> session
        """
        self.smtp_obj.quit()
