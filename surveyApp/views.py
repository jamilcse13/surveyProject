from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from . models import Survey, Question
from . serializers import SurveySerializer

# Create your views here.
@csrf_exempt
def CreateSurvey(request):
    if request.method == 'GET':
        survey = Survey.objects.all()
        serializer = SurveySerializer(survey, many=True)
        return JsonResponse(serializer.data, safe=False)

    elif request.method == 'POST':
        data = JSONParser().parse(request)
        serializer = SurveySerializer(data = data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=201)
        return JsonResponse(serializer.errors, status=400)



# @csrf_exempt
# def CreateQuestion(request):
#     if request.method == 'POST':
#         question = request.POST['question']
#         survey_id = request.POST['survey-id']
#         # survey = get_object_or_404(Question, survey_id=survey_id)
#         survey = Question.objects.create(question=question, survey_id=survey_id)
#         survey.save()
#         message = "OKAY, got and saved your question"
#     elif request.method == 'GET':
#         message = "Use POST method"
    
#     mydictionary = {
#         "message" : message
#     }
#     return JsonResponse(mydictionary)