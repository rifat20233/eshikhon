from django.shortcuts import render
from django.http import HttpResponse
from datetime import datetime

# Create your views here.


def index (request):
    value=datetime.now()

    return HttpResponse("<h2>Hello from django: {}</h2>".format(value))