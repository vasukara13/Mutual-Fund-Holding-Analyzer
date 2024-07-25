import date


#  https://realpython.com/python-send-email/


import smtplib
from email.mime.text import MIMEText

def send_email():
    email_user = 'your_email@gmail.com'
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.login(email_user, 'your_password')

    subject = 'Automated Email'
    text = 'Hello, this is an automated email!'
    msg = MIMEText(text)
    msg['Subject'] = subject

    to = ['recipient1@example.com', 'recipient2@example.com']
    server.sendmail(from_addr=email_user, to_addrs=to, msg=msg.as_string())

    server.quit()

send_email()