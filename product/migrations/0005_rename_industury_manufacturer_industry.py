# Generated by Django 4.0.3 on 2022-04-05 19:43

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0004_manufacturer_remove_product_brand_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='manufacturer',
            old_name='industury',
            new_name='industry',
        ),
    ]
