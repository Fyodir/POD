# Generated by Django 2.1.5 on 2019-02-11 16:38

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('catalogue', '0007_order_supplier'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='order',
            name='supplier',
        ),
    ]
