from django.shortcuts import render
from django.http import JsonResponse
from events.models import Event
from events.serializers import EventSerializer


def event_list(request):
    all_events = Event.objects.select_related('place').all()
    s = EventSerializer(all_events, many=True)
    return JsonResponse(s.data, safe=False)
