from inertia import render
from .models import Event


def index(request):
  return render(request, 'Events/Index', props={
    'events': Event.objects.all()
  })
