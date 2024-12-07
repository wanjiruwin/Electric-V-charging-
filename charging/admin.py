from django.contrib import admin

# Register your models here.
# charging/admin.py

from django.contrib import admin
from .models import ChargingStation  # Assuming you have a model for charging stations

# Register your models here
admin.site.register(ChargingStation)
