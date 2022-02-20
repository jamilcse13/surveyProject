from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from . models import Survey

# Create your views here.
@csrf_exempt
def CreateSurvey(request):
    if request.method == 'POST':
        title = request.POST['title']
        survey = Survey.objects.create(title=title)
        survey.save()
        message = f"OKAY, got and saved user {title}"
    elif request.method == 'GET':
        message = "Use POST method"
    
    mydictionary = {
        "message" : message
    }
    return JsonResponse(mydictionary)
