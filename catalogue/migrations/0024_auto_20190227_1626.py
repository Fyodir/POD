# Generated by Django 2.1.5 on 2019-02-27 16:26

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('catalogue', '0023_auto_20190225_1428'),
    ]

    operations = [
        migrations.AddField(
            model_name='requisition',
            name='authoriser',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='requisition',
            name='date_delivered',
            field=models.DateField(blank=True, help_text='Enter date requisition was received (YYYY-MM-DD)', null=True),
        ),
        migrations.AlterField(
            model_name='requisition',
            name='date_sent',
            field=models.DateField(blank=True, help_text='Enter date requisition was sent for order (YYYY-MM-DD)', null=True),
        ),
    ]
