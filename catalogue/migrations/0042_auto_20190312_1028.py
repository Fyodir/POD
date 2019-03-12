# Generated by Django 2.1.5 on 2019-03-12 10:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('catalogue', '0041_auto_20190311_1404'),
    ]

    operations = [
        migrations.AlterField(
            model_name='requisition',
            name='requisition_status',
            field=models.CharField(choices=[('To Order', 'TO ORDER'), ('Incomplete', 'INCOMPLETE'), ('Authorised', 'AUTHORISED'), ('Sent', 'SENT'), ('Complete', 'COMPLETE')], default='Incomplete', max_length=24),
        ),
    ]
