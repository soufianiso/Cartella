# Generated by Django 4.1.7 on 2023-03-07 11:01

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    dependencies = [
        ("products", "0002_remove_orderitem_order_remove_orderitem_product_and_more"),
        ("cart", "0002_alter_orderitem_quantity"),
    ]

    operations = [
        migrations.AlterField(
            model_name="orderitem",
            name="order",
            field=models.OneToOneField(
                null=True, on_delete=django.db.models.deletion.SET_NULL, to="cart.order"
            ),
        ),
        migrations.AlterField(
            model_name="orderitem",
            name="product",
            field=models.OneToOneField(
                null=True,
                on_delete=django.db.models.deletion.SET_NULL,
                to="products.product",
            ),
        ),
    ]
