import random
import datetime
from decimal import Decimal
from Stych.models import SKU, Hub, Order

# Define the list of SKUs
skus = SKU.objects.all()

# Define the list of hub locations
hub_locations = ['Mumbai', 'Pune', 'Bangalore', 'Hyderabad']


# Generate orders and assign to hubs
def generate_orders():
    for _ in range(1000):
        sku = random.choice(skus)
        quantity = random.randint(1, 10)
        order = Order.objects.create(sku=sku)
        order.assigned_hub = Hub.objects.get(hub_location=random.choice(hub_locations))
        order.save()


# Call the function to generate orders and assign hubs
generate_orders()
