from django.shortcuts import render
from django.http import HttpResponse

import sys
# Create your views here.

def home(request):
    return HttpResponse(sys.version)
