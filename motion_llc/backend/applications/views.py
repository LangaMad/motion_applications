from rest_framework import generics, viewsets, status
import requests
from.serializers import ProductSerializer
from django.http import HttpResponse

from .models import Product
from rest_framework.viewsets import GenericViewSet
import telebot

# Create your views here.
from .token import token
import requests
import telegram





class ApplicationAPIViewSets(viewsets.ModelViewSet):

    queryset = Product.objects.all()
    serializer_class = ProductSerializer

    def create(self, request, *args, **kwargs):
        response = super().create(request, *args, **kwargs)
        # Получение данных из запроса
        data = request.data

        # Формирование текста сообщения для отправки
        message_text = "Получена новая заявка:\n"
        for key, value in data.items():
            if key in ["name", "email", "number"]:
                message_text += f"{key}: {value}\n"

        # Отправка сообщения в Telegram
        chat_id = "-1001740033990"
        bot_token = token
        url = f"https://api.telegram.org/bot{bot_token}/sendMessage"
        payload = {"chat_id": chat_id, "text": message_text}
        requests.post(url, json=payload)

        return response