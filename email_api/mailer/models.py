from django.db import models

class Email(models.Model):
    subject = models.CharField(max_length=200)
    message = models.TextField()
    recipient = models.EmailField()
    sent = models.BooleanField(default=False)
