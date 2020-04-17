
## TODO:
# Test with python3 container
# docker run --rm -it -v ~/Desktop/mail.py:/tmp/mail.py python:3.8.2-alpine python3 /tmp/mail.py
#
# Test with two-factor authentication enabled
#

from os import getenv
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.application import MIMEApplication
import argparse

def send_email( subj, body ):
    smtp_host = getenv('SMTP_HOST')
    smtp_port = getenv('SMTP_PORT')
    smtp_user = getenv('SMTP_USER')
    smtp_pass = getenv('SMTP_PASS')
    mail_to = getenv('MAIL_TO')
    mail_from = smtp_user

    print("Mail subject: " + subj)
    print("Mail body: " + body)

    msg = MIMEText(body)
    msg['Subject'] = subj
    msg['From'] = mail_from
    msg['To'] = mail_to

    print("Sending email...")
    server = smtplib.SMTP(smtp_host, smtp_port)
    server.starttls()
    server.login(smtp_user, smtp_pass)
    server.sendmail(mail_from, mail_to, msg.as_string())
    server.quit()

def main():
    parser = argparse.ArgumentParser(description='Send email')
    # Add the arguments
    parser.add_argument('--subject','-s', action="store", dest="mail_subject")
    parser.add_argument('--body','-b', action="store", dest="mail_body")
    args = parser.parse_args()
    print("Mail subject: " + args.mail_subject)
    print("Mail body: " + args.mail_body)
    send_email(args.mail_subject, args.mail_body)

if __name__ == "__main__":
    main()
