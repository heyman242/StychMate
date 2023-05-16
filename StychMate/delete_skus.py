from Stych.models import SKU


# Delete all SKUs
def delete_skus():
    SKU.objects.all().delete()


# Call the function to delete SKUs
delete_skus()
