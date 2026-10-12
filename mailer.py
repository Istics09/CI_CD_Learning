import os
import smtplib
import socket
from datetime import datetime
from email.message import EmailMessage

from dotenv import load_dotenv

load_dotenv()


def build_body(hostname, time):
    return f"Szia!\n\nEz a mail {hostname} ről jött\nAktuális idő: {time}"


def send_mail(body):
    msg = EmailMessage()
    msg["From"] = os.environ["SMTP_USER"]
    msg["To"] = os.environ["MAIL_TO"]
    msg["Subject"] = "CI/CD teszt üzenet"
    msg.set_content(body)

    with smtplib.SMTP_SSL(os.environ["SMTP_HOST"], int(os.environ["SMTP_PORT"])) as smtp:
        smtp.login(os.environ["SMTP_USER"], os.environ["SMTP_PASS"])
        smtp.send_message(msg)


if __name__ == "__main__":
    body = build_body(socket.gethostname(), datetime.now().strftime("%H:%M:%S"))
    send_mail(body)
    print("Mail elküldve")