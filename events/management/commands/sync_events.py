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
            url = facebook.get('url', '')
            events = self.request_events(url, graph)
            print("Received " + str(len(events)) + " events from " + url)
            for event in events:
                self.process_event(event)

    def request_events(self, org_url, graph):
        try:
            resp = graph.request(org_url)
            id = resp['id']
            int(id)  # Try to convert it to an int to verify it
            since = int(datetime.datetime.now(pytz.utc).timestamp())
            url = id + '/events?type=created&since={0}&fields={1}'.format(since, 'category,start_time,place,owner,description,name,end_time,ticket_uri,id,cover{source},event_times')
            print('Querying: {0}'.format(url))
            events = graph.request(url)
            return events.get('data', [])
        except Exception as error:
            print("Error: " + str(error) + ". Removing bad URL")
            self.remove_bad_url(org_url)
            return []

    def remove_bad_url(self, url):
        Facebook.objects.filter(url=url).delete()

    def process_event(self, event):
        parsed_event = self.create_event(event)
        event_serializer = EventSerializer(data=parsed_event)
        if event_serializer.is_valid():
            new_event, created = Event.objects.update_or_create(id=parsed_event['id'], defaults=parsed_event)
            if not created:
                print("Event was not created: " + str(parsed_event))
        else:
            print("Event was invalid: " + str(parsed_event))

    def create_event(self, event):
        parsed_event = {}
        parsed_event['id'] = event.get('id')
        parsed_event['event_name'] = event.get('name')
        parsed_event['start_time'] = event.get('start_time')
        parsed_event['end_time'] = event.get('end_time')
        parsed_event['description'] = event.get('description', '')
        parsed_event['category'] = event.get('category', '')
        parsed_event['owner'] = self.safe_get(event, 'owner', 'name')
        parsed_event['ticket_uri'] = event.get('ticket_uri', '')
        parsed_event['cover'] = self.safe_get(event, 'cover', 'source')
        parsed_event['place_name'] = self.safe_get(event, 'place', 'name')
        parsed_event['street'] = self.safe_get(event, 'place', 'location', 'street')
        parsed_event['city'] = self.safe_get(event, 'place', 'location', 'city')
        parsed_event['state'] = self.safe_get(event, 'place', 'location', 'state')
        parsed_event['country'] = self.safe_get(event, 'place', 'location', 'country')
        parsed_event['latitude'] = self.safe_get(event, 'place', 'location', 'latitude')
        parsed_event['longitude'] = self.safe_get(event, 'place', 'location', 'longitude')
        parsed_event['zip'] = self.safe_get(event, 'place', 'location', 'zip')

        # even more hacks
        if parsed_event['latitude'] == '':
            parsed_event['latitude'] = None
        if parsed_event['longitude'] == '':
            parsed_event['longitude'] = None

        return parsed_event

    def safe_get(self, dct, *keys):
        for key in keys:
            try:
                dct = dct[key]
            except KeyError:
                return ''
        return dct
