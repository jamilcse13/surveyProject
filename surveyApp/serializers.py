from rest_framework import serializers
from . models import Survey, Question, Option, Answer

class SurveySerializer(serializers.ModelSerializer):
    class Meta:
        model = Survey
        fields = ['id', 'title']

class QuestionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Question
        fields = ['id', 'question', 'survey_id']


class OptionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Option
        fields = ['id', 'name', 'question_id']


class AnswerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Answer
        fields = ['id', 'option_id', 'question_id', 'customer_id']

class SurveyDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = Survey
        fields = ['id', 'title']