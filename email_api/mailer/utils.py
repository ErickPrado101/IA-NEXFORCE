import smtplib
from email.mime.text import MIMEText
from django.core.mail import send_mail
from .models import Email

def send_email(email):
    subject = email.subject
    message = email.message
    recipient = [email.recipient]

    try:
        send_mail(subject, message, 'your_email@gmail.com', recipient)
        email.sent = True
        email.save()
    except Exception as e:
        print(str(e))