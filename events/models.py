from django.db import models
from django.core.validators import URLValidator
from django.core.exceptions import ValidationError
import re as Regex


def valid_facebook_url(url):
    pattern = Regex.compile("https://www.facebook.com/\w+")
    val = URLValidator(regex=pattern)
    val(url)
    if not pattern.match(url):
        raise ValidationError


class Event(models.Model):
    id = models.CharField(max_length=100, primary_key=True)
    event_name = models.CharField(max_length=1000)
    place_name = models.CharField(max_length=1000)
    start_time = models.DateTimeField()
    end_time = models.DateTimeField()

    description = models.TextField(blank=True)
    category = models.CharField(max_length=100, blank=True)
    owner = models.CharField(max_length=1000, blank=True)
    ticket_uri = models.CharField(max_length=1000, blank=True)
    cover = models.CharField(max_length=1000, blank=True)
    street = models.CharField(max_length=100, blank=True)
    city = models.CharField(max_length=100, blank=True)
    state = models.CharField(max_length=100, blank=True)
    zip = models.CharField(max_length=10, blank=True)
    country = models.CharField(max_length=100, blank=True)
    latitude = models.DecimalField(max_digits=25, decimal_places=20, blank=True, null=True)
    longitude = models.DecimalField(max_digits=25, decimal_places=20, blank=True, null=True)

    def __str__(this):
        return this.event_name


class Facebook(models.Model):
    name = models.CharField(max_length=100, primary_key=True)
    url = models.CharField(max_length=255, validators=[valid_facebook_url])

    def __str__(this):
        return this.name
