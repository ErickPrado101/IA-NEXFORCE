# mailer/views.py
from rest_framework import viewsets
from rest_framework.response import Response
from .models import Email
from .serializers import EmailSerializer
import smtplib

class EmailViewSet(viewsets.ModelViewSet):
    queryset = Email.objects.all()
    serializer_class = EmailSerializer

    def perform_create(self, serializer):
        email = serializer.save()
        self.send_email(email)

    def send_email(self, email):
        subject = email.subject
        message = email.message
        recipient = [email.recipient]

        try:

            smtp_server = 'your_smtp_server.com'
            smtp_port = 587
            smtp_username = 'your_username'
            smtp_password = 'your_password'


            server = smtplib.SMTP(smtp_server, smtp_port)
            server.starttls()


            server.login(smtp_username, smtp_password)


            email_message = f"Subject: {subject}\n\n{message}"


            server.sendmail(smtp_username, recipient, email_message)


            server.quit()

            email.sent = True
            email.save()
        except Exception as e:
            print(str(e))
