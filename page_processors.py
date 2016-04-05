__author__ = 'Dominic Fitzgerald'
from mezzanine.pages.page_processors import processor_for

from models import HomePage, Event, EventsPage
from datetime import datetime


@processor_for(HomePage)
def home(request, page):
    next_event = Event.objects.filter(time__gt=datetime.now())
    if next_event:
        next_event = next_event.earliest(field_name='time')
    return {'next_event': next_event}


@processor_for(EventsPage)
def events(request, page):
    all_events = Event.objects.filter(time__gt=datetime.now())
    return {'events': all_events}
