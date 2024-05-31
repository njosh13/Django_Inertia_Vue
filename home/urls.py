from django.contrib import admin
from django.urls import path
from . import views

app_name = "home"

urlpatterns = [
    path('', views.home, name='home'),
    path('events', views.events, name='events'),
    path('events/<int:id>', views.single_event, name='single_event'),
    path('events/create', views.create_event, name='create_event'),
    path('events/<int:id>/edit', views.edit_event, name='edit_event'),



]
