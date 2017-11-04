from django.shortcuts import render

# Create your views here.
from django.http import JsonResponse
from events.models import Event
from events.serializers import EventSerializer


def event_list(request):
    all_events = Event.objects.select_related('place').all()
    print(all_events)
    print(EventSerializer.serialize('json', list(all_events)))
    # for e in all_events:
    # print(serializers.serialize('json', e))
    return JsonResponse({'data': 'WIP'})
