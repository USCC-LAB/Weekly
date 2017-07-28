import os
import sys
import smtplib
from email import encoders
from email.mime.base import MIMEBase
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from datetime import date

class smtp:
    # smtp_obj =

    def __init__(self, *argv):
        if () != argv:
            self.smtp_obj = smtplib.SMTP_SSL(*argv)
        else:
            self.smtp_obj = self.default_setup()

    # Set Gmail server as default
    def default_setup(self):
        return smtplib.SMTP_SSL('smtp.gmail.com', 465)

    def login(self, account, passwd):
        self.smtp_obj.login(account, passwd)

    def send(self, frm, to, subject, content, *attachments):
        msg = self.render_msg(frm, to, subject, content, attachments)
        self.smtp_obj.sendmail(frm, to, msg)

    def render_msg(self, frm, to, subject, content, attachments):
        msg = MIMEMultipart()
        msg['Subject'] = subject
        msg['To'] = ', '.join(to)
        msg['Date'] = str(date.today())
        msg['From'] = frm
        msg.attach(MIMEText(content))
        msg = self.append_attachments(msg, attachments)

        return msg.as_string()
        
    def append_attachments(self, msg, attachments):
        for attachment in attachments:
            try:
                with open(attachment, 'rb') as fp:
                    file = MIMEBase('application', "octet-stream")
                    file.set_payload(fp.read())
                encoders.encode_base64(file)
                file.add_header('Content-Disposition', 'attachment',
                filename=os.path.basename(attachment))
                msg.attach(file)
            except:
                print("Unable to open one of the attachments. Error: ", sys.exc_info()[0])
                raise
        
        return msg

    def quit(self):
        self.smtp_obj.quit()
