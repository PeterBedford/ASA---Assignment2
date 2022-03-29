# Generated by Django 4.0.3 on 2022-03-29 08:47

import datetime
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('product', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='date_released',
            field=models.DateTimeField(verbose_name=datetime.datetime(2022, 3, 29, 8, 47, 30, 374503)),
        ),
        migrations.CreateModel(
            name='Review',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('rating', models.IntegerField(choices=[(1, 'Poor'), (2, 'Unstatisfactory'), (3, 'Satisfactory'), (4, 'Very Satisfactory'), (5, 'Outstanding')])),
                ('description', models.TextField()),
                ('date_posted', models.DateField(auto_now=True)),
                ('Author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('Product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='Reviews', to='product.product')),
            ],
        ),
    ]
