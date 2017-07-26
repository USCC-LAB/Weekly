import smtplib

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

<<<<<<< HEAD
    def send(self, frm, to, subject, content):
        self.smtp_obj.sendmail(frm, to, 'Subject:' + subject + '\n' + content)
=======
    def send(self, frm, to, subject, content, *attachments):
        # render msg
        msg = MIMEMultipart()
        msg['Subject'] = subject
        msg['To'] = ', '.join(to)
        msg['Date'] = str(date.today())
        msg['From'] = frm
        msg.attach(MIMEText(content))

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
        try:
            self.smtp_obj.sendmail(frm, to, msg.as_string())
            print ('Send email success.')
        except:
            print ('Send email Error: ', sys.exc_info()[0])

<<<<<<< HEAD
    def send_with_attachment(self, frm, to, subject, content, attachments):
        # render msg
        msg = MIMEMultipart()
        msg['Subject'] = subject
        msg['To'] = ', '.join(to)
        msg['Date'] = str(date.today())
        msg['From'] = frm
        msg.attach(MIMEText(content))

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
        try:
            self.smtp_obj.sendmail(frm, to, msg.as_string())
            print ('Send email with attachment success.')
        except:
            print ('Send with attachment Error: ', sys.exc_info()[0])
>>>>>>> d3c9f75... Simplify send function and delete duplicate code

=======
>>>>>>> e7dcf6e... Simplify send function and delete duplicate code
    def quit(self):
        self.smtp_obj.quit()
