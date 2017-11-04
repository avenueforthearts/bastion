from django.core.management.base import BaseCommand
from events.models import Facebook, Event
from django.conf import settings
import facebook as FacebookSDK
from events.serializers import EventSerializer

class Command(BaseCommand):
    help = "Loops through defined facebook URLs and creates events/locations"

    def handle(self, *args, **options):
        token = settings.FACEBOOK_TOKEN
        graph = FacebookSDK.GraphAPI(access_token=token, version='2.7')
        for facebook in Facebook.objects.values():
            events = self.request_events(facebook['url'], graph)
            for event in events:
                self.process_event(event)

    def request_events(self, org_url, graph):
        resp = graph.request(org_url)
        id = resp['id']
        events = graph.request(id + '/events?type=created')
        return events['data']

    def process_event(self, event):
        event_serializer = EventSerializer(data=event)
        print("What is this")
        if event_serializer.is_valid():
            print(event)
            new_event, created = Event.objects.update_or_create(**event)
            if not created:
                print("Dafaq")

