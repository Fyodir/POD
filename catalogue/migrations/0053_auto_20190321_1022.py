# Generated by Django 2.1.5 on 2019-03-21 10:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('catalogue', '0052_auto_20190319_1444'),
    ]

    operations = [
        migrations.AlterField(
            model_name='producttype',
            name='description',
            field=models.TextField(blank=True, help_text='Enter a brief description of the product_type', max_length=1000, null=True),
        ),
    ]