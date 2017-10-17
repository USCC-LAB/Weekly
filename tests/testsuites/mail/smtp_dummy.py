from mail import mail
from mail.prot import smtp


def smtp_dummy(acnt, pswd):
    frm = acnt
    to = acnt

    Mail = mail.Mail(smtp.Smtp)

    Mail.login(acnt, pswd)

    Mail.send(frm, to, 'Dummy mail from USCC LAB', 'Hello members : )')

    Mail.quit()

    return 0
