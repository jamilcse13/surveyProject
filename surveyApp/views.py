from django.shortcuts import render
from django.http import HttpResponse, JsonResponse

# Create your views here.
def Customer(request):
    mydictionary = {
        "name" : 'John Doe',
        "age" : 30
    }
    return JsonResponse(mydictionary)