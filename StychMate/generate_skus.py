from decimal import Decimal
from Stych.models import SKU

# Define the price range and sizes
price_range = range(345, 996)
sizes = ['XS', 'S', 'M', 'L', 'XL']


# Generate unique SKUs
def generate_skus():
    sku_count = 0
    for price in price_range:
        for size in sizes:
            sku_name = f"SKU-{price}-{size}"
            sku_price = Decimal(price)
            sku_size = size
            sku = SKU.objects.create(sku_name=sku_name, sku_price=sku_price, sku_size=sku_size)
            sku.sku_id = sku_count + 1
            sku.save()
            sku_count += 1
            if sku_count == 5000:
                return


# Call the function to generate SKUs
generate_skus()
