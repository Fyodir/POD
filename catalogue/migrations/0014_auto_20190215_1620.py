# Generated by Django 2.1.5 on 2019-02-15 16:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('catalogue', '0013_productinstance_date_updated'),
    ]

    operations = [
        migrations.AlterField(
            model_name='productinstance',
            name='date_updated',
            field=models.DateTimeField(auto_now=True),
        ),
    ]
