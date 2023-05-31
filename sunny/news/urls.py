from django.urls import path
from . import views  # импорт с той же папки

urlpatterns = [
    path('', views.news_home, name='news_home'),  # без круглых скобочек, тк мы просто хотим обратиться к нему без выполнения метода
    path('create', views.create, name='create'),
    path('<int:pk>', views.NewsDetailView.as_view(), name='news-detail'),  # отслеживаем динамический параметр через <>, потом тип названия стр (!!!Никаких пробелов)
    path('<int:pk>/update',views.NewsUpdateView.as_view(), name='news-update'),
    path('<int:pk>/delete',views.NewsDeleteView.as_view(), name='news-delete'),
]
