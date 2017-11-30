import smtplib
from email.mime.text import MIMEText   
from email.header import Header
import os

class exmail(object):

    def __init__(self, host, username, password):
        self.host = host
        self.username = username
        self.password = password
        self.smtp = smtplib.SMTP()  

    def connect(self):
        self.smtp.connect(self.host)

    def send(self, content, subject, sender, receivers):
        self.connect()
        self.login()

        msg = MIMEText(content, _subtype='plain',_charset='utf-8')
        msg['From'] = sender
        msg['To'] = ";".join(receivers)

        self.smtp.sendmail(sender, receivers, msg.as_string())
        self.smtp.quit()
        
    def login(self):
        try:
            self.smtp.login(username, password)
        except Exception as e:
            print e.args
        

if __name__=='__main__':
    subject = "subject"
    content = "test"
    sender = '13260071987@163.com'
    receivers = ['467754239@qq.com']

    mail = exmail('smtp.163.com', '13260071987@163.com', 'zhengyscn123456')
    mail.send(content, subject, sender, receivers)
