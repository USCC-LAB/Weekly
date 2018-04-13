import smtplib
import os
import sys
from email import encoders
from email.mime.base import MIMEBase
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from datetime import date


class Smtp:
    def __init__(self, *argv):
        # Declaration
        self.__smtp_obj = None

        # Initialization
        if () != argv:
            self.__smtp_obj = smtplib.SMTP_SSL(*argv)
        else:
            self.__smtp_obj = self.default_setup()

    # Set Gmail server as default
    def default_setup(self):
        return smtplib.SMTP_SSL('smtp.gmail.com', 465)

    def login(self, account, passwd):
        self.__smtp_obj.login(account, passwd)

    def send(self, frm, to, subject, content, attachments):
        '''
        @frm str
        @to list of email. e.g. ['abc@gmail.com', 'def@gmail.com']
        @subject str
        @content str
        @attachments None or list of file path. e.g. ['filePath1', 'filePath2'] 
        '''
        msg = MIMEMultipart()
        msg['From'] = frm
        msg['To'] = ', '.join(to)
        msg['Subject'] = subject
        msg['Date'] = str(date.today())
        msg.attach(MIMEText(content))

        for filePath in attachments:
            try:
                with open(filePath, 'rb') as fp:
                    file = MIMEBase('application', 'octet-stream')
                    file.set_payload(fp.read())
                
                encoders.encode_base64(file)
                file.add_header('Content-Disposition', 'attachment',
                filename=os.path.basename(filePath))
                msg.attach(file)
            except:
                print('Unable to open one of attachments. Error: ', sys.exc_info()[0])
        
        try:
            self.__smtp_obj.sendmail(frm, to, msg.as_string())
            print('Send email with attachment success.')
        except expression as identifier:
            print('Send with attatchment Error: ', sys.exc_info()[0])

    def quit(self):
        self.__smtp_obj.quit()
