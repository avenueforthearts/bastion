from django.core.management.base import BaseCommand
from events.models import Event
import pytz
import datetime
from django.db.models import Q


class Command(BaseCommand):
    help = "Clean out events that have ended"

    def handle(self, *args, **options):
        end_thresh = datetime.datetime.now(pytz.utc)
        start_thresh = end_thresh - datetime.timedelta(days=15)

        Event.objects.filter(Q(start_time__lte=start_thresh) | Q(end_time__lte=end_thresh)).delete()
