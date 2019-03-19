# Generated by Django 2.1.5 on 2019-02-28 10:11

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('catalogue', '0024_auto_20190227_1626'),
    ]

    operations = [
        migrations.AlterField(
            model_name='productinstance',
            name='stock_updater',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL, verbose_name='User'),
        ),
        migrations.AlterField(
            model_name='producttype',
            name='price',
            field=models.DecimalField(decimal_places=2, max_digits=8, verbose_name='Price (£)'),
        ),
    ]