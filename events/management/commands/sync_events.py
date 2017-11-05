from django.core.management.base import BaseCommand
from events.models import Facebook, Event
from django.conf import settings
import facebook as FacebookSDK
from events.serializers import EventSerializer
import datetime
import pytz


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
        print(resp)
        id = resp['id']
        since = int(datetime.datetime.now(pytz.utc).timestamp())

        url = id + '/events?type=created&since={0}'.format(since)
        print('querying: {0}'.format(url))
        events = graph.request(url)
        print(events)
        return events.get('data', [])

    def process_event(self, event):
        parsed_event = self.create_event(event)
        event_serializer = EventSerializer(data=parsed_event)
        if event_serializer.is_valid():
            # print(parsed_event)
            new_event, created = Event.objects.update_or_create(**parsed_event)
            if not created:
                print("Dafaq")

    def create_event(self, event):
        parsed_event = {}
        parsed_event['id'] = event.get('id')
        parsed_event['event_name'] = event.get('name')
        parsed_event['start_time'] = event.get('start_time')
        parsed_event['end_time'] = event.get('end_time')
        parsed_event['description'] = event.get('description', '')
        parsed_event['place_name'] = self.safe_get(event, 'place', 'name')
        parsed_event['street'] = self.safe_get(event, 'place', 'location', 'street')
        parsed_event['city'] = self.safe_get(event, 'place', 'location', 'city')
        parsed_event['state'] = self.safe_get(event, 'place', 'location', 'state')
        parsed_event['country'] = self.safe_get(event, 'place', 'location', 'country')
        parsed_event['latitude'] = self.safe_get(event, 'place', 'location', 'latitude')
        parsed_event['longitude'] = self.safe_get(event, 'place', 'location', 'longitude')
        parsed_event['zip'] = self.safe_get(event, 'place', 'location', 'zip')
        return parsed_event

    def safe_get(self, dct, *keys):
        for key in keys:
            try:
                dct = dct[key]
            except KeyError:
                return ''
        return dct
