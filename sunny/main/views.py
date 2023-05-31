from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

# Отвечает за те методы, которые будут вызваны при переходе пользователем на какую-либо определенную страницу


def index(request):
    data = {
        'title': 'Главная страница',
        'values': ['Some', 'Hello', '123'],
        'obj': {
            'car': 'BMW',
            'age': 18,
            'hobby': 'Football',
        },
    }
    return render(request, "main/index.html", data)  # Всегда передавать словари


def about(request):
    return render(request, "main/about.html")


