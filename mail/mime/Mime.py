import os
import sys
from email import encoders
from email.mime.base import MIMEBase
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from datetime import date


class Mime:

    msg = ""

    def __init__(self, *argv):
        self.msg = MIMEMultipart()

    def format_msg(self, frm, to, subject, content, attachments):
        self.msg['Subject'] = subject
        self.msg['To'] = ', '.join(to)
        self.msg['Date'] = str(date.today())
        self.msg['From'] = frm
        self.msg.attach(MIMEText(content))
        self.append_attachments(attachments)

        return self.msg.as_string()

    def append_attachments(self, attachments):
        for attachment in attachments:
            try:
                with open(attachment, 'rb') as fr:
                    file = MIMEBase('application', "octet-stream")
                    file.set_payload(fr.read())
                encoders.encode_base64(file)
                file.add_header('Content-Disposition', 'attachment',
                                filename=os.path.basename(attachment))
                self.msg.attach(file)
            except:
                print("Unable to open one of the attachments. Error: ",
                      sys.exc_info()[0])
                raise

    def get_msg(self):
        return self.msg.as_string()
