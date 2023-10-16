from django.db import models

class ChatbotQuestion(models.Model):
    question = models.TextField()
    timestamp = models.DateTimeField(auto_now_add=True)
