from mail import mail
from mail.smtp import smtp

def smtp_dummy(acnt, pswd):
    frm = acnt
<<<<<<< HEAD
    to = acnt
    
    Mail = mail.mail(smtp.smtp)
    
    Mail.login(acnt, pswd)
    
    Mail.send(frm, to, 'Dummy mail from USCC LAB', 'Hello members : )')
    
    Mail.quit()
=======
    to = [acnt]

    myMail = mail.mail(smtp.smtp)

    myMail.login(acnt, pswd)
    myMail.send(frm, to, 'Dummy mail from USCC LAB', 'Hello members : )', attachments)
    
    myMail.quit()
>>>>>>> 289654f... Modify unittest function

    return 0
