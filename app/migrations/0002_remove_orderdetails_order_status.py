# Generated by Django 3.0.14 on 2022-01-23 10:19

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='orderdetails',
            name='order_status',
        ),
    ]
