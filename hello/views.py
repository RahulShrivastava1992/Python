from django.shortcuts import render
from django.http import HttpResponse
import re
from datetime import datetime

def home(request):
    return HttpResponse("Hello, Django! Rahul is here now to take care")
def hello_there(request, name):
    return render(
        request,
        'hello/hello_there.html',
        {
            'name': name,
            'date': datetime.now()
        }
    )
def ChatBots(request, name):
    return render(
        request,
        'hello/ChatBots.html',
        {
            'name': name,
            'date': datetime.now()
        }
    )
# Create your views here.