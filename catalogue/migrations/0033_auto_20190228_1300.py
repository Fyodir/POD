# Generated by Django 2.1.5 on 2019-02-28 13:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('catalogue', '0032_auto_20190228_1236'),
    ]

    operations = [
        migrations.AlterField(
            model_name='requisition',
            name='urgency',
            field=models.CharField(choices=[('Urgent', 'URGENT'), ('Non-Urgent', 'NON-URGENT')], default='non-urgent', max_length=10),
        ),
    ]
