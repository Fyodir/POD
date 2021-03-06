# Generated by Django 2.1.5 on 2019-02-01 12:11

from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantity', models.IntegerField(help_text='Enter required quantity')),
                ('date_created', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='ProductInstance',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, help_text='Unique ID for this particular instance across whole department', primary_key=True, serialize=False)),
                ('stock', models.IntegerField(help_text='Enter current stock', verbose_name='Current Stock')),
                ('minimum_stock', models.IntegerField(verbose_name='Minimum Stock')),
            ],
            options={
                'ordering': ['-stock'],
            },
        ),
        migrations.CreateModel(
            name='ProductType',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('description', models.TextField(help_text='Enter a brief description of the product_type', max_length=1000, null=True)),
                ('product_EROS', models.CharField(help_text='Enter the products unique EROS number', max_length=20, verbose_name='Product EROS')),
                ('price', models.DecimalField(decimal_places=2, max_digits=6)),
            ],
        ),
        migrations.CreateModel(
            name='Requisition',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, help_text='Unique ID for this requisition', primary_key=True, serialize=False)),
                ('order_ref', models.CharField(help_text='Enter EROS reference number for requisition', max_length=20, null=True, verbose_name='Requisition Reference EROS')),
                ('date_created', models.DateField(auto_now_add=True)),
                ('date_ordered', models.DateField(blank=True, help_text='Enter date requisition was sent for order', null=True)),
                ('urgency', models.CharField(choices=[('urgent', 'URGENT'), ('non-urgent', 'NON-URGENT')], default='non-urgent', max_length=10)),
                ('date_delivered', models.DateField(blank=True, help_text='Enter date requisition was received', null=True)),
                ('requisition_status', models.CharField(choices=[('incomplete', 'INCOMPLETE'), ('awaiting_auth', 'AWAITING AUTHORIZATION'), ('authorized', 'AUTHORIZED'), ('pending', 'ORDER SENT'), ('complete', 'ORDER COMPLETE')], default='incomplete', max_length=24)),
                ('comments', models.TextField(blank=True, help_text='Enter a comment if required', max_length=1000, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Storage',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(help_text='Enter name of storage facility (ie Fridge A)', max_length=200)),
                ('location', models.CharField(help_text='Enter location of storage facility (ie floor, room)', max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Supplier',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(help_text='Enter a supplier name', max_length=200)),
                ('phone', models.CharField(help_text='Enter supplier contact telephone number', max_length=200)),
                ('email', models.EmailField(help_text='Enter supplier contact email', max_length=200)),
                ('agent', models.CharField(blank=True, help_text='Enter agent name', max_length=200)),
            ],
            options={
                'ordering': ['name'],
            },
        ),
        migrations.CreateModel(
            name='Team',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(help_text='Enter team name', max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Temperature',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, help_text='Enter name for temp range', max_length=200)),
                ('minimum', models.DecimalField(decimal_places=2, help_text='Enter minimum temperature (centigrade)', max_digits=6)),
                ('maximum', models.DecimalField(decimal_places=2, help_text='Enter amximum temperature (centigrade)', max_digits=6)),
            ],
        ),
        migrations.AddField(
            model_name='storage',
            name='temp_range',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='catalogue.Temperature'),
        ),
        migrations.AddField(
            model_name='requisition',
            name='supplier',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='catalogue.Supplier'),
        ),
        migrations.AddField(
            model_name='producttype',
            name='supplier',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='catalogue.Supplier'),
        ),
        migrations.AddField(
            model_name='productinstance',
            name='product_type',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='catalogue.ProductType', verbose_name='Product'),
        ),
        migrations.AddField(
            model_name='productinstance',
            name='storage',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='catalogue.Storage'),
        ),
        migrations.AddField(
            model_name='productinstance',
            name='team',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='catalogue.Team'),
        ),
        migrations.AddField(
            model_name='order',
            name='product_type',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='catalogue.ProductType'),
        ),
        migrations.AddField(
            model_name='order',
            name='requisition_id',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='catalogue.Requisition'),
        ),
    ]
