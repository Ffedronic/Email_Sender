import smtplib
import ssl
from email.message import EmailMessage

def send_email(content):
    content = content.decode("utf-8")

    host = "smtp.gmail.com"
    port = 465

    sender_email = "fedronicfelix.dev@gmail.com"
    password = "djqgupwnglhjauvq"

    message = EmailMessage()
    message["From"] = sender_email
    message["To"] = "fedronicfelix@gmail.com"
    message["Subject"] = "Google News"
    message.set_content(content)

    context = ssl.create_default_context()

    with smtplib.SMTP_SSL(host, port, context=context) as server:
        server.login(sender_email, password)
        server.send_message(message)