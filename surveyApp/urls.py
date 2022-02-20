from django.urls import path
from . import views

urlpatterns = [
    path('survey/', views.CreateSurvey, name='create-survey'),
    # path('create-question/', views.CreateQuestion, name='create-question'),
]