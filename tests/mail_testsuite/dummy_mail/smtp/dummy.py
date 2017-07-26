from mail import mail
from mail.smtp import smtp

def smtp_dummy(acnt, pswd, attachments):
    frm = acnt
<<<<<<< HEAD
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
=======
    to = [acnt]

    myMail = mail.mail(smtp.smtp)

    myMail.login(acnt, pswd)
    myMail.send(frm, to, 'Dummy mail from USCC LAB', 'Hello members : )', attachments)
    
    myMail.quit()
>>>>>>> origin/dev

    return 0
