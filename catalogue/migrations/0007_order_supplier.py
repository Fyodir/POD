# Generated by Django 2.1.5 on 2019-02-11 16:36

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('catalogue', '0006_auto_20190211_1631'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='supplier',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='catalogue.Supplier'),
        ),
    ]
