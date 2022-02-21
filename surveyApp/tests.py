import json

from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase

from .models import Survey
from .serializers import SurveySerializer


class SurveyTest(APITestCase):
    list_url = reverse("survey-list")

    def test_survey_list_autheticated(self):
        response = self.client.get(user=None)
        self.assertEqueal()