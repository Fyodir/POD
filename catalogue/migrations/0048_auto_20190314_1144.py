# Generated by Django 2.1.5 on 2019-03-14 11:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('catalogue', '0047_auto_20190314_0954'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='date_created',
            field=models.DateField(auto_now_add=True),
        ),
    ]
