# Generated by Django 2.1.5 on 2019-03-18 21:34

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('catalogue', '0050_auto_20190318_1556'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='requisition_id',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, to='catalogue.Requisition'),
        ),
    ]