# Generated by Django 2.1.5 on 2019-02-25 12:14

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('catalogue', '0016_auto_20190225_1128'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='producttype',
            options={'permissions': (('can_create_new_product_type', 'Able to Create New Product Type'), ('can_update_product_type', 'Able to Update Product Type'), ('can_delete_product_type', 'Able to Delete Product Type'))},
        ),
    ]
