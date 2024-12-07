from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),  # Index page (optional)
    path('stations/', views.stations_list, name='stations_list'),
    path('add_station/', views.add_station, name='add_station'),
]


# charging/urls.py

from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('stations/', views.stations_list, name='stations_list'),
    path('add_station/', views.add_station, name='add_station'),
    path('register/', views.register, name='register'),  # Registration URL
]

from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),  # Maps the root URL to the index view
]

from django.urls import path
from . import views

urlpatterns = [
    path('stations/', views.stations_list, name='stations_list'),
]
