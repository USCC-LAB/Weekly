from mail.Mail import Mail
from mail.smtp.Smtp import Smtp
from mail.mime.Mime import Mime


def SmtpDummy(acnt, pswd, *attachments):
    _frm = acnt
    _to = [acnt]

    _mail = Mail(Smtp)
    _mail.login(acnt, pswd)
    _mail.send(_frm, _to, Mime().format_msg(
        _frm, _to, 'Dummy mail from USCC LAB', 'Hello members : )', attachments))
    _mail.quit()

    return 0
