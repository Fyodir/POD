# Generated by Django 2.1.5 on 2019-03-11 10:20

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('catalogue', '0034_auto_20190304_1141'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='requisition_id',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='catalogue.Requisition'),
        ),
    ]