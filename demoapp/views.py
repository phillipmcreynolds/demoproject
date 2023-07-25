from django.shortcuts import render
from demoapp.forms import BookingForm


# Create your views here.
from django.http import HttpResponse 
def index(request): 
    return HttpResponse("Hello, world. This is the index view of Demoapp.")

def home(request):
    path = request.path
    user = request.user
    string_response = "Hello: " + str(path) + str(user)
    response = HttpResponse(string_response)
    return response

def about(request):
    context = {'about': 'Additional information'}
    return render(request, "about.html", context)

def menu(request):
    path = request.path
    response = HttpResponse("Menu")
    return response

def book(request):
    path = request.path
    response = HttpResponse("Make a booking")
    return response

def form_view(request):
    form = BookingForm()
    if request.method == 'POST':
        form = BookingForm(request.POST)
        if form.is_valid():
            form.save()
    context = {"form" : form}
    return render(request, "booking.html", context)