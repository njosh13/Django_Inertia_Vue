from django.contrib import admin
from django.urls import path
from . import views

app_name = "home"

urlpatterns = [
    path('', views.home, name='home'),
    path('events', views.events, name='events'),
    path('events/<int:id>', views.single_event, name='single_event'),


]
