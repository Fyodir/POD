# Generated by Django 2.1.5 on 2019-03-11 10:28

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('catalogue', '0037_auto_20190311_1027'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='requisition',
            options={'ordering': ['-id'], 'permissions': (('can_create_new_requisition', 'Able to Create New Requisition'), ('can_update_requisition', 'Able to Update Requisition'), ('can_delete_requisition', 'Able to Delete Requisition'))},
        ),
    ]
