import sys
from mail import mail
from mail.smtp import smtp

if __name__ == '__main__':
    acnt = sys.argv[1]
    pswd = sys.argv[2]

    frm = acnt
    to = acnt

    Mail = mail.mail(smtp.smtp)

    Mail.login(acnt, pswd)

    Mail.send(frm, to, 'Dummy mail from USCC LAB', 'Hello members : )')

    Mail.quit()
