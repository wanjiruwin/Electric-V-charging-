from django.shortcuts import render

# Create your views here.
from django.shortcuts import render

def home(request):
    return render(request, 'charging/home.html')  # Render the homepage


# charging/views.py

from django.shortcuts import render, redirect
from .forms import UserRegistrationForm
from django.contrib.auth.models import User
from django.contrib.auth import login

def register(request):
    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.set_password(form.cleaned_data['password'])  # Hash the password
            user.save()
            login(request, user)  # Log the user in after registration
            return redirect('index')  # Redirect to the homepage after registration
    else:
        form = UserRegistrationForm()

    return render(request, 'register.html', {'form': form})


from django.shortcuts import render

def index(request):
    return render(request, 'index.html')  # Or another template of your choice

from django.shortcuts import render

def stations_list(request):
    # Dummy data for now
    stations = [
        {'name': 'Station A', 'location': 'City Center'},
        {'name': 'Station B', 'location': 'Highway Exit'},
        {'name': 'Station C', 'location': 'Suburban Area'},
    ]
    return render(request, 'stations_list.html', {'stations': stations})

from django.shortcuts import render, redirect
from django.http import HttpResponse
from .forms import StationForm

def add_station(request):
    if request.method == "POST":
        form = StationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('stations_list')  # Redirect to the stations list after adding a station
    else:
        form = StationForm()
    return render(request, 'add_station.html', {'form': form})

