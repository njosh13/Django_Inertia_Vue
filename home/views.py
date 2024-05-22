from inertia import render
from .models import Event


def home(request):

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
