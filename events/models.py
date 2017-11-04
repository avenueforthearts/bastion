from django.db import models


class Event(models.Model):
    id = models.CharField(max_length=100, primary_key=True)
    name = models.CharField(max_length=1000)
    description = models.TextField()
    start_time = models.DateTimeField()
    end_time = models.DateTimeField()

    place = models.ForeignKey('events.Place')

    def __str__(this):
        return this.name


class Place(models.Model):
    id = models.CharField(max_length=100, primary_key=True)
    name = models.CharField(max_length=1000)
    city = models.CharField(max_length=100)
    country = models.CharField(max_length=100)
    latitude = models.DecimalField(max_digits=9, decimal_places=6)
    longitude = models.DecimalField(max_digits=9, decimal_places=6)
    state = models.CharField(max_length=100)
    street = models.CharField(max_length=100)
    zip = models.CharField(max_length=10)

    def __str__(this):
        return this.name

class Facebook(models.Model):
    name = models.CharField(max_length=100, primary_key=True)
    url = models.CharField(max_length=255)

    def __str__(this):
        return this.name