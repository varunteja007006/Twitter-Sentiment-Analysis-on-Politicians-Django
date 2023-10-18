from django.urls import path
from . import views

app_name = 'sentiment'

urlpatterns = [
    path('', views.sentiment_analysis, name="sentiment_anaylsis"),
    path('type', views.sentiment_analysis_type, name="sentiment_analysis_type"),
    path('import', views.sentiment_analysis_import, name="sentiment_analysis_import"),
]