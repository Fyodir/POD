# Generated by Django 2.1.5 on 2019-03-18 15:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('catalogue', '0049_auto_20190314_1410'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='order_issue',
            field=models.CharField(choices=[('Yes', 'YES'), ('No', 'NO')], default='No', max_length=5),
        ),
        migrations.AlterField(
            model_name='order',
            name='qc_status',
            field=models.CharField(choices=[('N/a', 'N/A'), ('Room Temp', 'ROOM TEMP'), ('Dry Ice', 'DRY ICE'), ('Cold Block', 'COLD BLOCK')], default='N/a', max_length=24, verbose_name='Condition Received'),
        ),
    ]
