from django.urls import path
from . import views

urlpatterns = [
    path('survey/', views.SurveyList.as_view(), name='create-survey'),
    path('question/', views.QuestionList.as_view(), name='create-question'),
    path('option/', views.OptionList.as_view(), name='create-option'),
    path('answer/', views.AnswerList.as_view(), name='create-answer'),
    path('survey-details/<int:survey_id>', views.SurveyDetails.as_view(), name="survey-details")
]