from django.urls import path
from . import views

urlpatterns = [
    path('ask/', views.ask_question, name='chatbot'),
    path('', views.home, name='home'),
]
