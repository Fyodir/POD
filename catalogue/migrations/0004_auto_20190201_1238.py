# Generated by Django 2.1.5 on 2019-02-01 12:38

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('catalogue', '0003_auto_20190201_1231'),
    ]

    operations = [
        migrations.RenameField(
            model_name='requisition',
            old_name='order_ref',
            new_name='req_ref',
        ),
    ]
