import csv
import smtplib
import ssl
from collections import namedtuple

from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart


Message = namedtuple('Message', 'subject message_html message_txt')
message_templates = dict()

message_templates["confirm"] = Message("{name}, WIETsourcing is asking you to confirm your email",
                                       "message_templates/confirm.html",
                                       "message_templates/confirm.txt")
port = 465


def send_confirmation_mail_to(receiver_email, receiver_name, code) -> None:
    sender_email = "loginfajnegoczlowieka@gmail.com"
    # password = input("Type your password and press enter: ")
    password = ****

    message_template = message_templates["confirm"]
    message = MIMEMultipart("alternative")
    file = open("WIET_sourcing/service/message_templates/confirm.txt")

    text = file.read()
    part1 = MIMEText(text, "plain")

    file = open("WIET_sourcing/service/message_templates/confirm.html")
    html = file.read()
    part2 = MIMEText(html, "html")

    message.attach(part1)
    message.attach(part2)

    message["Subject"] = 'WIETsourcing is asking you to confirm your email'
    message["From"] = sender_email
    message["To"] = sender_email

    context = ssl.create_default_context()

    message = message.as_string().format(name=receiver_name.strip().title(), code=code)
    with smtplib.SMTP_SSL("smtp.gmail.com", port, context=context) as server:
        server.login(sender_email, password)
        server.sendmail(sender_email, receiver_email, message)

