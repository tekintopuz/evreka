from django.utils import timezone
from rest_framework.response import Response
from rest_framework.views import APIView

from navigation.models import Vehicle
from navigation.serializers import VehicleSerializer


def get_last_two_days_records():
    two_days_ago = timezone.now() - timezone.timedelta(days=2)
    navigations = Vehicle.objects.filter(datetime__gte=two_days_ago)
    return navigations


class LastTwoHoursRecord(APIView):
    def get(self, request):
        vehicle_records = get_last_two_days_records()
        serializer = VehicleSerializer(vehicle_records, many=True)
        return Response(serializer.data)

