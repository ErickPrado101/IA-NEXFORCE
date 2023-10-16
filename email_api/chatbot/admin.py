from django.contrib import admin
from .models import ChatbotQuestion

class ChatbotQuestionAdmin(admin.ModelAdmin):
    list_display = ('question', 'timestamp')
    search_fields = ('question',)

admin.site.register(ChatbotQuestion, ChatbotQuestionAdmin)

