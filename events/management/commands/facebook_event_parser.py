from django.core.management.base import BaseCommand, CommandError
from events.models import Facebook
import re

class Command(BaseCommand):
  help = "Does a thing"

  # def add_arguments(self, parser):
  #   # self.stdout("No arguments to")
  #   parser.add_argument('our_arg', nargs='+', type=int)

  def handle(self, *args, **options):
    pattern = re.compile("https:\/\/(www\.)?facebook.com\/events\/\d{16}\/?")
    self.stdout.write("Print me")
    for facebook in Facebook.objects.values():
      print(facebook['url'])
      # url = facebook['url']
      # if not pattern.match(url):
      #   continue
      # split_url = url.split("/")
      # print(split_url[-2])


