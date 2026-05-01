from django.db import models
from django.contrib.auth.models import User


class Service(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField(blank=True)
    price = models.DecimalField(max_digits=8, decimal_places=2)
    duration_days = models.PositiveIntegerField(default=1)  # скільки днів займає

    def __str__(self):
        return self.name


class Device(models.Model):
    DEVICE_TYPES = [
        ('phone', 'Смартфон'),
        ('laptop', 'Ноутбук'),
        ('tablet', 'Планшет'),
        ('other', 'Інше'),
    ]
    owner = models.ForeignKey(User, on_delete=models.CASCADE, related_name='devices')
    name = models.CharField(max_length=200)           # наприклад: "iPhone 13"
    device_type = models.CharField(max_length=20, choices=DEVICE_TYPES)
    serial_number = models.CharField(max_length=100, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.owner.username} — {self.name}"


class RepairOrder(models.Model):
    STATUS_CHOICES = [
        ('pending', 'Очікує'),
        ('in_progress', 'В роботі'),
        ('done', 'Виконано'),
        ('cancelled', 'Скасовано'),
    ]
    device = models.ForeignKey(Device, on_delete=models.CASCADE, related_name='orders')
    service = models.ForeignKey(Service, on_delete=models.CASCADE)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='pending')
    comment = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.device} — {self.service} ({self.get_status_display()})"