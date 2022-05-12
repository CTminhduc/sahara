# Generated by Django 4.0.3 on 2022-04-21 10:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0008_order_status'),
    ]

    operations = [
        migrations.CreateModel(
            name='Report',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=120)),
                ('image', models.ImageField(upload_to='uploads/products/')),
                ('remarks', models.TextField()),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
            ],
        ),
    ]