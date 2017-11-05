from django.http import JsonResponse
from events.models import Event


def event_list(request):
    all_events = Event.objects.select_related('place').order_by('start_time').values()
    # s = EventSerializer(all_events, many=True)
    return JsonResponse(list(all_events), safe=False)
