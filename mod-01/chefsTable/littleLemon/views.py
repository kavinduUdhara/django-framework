from django.shortcuts import render
from django.http import HttpResponse

def home(request):
    return HttpResponse("hello world")

def menuList(request):
    return HttpResponse("this is menu list")