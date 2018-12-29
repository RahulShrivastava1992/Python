from django.shortcuts import render
from django.http import HttpResponse

def home(request):
    return HttpResponse("Hello, Django! Rahul is here now to take care")
# Create your views here.
