from django.urls import path
from . import views
urlpatterns = [
    path('', views.home, name='home'),
    path('quiz', views.quiz, name='quiz'),
    path('century_score', views.century_answers, name='century_answers'),
]