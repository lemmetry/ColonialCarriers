from django.contrib import admin
from .models import *


class FacilityAdmin(admin.ModelAdmin):
    list_display = ('name', 'street_address', 'manager')


class ManagerAdmin(admin.ModelAdmin):
    list_display = ('last_name', 'first_name')


class ItemAdmin(admin.ModelAdmin):
    readonly_fields = ['time_stamp']
    list_display = ('id', 'facility', 'item_description', 'time_stamp')


admin.site.register(Facility, FacilityAdmin)
admin.site.register(Manager, ManagerAdmin)
admin.site.register(Item, ItemAdmin)
