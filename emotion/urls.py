from django.urls import path
from . import views

app_name = 'emotion'

urlpatterns = [
    path('', views.emotion_analysis, name="emotion_anaylsis"),
    path(r'^type/$', views.emotion_analysis_type, name="emotion_analysis_type"),
    path(r'^import/$', views.emotion_analysis_import, name="emotion_analysis_import"),
]