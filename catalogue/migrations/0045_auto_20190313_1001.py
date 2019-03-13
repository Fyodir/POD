# Generated by Django 2.1.5 on 2019-03-13 10:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('catalogue', '0044_auto_20190312_1250'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='order_status',
            field=models.CharField(choices=[('Order Created', 'ORDER CREATED'), ('Received', 'RECEIVED'), ('Received Frozen', 'RECEIVED FROZEN'), ('Delayed', 'ORDER DELAYED'), ('Damaged', 'DAMAGED')], default='order_created', max_length=24),
        ),
    ]
