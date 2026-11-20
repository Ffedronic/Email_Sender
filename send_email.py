import os
from dotenv import load_dotenv
import smtplib
import ssl
from email.message import EmailMessage

load_dotenv()

def send_email(content):
    content = content.decode("utf-8")

    host = "smtp.gmail.com"
    port = 465

    sender_email = str(os.getenv("SENDER_EMAIL"))
    password = str(os.getenv("APP_PASSWORD_SENDER"))

    message = EmailMessage()
    message["From"] = sender_email
    message["To"] = str(os.getenv("DESTINATION_EMAIL"))
    message["Subject"] = "Google News"
    message.set_content(content)

    context = ssl.create_default_context()

    with smtplib.SMTP_SSL(host, port, context=context) as server:
        server.login(sender_email, password)
        server.send_message(message)