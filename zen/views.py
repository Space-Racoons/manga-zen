from django.shortcuts import render
from django.http import HttpResponse

def home(request):
    return HttpResponse("This is supposed to be the home page :)")
