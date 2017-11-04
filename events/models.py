from django.db import models


class Event(models.Model):
    id = models.CharField(max_length=100, primary_key=True)
    event_name = models.CharField(max_length=1000)
    place_name = models.CharField(max_length=1000)
    start_time = models.DateTimeField()
    end_time = models.DateTimeField()

    description = models.TextField(blank=True)
    street = models.CharField(max_length=100, blank=True)
    city = models.CharField(max_length=100, blank=True)
    state = models.CharField(max_length=100, blank=True)
    zip = models.CharField(max_length=10, blank=True)
    country = models.CharField(max_length=100, blank=True)
    latitude = models.DecimalField(max_digits=9, decimal_places=6, blank=True, null=True)
    longitude = models.DecimalField(max_digits=9, decimal_places=6, blank=True, null=True)

    def __str__(this):
        return this.event_name


class Facebook(models.Model):
    name = models.CharField(max_length=100, primary_key=True)
    url = models.CharField(max_length=255)

    def __str__(this):
        return this.name
