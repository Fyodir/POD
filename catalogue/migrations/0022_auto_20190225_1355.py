# Generated by Django 2.1.5 on 2019-02-25 13:55

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('catalogue', '0021_auto_20190225_1338'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='temperature',
            options={'permissions': (('can_create_new_temperature', 'Able to Create New Temperature'), ('can_update_temperature', 'Able to Update Temoperature'), ('can_delete_temperature', 'Able to Delete Temperature'))},
        ),
    ]
