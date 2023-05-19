from django.db import models
from django.contrib.auth.models import User
import json


class SKU(models.Model):
    sku_id = models.AutoField(primary_key=True)
    sku_name = models.CharField(max_length=100)
    sku_price = models.DecimalField(max_digits=10, decimal_places=2)
    sku_size = models.CharField(max_length=10, default='')

    def __str__(self):
        return self.sku_name


class Tailor(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)
    tailor_id = models.CharField(max_length=5, unique=True)
    tailor_name = models.CharField(max_length=100)
    tailor_location = models.CharField(max_length=100)
    tailor_payout = models.DecimalField(default=0, max_digits=10, decimal_places=2)
    sku_units_worked = models.JSONField(default=dict)

    def __str__(self):
        return self.tailor_name


class Hub(models.Model):
    hub_id = models.AutoField(primary_key=True)
    hub_location = models.CharField(max_length=100)

    def __str__(self):
        return self.hub_location


class Order(models.Model):
    ORDER_STATUS_CHOICES = [
        ('Pending', 'Pending'),
        ('Assigned', 'Assigned'),
        ('Completed', 'Completed'),
    ]

    order_id = models.AutoField(primary_key=True)
    sku = models.ForeignKey(SKU, on_delete=models.CASCADE)
    order_status = models.CharField(max_length=100, choices=ORDER_STATUS_CHOICES, default='Pending')
    assigned_hub = models.ForeignKey(Hub, on_delete=models.CASCADE, null=True, blank=True)
    assigned_date = models.DateField(blank=True, null=True)

    def __str__(self):
        return f"Order ID: {self.order_id}, Status: {self.order_status}"
