# Serializers define the API representation.
from django.utils import timezone
from rest_framework import serializers

from navigation.models import NavigationRecord, Vehicle


class VehicleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Vehicle
        fields = ['latitude', 'longitude', 'vehicle_plate', 'datetime']

    datetime = serializers.DateTimeField(format="%d.%m.%y %H:%M:%S", read_only=True, default=timezone.now)
    vehicle_plate = serializers.SerializerMethodField('get_vehicle_plate')

    def get_vehicle_plate(self, obj):
        return obj.plate


class NavigationRecordSerializer(serializers.ModelSerializer):
    class Meta:
        model = NavigationRecord
        fields = ('latitude', 'longitude', 'vehicle_plate', 'datetime')

    datetime = serializers.DateTimeField(format="%d.%m.%y %H:%M:%S", read_only=True, default=timezone.now)
    vehicle_plate = serializers.SerializerMethodField('get_vehicle_plate')

    def get_vehicle_plate(self, obj):
        return obj.vehicle.plate
