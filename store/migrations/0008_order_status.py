# Generated by Django 4.0.3 on 2022-04-20 15:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0007_order_address_order_phone'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='status',
            field=models.BooleanField(default=False),
        ),
    ]