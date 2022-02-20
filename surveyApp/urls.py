from django.urls import path
from . import views

urlpatterns = [
    path('survey/', views.CreateSurvey, name='create-survey'),
    path('question/', views.CreateQuestion, name='create-question'),
    path('option/', views.CreateOption, name='create-option'),
    path('answer/', views.CreateAnswer, name='create-answer'),
    path('survey-details/<int:survey_id>', views.SurveyDetails, name="survey-details")
]