from django.shortcuts import render
from django.http import Http404
from . models import Survey, Question, Option, Answer
from . serializers import SurveySerializer, QuestionSerializer, OptionSerializer, AnswerSerializer, SurveyDetailSerializer
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import APIView
from rest_framework import generics
from rest_framework import mixins
from rest_framework.authentication import SessionAuthentication, BasicAuthentication, TokenAuthentication
from rest_framework.permissions import IsAuthenticated

# Create your views here.

class SurveyList(generics.GenericAPIView, mixins.ListModelMixin, mixins.CreateModelMixin):
    serializer_class = SurveySerializer
    queryset = Survey.objects.all()
    # authentication_classes = [SessionAuthentication, BasicAuthentication]
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]

    def get(self, request):
        return self.list(request)
    
    def post(self, request):
        return self.create(request)


class QuestionList(generics.GenericAPIView, mixins.ListModelMixin, mixins.CreateModelMixin):
    serializer_class = QuestionSerializer
    queryset = Question.objects.all()
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]

    def get(self, request):
        return self.list(request)
    
    def post(self, request):
        return self.create(request)


class OptionList(generics.GenericAPIView, mixins.ListModelMixin, mixins.CreateModelMixin):
    serializer_class = OptionSerializer
    queryset = Option.objects.all()
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]

    def get(self, request):
        return self.list(request)
    
    def post(self, request):
        return self.create(request)


class AnswerList(generics.GenericAPIView, mixins.ListModelMixin, mixins.CreateModelMixin):
    serializer_class = AnswerSerializer
    queryset = Answer.objects.all()
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]

    def get(self, request):
        return self.list(request)
    
    def post(self, request):
        return self.create(request)


# class SurveyDetails(generics.GenericAPIView, mixins.RetrieveModelMixin):
#     serializer_class = SurveyDetailSerializer
#     queryset = Survey.objects.all()
#     lookup_field = ['id']

#     def get(self, request):
#         return self.retrieve(request)


class SurveyDetails(APIView):
    authentication_classes = [SessionAuthentication, BasicAuthentication]
    permission_classes = [IsAuthenticated]
    
    def get_object(self, survey_id):
        try:
            return Survey.objects.get(pk = survey_id)
        except Survey.DoesNotExist:
            raise Http404
    
    def get(self, request, survey_id):
        survey = self.get_object(survey_id)
        serializer = SurveyDetailSerializer(survey)
        return Response(serializer.data)


# class SurveyList(APIView):
#     def get(self, request):
#         survey = Survey.objects.all()
#         serializer = SurveySerializer(survey, many=True)
#         return Response(serializer.data)
    
#     def post(self, request):
#         serializer = SurveySerializer(data = request.data)
        
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data, status=status.HTTP_201_CREATED)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
