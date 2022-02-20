from rest_framework import serializers
from . models import Survey, Question

class SurveySerializer(serializers.ModelSerializer):
    class Meta:
        model = Survey
        fields = ['title']

class QuestionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Question
        fields = ['question', 'survey_id']