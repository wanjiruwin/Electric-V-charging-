from django.contrib.auth import login
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from .models import ChargingStation
from .forms import ChargingStationForm, UserRegistrationForm

def home(request):
    """Homepage view"""
    return render(request, 'home.html')

def station_list(request):
    """List all charging stations"""
    stations = ChargingStation.objects.all()
    return render(request, 'station_list.html', {'stations': stations})

def station_detail(request, pk):
    """Detail view for a specific charging station"""
    station = get_object_or_404(ChargingStation, pk=pk)
    return render(request, 'station_detail.html', {'station': station})

def station_create(request):
    """Create a new charging station"""
    if request.method == 'POST':
        form = ChargingStationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Charging station created successfully!')
            return redirect('station_list')
    else:
        form = ChargingStationForm()
    return render(request, 'station_form.html', {'form': form})

def station_update(request, pk):
    """Update an existing charging station"""
    station = get_object_or_404(ChargingStation, pk=pk)
    if request.method == 'POST':
        form = ChargingStationForm(request.POST, instance=station)
        if form.is_valid():
            form.save()
            messages.success(request, 'Charging station updated successfully!')
            return redirect('station_list')
    else:
        form = ChargingStationForm(instance=station)
    return render(request, 'station_form.html', {'form': form})

def station_delete(request, pk):
    """Delete a charging station"""
    station = get_object_or_404(ChargingStation, pk=pk)
    if request.method == 'POST':
        station.delete()
        messages.success(request, 'Charging station deleted successfully!')
        return redirect('station_list')
    return render(request, 'station_confirm_delete.html', {'station': station})

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
