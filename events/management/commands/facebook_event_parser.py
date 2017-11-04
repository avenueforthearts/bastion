from django.core.management.base import BaseCommand
from events.models import Facebook
from django.conf import settings


class Command(BaseCommand):
    help = "Does a thing"

    def handle(self, *args, **options):
        # print(settings.FACEBOOK_TOKEN)
        for facebook in Facebook.objects.values():
            print(facebook)
