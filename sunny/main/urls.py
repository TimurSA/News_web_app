
from django.urls import path
from . import views  # импорт с той же папки

urlpatterns = [
    path('', views.index, name='home'),  # без круглых скобочек, тк мы просто хотим обратиться к нему без выполнения метода
    path('about', views.about, name='about')
]
