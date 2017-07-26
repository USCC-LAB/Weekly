from mail import mail
from mail.smtp import smtp

def smtp_dummy(acnt, pswd, attachments):
    frm = acnt
    to = [acnt]

    myMail = mail.mail(smtp.smtp)

    myMail.login(acnt, pswd)
    myMail.send(frm, to, 'Dummy mail from USCC LAB', 'Hello members : )', attachments)
    
    myMail.quit()

    return 0
