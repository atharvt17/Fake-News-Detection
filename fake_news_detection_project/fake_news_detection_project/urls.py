# fake_news_detection_project/urls.py

from django.urls import path
from news_detection.views import analyze_article,index

urlpatterns = [
    path('', index, name='index'),
    path('analyze_article/', analyze_article, name='analyze_article'),
]
