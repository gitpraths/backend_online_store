from django.db import migrations


def create_dummy_products(apps, schema_editor):
    Product = apps.get_model("product", "Product")
    products = [
        Product(
            name="Product 1",
            description="Description for Product 1",
            price=10.99,
            stock=100,
        ),
        Product(
            name="Product 2",
            description="Description for Product 2",
            price=15.99,
            stock=50,
        ),
        Product(
            name="Product 3",
            description="Description for Product 3",
            price=25.50,
            stock=20,
        ),
    ]
    Product.objects.bulk_create(products)


class Migration(migrations.Migration):
    dependencies = [
        (
            "product",
            "0001_initial",
        ),  # This line indicates that this migration depends on the initial migration
    ]

    operations = [
        migrations.RunPython(
            create_dummy_products
        ),  # This applies the dummy product creation function
    ]
