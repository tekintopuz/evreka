from django.contrib import admin

# Register your models here.
from bin.models import Bin, Operation, BinOperation


class BinAdmin(admin.ModelAdmin):
    search_fields = ('id', 'name',  'latitude', 'longtitude', 'last_collection')


class OperationAdmin(admin.ModelAdmin):
    search_fields = ('id', 'name')


class BinOperationAdmin(admin.ModelAdmin):
    search_fields = ('id', 'bin__id', 'operation__id', 'operation__name', 'latitude', 'longtitude', 'datetime')


admin.site.register(Bin, BinAdmin)
admin.site.register(Operation, OperationAdmin)
admin.site.register(BinOperation, BinOperationAdmin)