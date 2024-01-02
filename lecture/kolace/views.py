from django.shortcuts import render
from django import http
from django.template import loader
from django.http import HttpResponse
# Create your views here.
def register_user(request):
    return http.HttpResponse("Hello, world. You're at the polls index.")

# def index(request):
#     return render(request,"templates/kolace/index.html")

def index(request):
   template = loader.get_template('kolace/index.html') # getting our template
   return HttpResponse(template.render())       # rendering the template in HttpResponse

def vajco(request):
    return http.HttpResponse("vajco")

def greet(request, name):
    return render(request,"kolace/greet.html",{
        "name":name.capitalize()
    })