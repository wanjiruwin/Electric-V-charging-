from django import forms
from .models import ChargingStation
from django.contrib.auth.models import User

class UserRegistrationForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput, label="Password")
    confirm_password = forms.CharField(widget=forms.PasswordInput, label="Confirm Password")

    class Meta:
        model = User
        fields = ['username', 'email', 'password']

    def clean(self):
        cleaned_data = super().clean()
        password = cleaned_data.get("password")
        confirm_password = cleaned_data.get("confirm_password")

        if password != confirm_password:
            raise forms.ValidationError("Passwords do not match.")
        return cleaned_data

class ChargingStationForm(forms.ModelForm):
    class Meta:
        model = ChargingStation
        fields = [
            'name', 
            'address', 
            'latitude', 
            'longitude', 
            'total_charging_points', 
            'available_charging_points', 
            'is_operational', 
            'connector_type'
        ]
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control'}),
            'address': forms.TextInput(attrs={'class': 'form-control'}),
            'latitude': forms.NumberInput(attrs={'class': 'form-control'}),
            'longitude': forms.NumberInput(attrs={'class': 'form-control'}),
            'total_charging_points': forms.NumberInput(attrs={'class': 'form-control'}),
            'available_charging_points': forms.NumberInput(attrs={'class': 'form-control'}),
            'is_operational': forms.CheckboxInput(attrs={'class': 'form-check-input'}),
            'connector_type': forms.Select(attrs={'class': 'form-select'}),
        }