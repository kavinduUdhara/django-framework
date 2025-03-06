from django.shortcuts import render
from django.http import HttpResponse

def home(request):
    return HttpResponse("hello world")

def menuList(request):
    return HttpResponse("this is menu list")

def pathview(request, name, id):
    return HttpResponse(f"Hola {name}, Tu id es {id}")

def qryview(request):
    if request.method == "GET":
        name = request.GET['name']
        id = request.GET['id']
        return HttpResponse(f"Hola {name}, Tu id es {id}")

def formview(request):
    return HttpResponse("""
<form method="get" action="/getuserq" target="_blank">
                        {% csrf_token %} 
    <input name='name' type='text' placeholder='name'/>
    <input name='id' type='text' placeholder='id'/>
    <input type='submit'/>                  
</form>

""")