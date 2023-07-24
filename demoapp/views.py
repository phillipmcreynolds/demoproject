from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse 
def index(request): 
    return HttpResponse("Hello, world. This is the index view of Demoapp.")

def home(request):
    path = request.path
    response = HttpResponse("This works")
    return response

def about(request):
    path = request.path
    response = HttpResponse("About us")
    return response

def menu(request):
    path = request.path
    response = HttpResponse("Menu")
    return response

def book(request):
    path = request.path
    response = HttpResponse("Make a booking")
    return response