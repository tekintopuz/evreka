from django.db import models

from django.db.models.signals import post_save
from django.utils import timezone


class Bin(models.Model):
    name = models.CharField(max_length=255, blank=True, null=True)
    latitude = models.FloatField(blank=True, null=True)
    longitude = models.FloatField(blank=True, null=True)
    collection_frequency = models.IntegerField(default=0)
    last_collection = models.DateTimeField(blank=True, null=True)

    def __str__(self):
        return str(self.id) + ". " +self.name

class Operation(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name


class BinOperation(models.Model):
    bin = models.ForeignKey(Bin, on_delete=models.CASCADE)
    operation = models.ForeignKey(Operation, on_delete=models.CASCADE)
    datetime = models.DateTimeField(default=timezone.now, editable=False, db_index=True)

    def __str__(self):
        return "Bin-" + str(self.bin.id) + ") " + self.operation.name


def update_bin(sender, instance, **kwargs):
    instance.bin.collection_frequency += 1
    instance.bin.last_collection = instance.datetime
    instance.bin.save()


post_save.connect(update_bin, sender=BinOperation)
