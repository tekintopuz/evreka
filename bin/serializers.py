# Serializers define the API representation.
from django.utils import timezone
from rest_framework import serializers

from bin.models import Bin, Operation, BinOperation


class BinCollectionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Bin
        fields = ('pk', 'name', 'latitude', 'longitude', 'collection_frequency', 'last_collection', 'operations')

    last_collection = serializers.DateTimeField(format="%d.%m.%y %H:%M:%S", read_only=True, default=timezone.now)
    operations = serializers.SerializerMethodField('get_operations')

    def get_operations(self, obj):
        operations = []
        for operation in Operation.objects.all():
            my_query = BinOperation.objects.filter(bin=obj, operation=operation)
            if my_query.exists():
                operations.append({"operation": operation.name, "frequency": len(my_query)})
        return operations
