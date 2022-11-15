from django.urls import path
from . import views

app_name = 'sentiment_or_emotion'

urlpatterns = [
    path('', views.choose_sentiment_or_emotion, name="choose_sentiment_or_emotion"),
    path('Trending', views.trending, name="Trending"),
]