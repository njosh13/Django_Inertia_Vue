from inertia import render
from .models import Event
from inertia import share
from django.shortcuts import redirect
from .forms import EventForm
from .serializers import EventSchema
import json
from django.core.exceptions import ValidationError


def home(request):

    share(request, success="Home Page")
    return render(request, 'Home/Index')


def events(request):

    events = Event.objects.all()

    return render(request, 'Events/Index', props={
        'events': events
    })


def single_event(request, id):

    event = Event.objects.get(id=id)

    return render(request, 'Events/Show', props={
        'event': event
    })


def create_event(request):

    if request.method == "POST":
        data = json.loads(request.body.decode('utf-8'))
        event_form = EventForm(data)

        if event_form.is_valid():
            event_form.save()
            return redirect('home:events')
        else:
            return render(request, 'Events/CreateAndEdit', {
                'errors': event_form.errors,
            })

    return render(request, "Events/CreateAndEdit", {})


def edit_event(request, id):

    event = Event.objects.get(id=id)

    props = {'event': event}

    if request.method == "POST":
        data = json.loads(request.body.decode('utf-8'))
        event_form = EventForm(data, instance=event)

        if event_form.is_valid():
            event_form.save()
            return redirect('home:events')
        else:
            return render(request, 'Events/CreateAndEdit', {
                'errors': event_form.errors,
            })
    return render(request, "Events/CreateAndEdit", props)
