# from rest_framework import serializers
from rest_framework import serializers


class EventSerializer(serializers.Serializer):
    id = serializers.CharField(max_length=100)
    event_name = serializers.CharField(max_length=1000)
    place_name = serializers.CharField(max_length=1000)
    start_time = serializers.DateTimeField()

    def validate_id(self, value):
        return value

    def validate_event_name(self, value):
        return value

    def validate_place_name(self, value):
        return value

    def validate_start_time(self, value):
        return value
