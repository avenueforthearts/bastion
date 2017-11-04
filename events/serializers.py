# from rest_framework import serializers
from events.models import Event, Place
from rest_framework import serializers


class PlaceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Place
        fields = '__all__'


class EventSerializer(serializers.ModelSerializer):
    place = PlaceSerializer()

    class Meta:
        model = Event
        fields = '__all__'
