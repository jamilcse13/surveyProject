from django.shortcuts import render
from django.http import Http404
from . models import Survey, Question, Option, Answer
from . serializers import SurveySerializer, QuestionSerializer, OptionSerializer, AnswerSerializer, SurveyDetailSerializer
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import APIView

# Create your views here.

class SurveyList(APIView):
    def get(self, request):
        survey = Survey.objects.all()
        serializer = SurveySerializer(survey, many=True)
        return Response(serializer.data)
    
    def post(self, request):
        serializer = SurveySerializer(data = request.data)
        
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class QuestionList(APIView):
    def get(self, request):
        question = Question.objects.all()
        serializer = QuestionSerializer(question, many=True)
        return Response(serializer.data)
    
    def post(self, request):
        serializer = QuestionSerializer(data = request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class OptionList(APIView):
    def get(self, request):
        option = Option.objects.all()
        serializer = OptionSerializer(option, many=True)
        return Response(serializer.data)
    def post(self, request):
        serializer = OptionSerializer(data = request.data)
        
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class AnswerList(APIView):
    def get(self, request):
        answer = Answer.objects.all()
        serializer = AnswerSerializer(answer, many=True)
        return Response(serializer.data)
    
    def post(self, request):
        serializer = AnswerSerializer(data = request.data)
        
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class SurveyDetails(APIView):
    def get_object(self, survey_id):
        try:
            return Survey.objects.get(pk = survey_id)
        except Survey.DoesNotExist:
            raise Http404
    
    def get(self, request, survey_id):
        survey = self.get_object(survey_id)
        serializer = SurveyDetailSerializer(survey)
        return Response(serializer.data)
