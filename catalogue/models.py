from django.db import models
from django.urls import reverse # Used to generate URLs by reversing the URL patterns
import uuid # Required for unique product instances
from django.contrib.auth.models import User
import datetime

class Team(models.Model):
    """Model representing a laboratory team."""
    name = models.CharField(max_length=200, help_text='Enter team name')

    class Meta:
        permissions = (("can_create_new_team", "Able to Create New Team" ), ("can_update_team", "Able to Update Team"), ("can_delete_team", "Able to Delete Team"),)


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
        permissions = (("can_create_new_supplier", "Able to Create New Supplier" ), ("can_update_supplier", "Able to Update Supplier"), ("can_delete_supplier", "Able to Delete Supplier"),)

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
    price = models.DecimalField('Price (£)', max_digits=8, decimal_places=2)

    class Meta:
        permissions = (("can_create_new_product_type", "Able to Create New Product Type" ), ("can_update_product_type", "Able to Update Product Type"), ("can_delete_product_type", "Able to Delete Product Type"),)

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

    class Meta:
        permissions = (("can_create_new_temperature", "Able to Create New Temperature" ), ("can_update_temperature", "Able to Update Temoperature"), ("can_delete_temperature", "Able to Delete Temperature"),)

    def __str__(self):
        """String for representing the Model object."""
        return self.name

    def get_absolute_url(self):
        """Returns the url to access a detail record for this object."""
        return reverse('temperature-detail', args=[str(self.id)])

class Storage(models.Model):
    """Model representing storage locations of product instances"""
    name = models.CharField(max_length=200, help_text="Enter name of storage facility (ie Fridge A)")
    location = models.CharField(max_length=200, help_text="Enter location of storage facility (ie floor, room)")
    temp_range = models.ForeignKey('Temperature', on_delete=models.SET_NULL, null=True)

    class Meta:
        permissions = (("can_create_new_storage", "Able to Create New Storage" ), ("can_update_storage", "Able to Update Storage"), ("can_delete_storage", "Able to Delete Storage"),)


    def __str__(self):
        """String for representing the Model object."""
        return f'{self.name} ({self.temp_range.minimum}°C to {self.temp_range.maximum}°C)'


    def get_absolute_url(self):
        """Returns the url to access a detail record for this object."""
        return reverse('storage-detail', args=[str(self.id)])

class ProductInstance(models.Model):
    """Model representing a specific instance of a product"""
    product_type = models.ForeignKey('ProductType', verbose_name='Product', on_delete=models.SET_NULL, null=True)
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, help_text='Unique ID for this particular instance across whole department')
    team = models.ForeignKey('Team', on_delete=models.SET_NULL, null=True)
    storage = models.ForeignKey('Storage', on_delete=models.SET_NULL, null=True)
    stock = models.IntegerField('Current Stock', help_text='Enter current stock')
    minimum_stock = models.IntegerField('Minimum Stock')
    stock_updater = models.ForeignKey(User, verbose_name='User', on_delete=models.SET_NULL, null=True, blank=True)
    date_updated = models.DateTimeField(auto_now=True)

    # should a product instance be an updateable stock level? or a new instance for each delivery?

    class Meta:
        ordering = ['-stock']
        permissions = (("can_create_new_product_instance", "Able to Create New Product Instance" ), ("can_update_product_instance", "Able to Update Product Instance"), ("can_delete_product_instance", "Able to Delete Product Instance"),)

    def __str__(self):
        """String for representing the Model object."""
        return self.product_type.name

    def get_absolute_url(self):
        """Returns the url to access a detail record for this object."""
        return reverse('product-instance-detail', args=[str(self.id)])

    @property
    def stock_is_low(self):
        if self.stock < self.minimum_stock:
            return True
        return False


class Order(models.Model):
    """Model representing individual orders for an instance of a product type"""
    # Need to link a user account to an order
    requisition_id = models.ForeignKey('Requisition', on_delete=models.SET_NULL, null=True, blank=True)
    product_type = models.ForeignKey('ProductType', on_delete=models.SET_NULL, null=True)
    quantity = models.IntegerField(help_text='Enter required quantity')
    date_created = models.DateTimeField(auto_now_add=True)
    orderer = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)

    class Meta:
        permissions = (("can_create_new_order", "Able to Create New Order" ), ("can_update_order", "Able to Update Order"), ("can_delete_order", "Able to Delete Order"),)


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
    URGENCY = (
        ('urgent', 'URGENT'),
        ('non-urgent', 'NON-URGENT')
    )

    urgency = models.CharField(max_length=10, choices=URGENCY, default='non-urgent')
    authoriser = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    req_ref = models.CharField('Requisition Reference EROS', max_length=20, help_text='Enter EROS reference number for requisition', null=True, blank=True)
    date_created = models.DateField(auto_now_add=True)
    date_sent = models.DateField(help_text='Enter date requisition was sent for order (YYYY-MM-DD)', null=True, blank=True)



    date_delivered = models.DateField(help_text='Enter date requisition was received (YYYY-MM-DD)', null=True, blank=True)

    STATUS = (
        ('incomplete', 'INCOMPLETE'),
        ('awaiting_auth', 'AWAITING AUTHORIZATION'),
        ('authorized', 'AUTHORIZED'),
        ('sent', 'SENT'),
        ('complete', 'COMPLETE')
    )

    requisition_status = models.CharField(max_length=24, choices=STATUS, default='incomplete')
    comments = models.TextField(max_length=1000, help_text='Enter a comment if required', null=True, blank=True)

    class Meta:
        permissions = (("can_create_new_requisition", "Able to Create New Requisition" ), ("can_update_requisition", "Able to Update Requisition"), ("can_delete_requisition", "Able to Delete Requisition"),)


    def __str__(self):
        """String for representing the Model object."""
        return f'({self.id}) {self.req_ref}'

    def get_absolute_url(self):
        """Returns the url to access a detail record for this object."""
        return reverse('requisition-detail', args=[str(self.id)])

    # Fields to add - user id, authorizer id, total price of req, attachments,
