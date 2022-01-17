from django.db import models
from django.utils import timezone
from django.db.models.signals import post_save


class Vehicle(models.Model):
    plate = models.CharField(max_length=20, unique=True, db_index=True)
    latitude = models.FloatField(blank=True, null=True)
    longitude = models.FloatField(blank=True, null=True)
    datetime = models.DateTimeField(blank=True, null=True)

    def save(self, *args, **kwargs):
        self.plate = self.plate.upper()
        return super(Vehicle, self).save(*args, **kwargs)

    def __str__(self):
        return self.plate


class NavigationRecord(models.Model):
    vehicle = models.ForeignKey(Vehicle, on_delete=models.CASCADE, related_name='vehicle')
    datetime = models.DateTimeField(default=timezone.now, editable=False, db_index=True)
    latitude = models.FloatField(blank=True, null=True)
    longitude = models.FloatField(blank=True, null=True)

    def save(self, *args, **kwargs):
        if not self.pk:
            self.datetime = timezone.now()

        return super(NavigationRecord, self).save(*args, **kwargs)

    def __str__(self):
        return self.datetime.strftime("%Y-%m-%d %H:%M:%S")


def update_vehicle(sender, instance, **kwargs):
    instance.vehicle.latitude = instance.latitude
    instance.vehicle.longitude = instance.longitude
    instance.vehicle.datetime = instance.datetime
    instance.vehicle.save()


post_save.connect(update_vehicle, sender=NavigationRecord)
