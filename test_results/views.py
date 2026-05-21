from django.shortcuts import render
from django.http import HttpResponse
from django.views import View
from rest_framework import viewsets
from .serializers import TestResultsSerializer
from .models import TestResults

# note: views are functions or class object methods that take in http requests as parameters and return http responses



# 
class TestResultsView(viewsets.ModelViewSet):

    # assigning test results serializer class to serializer_class
    serializer_class = TestResultsSerializer

    # variable populated with all test results entries
    queryset = TestResults.objects.all()


# Handles public leaderboard get/put/push/post requests
# class PublicLeaderboards(View):
    
#     def get(self, request) -> HttpResponse:
#         return HttpResponse('im in the get method in PublicLeaderboards class in leaderboards django app')


# # Handles public leaderboard get/put/push/post requests
# class PrivateLeaderboard(View):

#     def get(self, request) -> HttpResponse:
#         return HttpResponse('im in the get method in PrivateLeaderboard class in leaderboards django app')


