import random
from Stych.models import SKU, Hub, Order

# Define the list of SKUs
skus = SKU.objects.all()

# Define the list of hub locations
hub_locations = ['Mumbai', 'Pune', 'Bangalore', 'Hyderabad', 'kolkata', ]


# Generate orders and assign to hubs
def generate_orders():
    for _ in range(1000):
        sku = random.choice(skus)
        order = Order.objects.create(sku=sku)
        assigned_hubs = Hub.objects.filter(hub_location=random.choice(hub_locations))
        if assigned_hubs.exists():
            order.assigned_hub = assigned_hubs.first()
            order.save()


# use this command to generate orders <python manage.py shell < generate_orders_script.py>

# Call the function to generate orders and assign hubs
generate_orders()
