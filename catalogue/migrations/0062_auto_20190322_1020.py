# Generated by Django 2.1.5 on 2019-03-22 10:20

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('catalogue', '0061_auto_20190321_1648'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='lot_id',
            field=models.CharField(blank=True, help_text='Enter Lot Number of product upon delivery', max_length=20, null=True, verbose_name='Lot Number'),
        ),
        migrations.AlterField(
            model_name='order',
            name='requisition_id',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, to='catalogue.Requisition', verbose_name='Requisition ID'),
        ),
        migrations.AlterField(
            model_name='producttype',
            name='lead_time',
            field=models.IntegerField(blank=True, help_text='Estimated delivery time required', null=True, verbose_name='Lead Time (Days)'),
        ),
    ]
