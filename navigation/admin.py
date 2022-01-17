from __future__ import unicode_literals
from django.contrib import admin
from navigation.models import *


class VehicleAdmin(admin.ModelAdmin):
    search_fields = ('id', 'plate')


class NavigationRecordAdmin(admin.ModelAdmin):
    search_fields = ('id', 'vehicle__plate', 'datetime', 'latitude', 'longitude')


admin.site.register(Vehicle, VehicleAdmin)
admin.site.register(NavigationRecord, NavigationRecordAdmin)

