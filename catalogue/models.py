from django.db import models
from django.urls import reverse # Used to generate URLs by reversing the URL patterns
import uuid # Required for unique product instances
from django.contrib.auth.models import User

class Team(models.Model):
    """Model representing a laboratory team."""
    name = models.CharField(max_length=200, help_text='Enter team name')

    def __str__(self):
        """String for representing the Model object."""
        return self.name

    def get_absolute_url(self):
        """Returns the url to access a detail record for this object."""
        return reverse('team-detail', args=[str(self.id)])


class Supplier(models.Model):
    """Model representing a product supplier."""
    name = models.CharField(max_length=200, help_text='Enter a supplier name')
    phone = models.CharField(max_length=200, help_text='Enter supplier contact telephone number')
    email = models.EmailField(max_length=200, help_text='Enter supplier contact email')
    agent = models.CharField(max_length=200, help_text='Enter agent name', blank=True)

    class Meta:
        ordering = ['name']

    def __str__(self):
        """String for representing the Model object."""
        return self.name

    def get_absolute_url(self):
        """Returns the url to access a detail record for this object."""
        return reverse('supplier-detail', args=[str(self.id)])


class ProductType(models.Model):
    """Model representing a type of product (but not a specific instance of a product)."""
    name = models.CharField(max_length=200)
    supplier = models.ForeignKey('Supplier', on_delete=models.SET_NULL, null=True)
    description = models.TextField(max_length=1000, null=True, help_text='Enter a brief description of the product_type')
    product_EROS = models.CharField('Product EROS', max_length=20, help_text='Enter the products unique EROS number')
    price = models.DecimalField(max_digits=8, decimal_places=2)

    def __str__(self):
        """String for representing the Model object."""
        return self.name

    def get_absolute_url(self):
        """Returns the url to access a detail record for this object."""
        return reverse('product-type-detail', args=[str(self.id)])

class Temperature(models.Model):
    """Model representing a temperature ranges for storage locations."""
    name = models.CharField(max_length=200, help_text='Enter name for temp range', blank=True)
    minimum = models.DecimalField(max_digits=6, decimal_places=2, help_text='Enter minimum temperature (centigrade)')
    maximum = models.DecimalField(max_digits=6, decimal_places=2, help_text='Enter amximum temperature (centigrade)')

    def __str__(self):
        """String for representing the Model object."""
        return self.name

class Storage(models.Model):
    """Model representing storage locations of product instances"""
    name = models.CharField(max_length=200, help_text="Enter name of storage facility (ie Fridge A)")
    location = models.CharField(max_length=200, help_text="Enter location of storage facility (ie floor, room)")
    temp_range = models.ForeignKey('Temperature', on_delete=models.SET_NULL, null=True)

    def __str__(self):
        """String for representing the Model object."""
        return self.name

class ProductInstance(models.Model):
    """Model representing a specific instance of a product"""
    product_type = models.ForeignKey('ProductType', verbose_name='Product', on_delete=models.SET_NULL, null=True)
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, help_text='Unique ID for this particular instance across whole department')
    team = models.ForeignKey('Team', on_delete=models.SET_NULL, null=True)
    storage = models.ForeignKey('Storage', on_delete=models.SET_NULL, null=True)
    stock = models.IntegerField('Current Stock', help_text='Enter current stock')
    minimum_stock = models.IntegerField('Minimum Stock')

    # should a product instance be an updateable stock level? or a new instance for each delivery?

    class Meta:
        ordering = ['-stock']

    def __str__(self):
        """String for representing the Model object."""
        return self.product_type.name

class Order(models.Model):
    """Model representing individual orders for an instance of a product type"""
    # Need to link a user account to an order
    product_type = models.ForeignKey('ProductType', on_delete=models.SET_NULL, null=True)
    requisition_id = models.ForeignKey('Requisition', on_delete=models.SET_NULL, null=True)
    quantity = models.IntegerField(help_text='Enter required quantity')
    date_created = models.DateTimeField(auto_now_add=True)
    orderer = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True)

    def __str__(self):
        """String for representing the Model object."""
        return f'{self.product_type.name} ({self.id})'

    def get_absolute_url(self):
        """Returns the url to access a detail record for this object."""
        return reverse('order-detail', args=[str(self.id)])

class Requisition(models.Model):
    """Model representing a collection of orders from a single supplier"""
    # id = models.UUIDField(primary_key=True, default=uuid.uuid4, help_text='Unique ID for this requisition')
    supplier = models.ForeignKey('Supplier', on_delete=models.SET_NULL, null=True)
    team = models.ForeignKey('Team', on_delete=models.SET_NULL, null=True)
    req_ref = models.CharField('Requisition Reference EROS', max_length=20, help_text='Enter EROS reference number for requisition', null=True, blank=True)
    date_created = models.DateField(auto_now_add=True)
    date_sent = models.DateField(help_text='Enter date requisition was sent for order', null=True, blank=True)

    URGENCY = (
        ('urgent', 'URGENT'),
        ('non-urgent', 'NON-URGENT')
    )

    urgency = models.CharField(max_length=10, choices=URGENCY, default='non-urgent')

    date_delivered = models.DateField(help_text='Enter date requisition was received', null=True, blank=True)

    STATUS = (
        ('incomplete', 'INCOMPLETE'),
        ('awaiting_auth', 'AWAITING AUTHORIZATION'),
        ('authorized', 'AUTHORIZED'),
        ('sent', 'SENT'),
        ('complete', 'COMPLETE')
    )

    requisition_status = models.CharField(max_length=24, choices=STATUS, default='incomplete')
    comments = models.TextField(max_length=1000, help_text='Enter a comment if required', null=True, blank=True)


    def __str__(self):
        """String for representing the Model object."""
        return f'{self.id} - {self.supplier.name} - {self.urgency} - ({self.requisition_status})'

    def get_absolute_url(self):
        """Returns the url to access a detail record for this object."""
        return reverse('requisition-detail', args=[str(self.id)])

    # Fields to add - user id, authorizer id, total price of req, attachments,
