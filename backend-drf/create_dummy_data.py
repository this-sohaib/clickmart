import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'clickmart_main.settings')
django.setup()

from products.models import Product
from decimal import Decimal

def create_product():
    product, created = Product.objects.get_or_create(
        name="Premium Smart Watch",
        defaults={
            "description": "A sleek and modern smartwatch with advanced health tracking features and a premium metallic band.",
            "price": Decimal("299.99"),
            "stock": 50,
            "image": "products/smart_watch.png",
            "is_active": True
        }
    )
    if created:
        print(f"Product '{product.name}' created successfully.")
    else:
        print(f"Product '{product.name}' already exists.")

if __name__ == "__main__":
    create_product()
