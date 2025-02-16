from django.shortcuts import render
from django.http import HttpResponse

def home(request):
    path = request.path
    content = "<html><body><h1>welcome</h1></body></html>"
    return HttpResponse(str(path))