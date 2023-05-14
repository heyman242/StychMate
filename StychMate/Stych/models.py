from django.db import models
from django.contrib.auth.models import User


class SKU(models.Model):
    sku_id = models.AutoField(primary_key=True)
    sku_name = models.CharField(max_length=100)
    sku_description = models.TextField()
    sku_price = models.DecimalField(max_digits=10, decimal_places=2)
    
    def __str__(self):
        return self.sku_name

class Tailor(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)
    tailor_id = models.CharField(max_length=5, unique=True)
    tailor_name = models.CharField(max_length=100)
    tailor_location = models.CharField(max_length=100)
    tailor_availability = models.CharField(max_length=100)
    tailor_payout = models.DecimalField(max_digits=6, decimal_places=2)

    def __str__(self):
        return self.tailor_name


class Hub(models.Model):
    hub_id = models.AutoField(primary_key=True)
    hub_location = models.CharField(max_length=100)
    hub_capacity = models.IntegerField()
    
    def __str__(self):
        return self.hub_location

class Order(models.Model):
    order_id = models.AutoField(primary_key=True)
    sku = models.ForeignKey(SKU, on_delete=models.CASCADE)
    quantity = models.IntegerField()
    customer_name = models.CharField(max_length=100)
    customer_address = models.TextField()
    order_status = models.CharField(max_length=100, default='Pending')
    delivery_info = models.TextField()
    assigned_hub = models.ForeignKey(Hub, on_delete=models.CASCADE, null=True, blank=True)
    assigned_tailor = models.ForeignKey(Tailor, on_delete=models.CASCADE, null=True, blank=True)
    completion_time = models.DateTimeField(null=True, blank=True)
    
    def __str__(self):
        return self.customer_name

class Order_Item(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE)
    sku = models.ForeignKey(SKU, on_delete=models.CASCADE)
    quantity = models.IntegerField()
    size = models.CharField(max_length=2)

    def __str__(self):
        return str(self.order.order_id) + ' - ' + self.sku.sku_name + ' - ' + self.size

class Hub_Inventory(models.Model):
    hub = models.ForeignKey(Hub, on_delete=models.CASCADE)
    sku = models.ForeignKey(SKU, on_delete=models.CASCADE)
    quantity = models.IntegerField()
    size = models.CharField(max_length=2)

    def __str__(self):
        return self.hub.hub_location + ' - ' + self.sku.sku_name + ' - ' + self.size
# Create your models here.
