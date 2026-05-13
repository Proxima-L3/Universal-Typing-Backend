from django.shortcuts import render
from django.http import HttpResponse
from django.views import View

# note: views are functions or class object methods that take in http requests as parameters and return http responses

# Create your views here.


# Handles login request
class LoginAuthentication(View):

    # below not needed for django view classes (init defined in inherited View class)

    # def __init__(self) -> None:
    #     self.fillerVars = ''
    
    def get(self, request) -> HttpResponse:
        return HttpResponse('im in the get method in LoginAuthentication class in authentication django app')
    
    # def response(self, request) -> HttpResponse:
    #     return HttpResponse('temp filler string')

