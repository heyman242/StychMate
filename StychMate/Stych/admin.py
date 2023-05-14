from django.contrib import admin
from .models import SKU, Tailor, Hub, Order, Order_Item, Hub_Inventory

admin.site.register(SKU)
admin.site.register(Tailor)
admin.site.register(Hub)
admin.site.register(Order)
admin.site.register(Order_Item)
admin.site.register(Hub_Inventory)
