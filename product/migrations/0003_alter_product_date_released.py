# Generated by Django 4.0.3 on 2022-03-29 08:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0002_alter_product_date_released_review'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='date_released',
            field=models.DateField(auto_now=True),
        ),
    ]
