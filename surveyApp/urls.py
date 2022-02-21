from django.urls import path
from . import views

urlpatterns = [
    path('generic/survey/', views.SurveyList.as_view(), name='survey'),
    path('generic/question/', views.QuestionList.as_view(), name='question'),
    path('generic/option/', views.OptionList.as_view(), name='option'),
    path('generic/answer/', views.AnswerList.as_view(), name='answer'),
    # path('generic/survey/<int:id>/', views.SurveyDetails.as_view(), name="survey-details"),
    path('survey-details/<int:survey_id>', views.SurveyDetails.as_view(), name="survey-details"),
]