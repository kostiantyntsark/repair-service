from django.contrib import admin
from .models import Service, Device, RepairOrder

admin.site.register(Service)
admin.site.register(Device)
admin.site.register(RepairOrder)