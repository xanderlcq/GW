__author__ = 'x'
import smtplib
import time


class Emailer(object):
    # @ tmomail.net
    # @ mms.att.net
    def __init__(self):
        self.username = 'deerfieldnoteworthy@gmail.com'
        self.password = 'deerfieldnoteworthy123'

    def send_email(self,email_subject,body_of_email,recipient):
        session = smtplib.SMTP('smtp.gmail.com', 587)
        session.ehlo()
        session.starttls()
        session.login(self.username, self.password)
        headers = "\r\n".join(["from: " + self.username,
                               "subject: " + email_subject,
                               "to: " + recipient,
                               "mime-version: 1.0",
                               "content-type: text/html"])

        # body_of_email can be plaintext or html!
        content = headers + "\r\n\r\n" + body_of_email
        session.sendmail(self.username, recipient, content)
        session.close()
        print 'sent'

    def generate_data_email(self,data):
        assert data.is_valid(),AssertionError
        current_time = time.asctime(time.localtime())
        header = """<html><head><title></title></head><body ginger_software_doc="true"
         ginger_software_stylesheet="true"><p>The time right now is: """+current_time+"""."""
        footer = """</body></html>"""
        body = """"""
        for key in data.get_data_keys():
            print key
            value = data.get_value(key)
            print value
            body = body + """<p>Current """+key+""" is: """+value+""".</p>"""
        msg = header+body+footer
        return msg
