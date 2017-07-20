from mail import mail
from mail.smtp import smtp

def smtp_dummy(acnt, pswd):
    frm = acnt
    to = acnt
    
    Mail = mail.mail(smtp.smtp)
    
    Mail.login(acnt, pswd)
    
    Mail.send(frm, to, 'Dummy mail from USCC LAB', 'Hello members : )')
    
    Mail.quit()

    return 0
