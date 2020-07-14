from django.urls import path
from news import views

urlpatterns = [
    path('', views.news_detail , name = 'news_detail'),
]
