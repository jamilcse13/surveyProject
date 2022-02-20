from django.urls import path
from . import views

urlpatterns = [
    path('create-survey/', views.CreateSurvey, name='create-survey'),
]