# Generated by Django 2.1.5 on 2019-02-15 16:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('catalogue', '0012_productinstance_stock_updater'),
    ]

    operations = [
        migrations.AddField(
            model_name='productinstance',
            name='date_updated',
            field=models.DateField(auto_now=True),
        ),
    ]