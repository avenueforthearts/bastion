from django.http import JsonResponse
from events.models import Event
from django.views.decorators.cache import cache_control


@cache_control(max_age=3600)
def event_list(request):
    all_events = Event.objects.select_related('place').order_by('start_time').values()
    return JsonResponse(list(all_events), safe=False)
