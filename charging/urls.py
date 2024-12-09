
from django.urls import path
from . import views


urlpatterns = [
    path('', views.home, name='home'),
    path('stations/', views.station_list, name='station_list'),
    path('stations/new/', views.station_create, name='station_create'),
    path('stations/<int:pk>/', views.station_detail, name='station_detail'),
    path('stations/<int:pk>/edit/', views.station_update, name='station_update'),
    path('stations/<int:pk>/delete/', views.station_delete, name='station_delete'),
    path('register/', views.register, name='register'),  
]

