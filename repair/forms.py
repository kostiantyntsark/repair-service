from django import forms
from .models import Service, Device, RepairOrder


class ServiceForm(forms.ModelForm):
    class Meta:
        model = Service
        fields = ['name', 'description', 'price', 'duration_days']


class DeviceForm(forms.ModelForm):
    class Meta:
        model = Device
        fields = ['name', 'device_type', 'serial_number']


class RepairOrderForm(forms.ModelForm):
    class Meta:
        model = RepairOrder
        fields = ['device', 'service', 'comment']