import smtplib
from prot import Prot


class Smtp(Prot):

    def __init__(self, host='smtp.gmail.com', port=465):
        self.smtp_obj = smtplib.SMTP_SSL(host, port)


    def login(self, account, passwd):
        self.smtp_obj.login(account, passwd)

    def send(self, frm, to, subject, content):
        self.smtp_obj.sendmail(frm, to, 'Subject:' + subject + '\n' + content)

    def quit(self):
        self.smtp_obj.quit()
