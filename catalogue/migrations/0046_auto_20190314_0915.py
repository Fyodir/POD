# Generated by Django 2.1.5 on 2019-03-14 09:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('catalogue', '0045_auto_20190313_1001'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='productinstance',
            options={'ordering': ['product_type'], 'permissions': (('can_create_new_product_instance', 'Able to Create New Product Instance'), ('can_update_product_instance', 'Able to Update Product Instance'), ('can_delete_product_instance', 'Able to Delete Product Instance'))},
        ),
        migrations.RemoveField(
            model_name='requisition',
            name='authoriser',
        ),
        migrations.RemoveField(
            model_name='requisition',
            name='date_delivered',
        ),
        migrations.RemoveField(
            model_name='requisition',
            name='team',
        ),
        migrations.RemoveField(
            model_name='requisition',
            name='urgency',
        ),
        migrations.AlterField(
            model_name='requisition',
            name='requisition_status',
            field=models.CharField(choices=[('To Order', 'TO ORDER'), ('Sent', 'SENT')], default='To Order', max_length=24),
        ),
    ]
