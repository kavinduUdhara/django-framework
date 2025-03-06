from django.shortcuts import render
from django.http import HttpResponse

def home(request):
    path = request.path
    schema = request.scheme
    method = request.method
    address = request.META['REMOTE_ADDR']
    user_agent = request.META['REMOTE_ADDR']
    content = f"""
        <br>path: {path}
        <br>scheme: {schema}
        <br>method: {method}
        <br>address: {address}
        <br>user_agent: {user_agent}
"""
    return HttpResponse(content)