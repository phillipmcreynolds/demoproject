from django.shortcuts import render
from demoapp.forms import BookingForm


# Create your views here.
from django.http import HttpResponse 
def index(request): 
    render(request, 'index.html')

def home(request):
    return render(request, 'index.html')

def menu(request):
    return render(request, 'menu.html')
    
def about(request):
    return render(request, 'about.html')

def book(request):
    return render(request, 'book.html')

def form_view(request):
    form = BookingForm()
    if request.method == 'POST':
        form = BookingForm(request.POST)
        if form.is_valid():
            form.save()
    context = {"form" : form}
    return render(request, "booking.html", context)