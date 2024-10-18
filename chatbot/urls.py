# chatbot/urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('message/', views.ask_question, name='ask_question'),  # Ruta para interactuar con el chatbot
]
