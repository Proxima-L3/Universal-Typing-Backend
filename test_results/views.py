from django.shortcuts import render
from django.http import HttpResponse
from django.views import View
from rest_framework import viewsets
from .serializers import TestResultsSerializer
from .models import TestResults

# note: views are functions or class object methods that take in http requests as parameters and return http responses



# 
class TestResultsViewSet(viewsets.ModelViewSet):

    # assigning test results translation process (between JSON and django model instances) to serializer class TestResultsSerializer
    serializer_instance = TestResultsSerializer

    # variable populated with ALL test results entry rows of sql table
    queryset = TestResults.objects.all()


# Handles public leaderboard get/put/push/post requests
# class PublicLeaderboards(View):
    
#     def get(self, request) -> HttpResponse:
#         return HttpResponse('im in the get method in PublicLeaderboards class in leaderboards django app')


# # Handles public leaderboard get/put/push/post requests
# class PrivateLeaderboard(View):

#     def get(self, request) -> HttpResponse:
#         return HttpResponse('im in the get method in PrivateLeaderboard class in leaderboards django app')


