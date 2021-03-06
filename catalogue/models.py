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
        ordering = ["name"]


    def __str__(self):
        """String for representing the Model object."""
        return self.name

    def get_absolute_url(self):
        """Returns the url to access a detail record for this object."""
        return reverse('team-detail', args=[str(self.id)])


class Supplier(models.Model):
    """Model representing a product supplier."""
    name = models.CharField(max_length=200, help_text='Enter a supplier name')
    phone = models.CharField(max_length=50, help_text='Enter supplier contact telephone number')
    email = models.EmailField(max_length=50, help_text='Enter supplier contact email', null=True, blank=True)
    address = models.TextField(max_length=200, help_text='Enter an address for the supplier', blank=True)
    comments = models.TextField(max_length=200, blank=True)
    # agent = models.CharField(max_length=200, help_text='Enter agent name', null=True, blank=True)

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
    description = models.TextField(max_length=1000, help_text='Enter a brief description of the product_type', blank=True, null=True)
    product_EROS = models.CharField('Product EROS', max_length=20, help_text='Enter the products unique EROS number')
    price = models.DecimalField('Price (£)', max_digits=8, decimal_places=2)
    lead_time = models.IntegerField('Lead Time (Days)', help_text='Estimated delivery time required', blank=True, null=True)

    class Meta:
        permissions = (("can_create_new_product_type", "Able to Create New Product Type" ), ("can_update_product_type", "Able to Update Product Type"), ("can_delete_product_type", "Able to Delete Product Type"),)
        ordering =["name"]

    def save(self, *args, **kwargs):
        if(self.lead_time > 0):
            super(ProductType, self).save(*args, **kwargs)
        else:
            raise Exception("Lead Time cannot be less than 0 days")

    def save(self, *args, **kwargs):
        if(self.price >= 0):
            super(ProductType, self).save(*args, **kwargs)
        else:
            raise Exception("Price cannot be less than £0")

    def __str__(self):
        """String for representing the Model object."""
        return self.name

    def get_absolute_url(self):
        """Returns the url to access a detail record for this object."""
        return reverse('product-type-detail', args=[str(self.id)])

class Temperature(models.Model):
    """Model representing a temperature ranges for storage locations."""
    name = models.CharField(max_length=200, help_text='Enter name for temperature range')
    minimum = models.DecimalField(max_digits=6, decimal_places=2, help_text='Enter minimum temperature (°C)')
    maximum = models.DecimalField(max_digits=6, decimal_places=2, help_text='Enter maximum temperature (°C)')

    class Meta:
        ordering =["name"]
        permissions = (("can_create_new_temperature", "Able to Create New Temperature" ), ("can_update_temperature", "Able to Update Temoperature"), ("can_delete_temperature", "Able to Delete Temperature"),)

    def save(self, *args, **kwargs):
        if(self.maximum > self.minimum):
            super(Temperature, self).save(*args, **kwargs)
        else:
            raise Exception("Maximum temperature cannot be below Minimum temperature")

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
    temp_range = models.ForeignKey('Temperature', on_delete=models.CASCADE, null=True)

    class Meta:
        permissions = (("can_create_new_storage", "Able to Create New Storage" ), ("can_update_storage", "Able to Update Storage"), ("can_delete_storage", "Able to Delete Storage"),)
        ordering = ["name"]

    def __str__(self):
        """String for representing the Model object."""
        return f'{self.name} ({self.location})'

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
        ordering = ['product_type', 'team']
        permissions = (("can_create_new_product_instance", "Able to Create New Product Instance" ), ("can_update_product_instance", "Able to Update Product Instance"), ("can_delete_product_instance", "Able to Delete Product Instance"),)

    def save(self, *args, **kwargs):
        if(self.stock >= 0):
            super(ProductInstance, self).save(*args, **kwargs)
        else:
            raise Exception("Stock cannot be less than 0")

    def save(self, *args, **kwargs):
        if(self.minimum_stock > 0):
            super(ProductInstance, self).save(*args, **kwargs)
        else:
            raise Exception("Minimum stock cannot be less than 1")

    def __str__(self):
        """String for representing the Model object."""
        return self.product_type.name

    def get_absolute_url(self):
        """Returns the url to access a detail record for this object."""
        return reverse('product-instance-detail', args=[str(self.id)])

    @property
    def stock_diff(self):
        # returns a positive value if stock is below minimum_stock. Shows differene in stock levels
        return self.minimum_stock - self.stock

    @property
    def stock_is_low(self):
        # Returns true if stock is below minimum stock value
        if self.stock < self.minimum_stock:
            return True
        return False


class Order(models.Model):
    """Model representing individual orders for an instance of a product type"""
    team = models.ForeignKey('Team', on_delete=models.SET_NULL, null=True)
    requisition_id = models.ForeignKey('Requisition', verbose_name="Requisition ID", on_delete=models.PROTECT, null=True)
    product_type = models.ForeignKey('ProductType', verbose_name="Product Type", on_delete=models.SET_NULL, null=True)
    quantity = models.IntegerField(help_text='Enter required quantity')

    URGENCY = (
        ('Urgent', 'URGENT'),
        ('Non-Urgent', 'NON-URGENT')
    )
    urgency = models.CharField(max_length=10, choices=URGENCY, default='Non-Urgent')

    orderer = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)

    ISSUE = (
        ('Yes', 'YES'),
        ('No', 'NO')
    )
    order_issue = models.CharField(max_length=5, choices=ISSUE, default="No")

    STATUS = (
        ('Order Created', 'CREATED'),
        ('Order Sent', 'SENT'),
        ('Part Received', 'PART RECEIVED'),
        ('Complete', 'COMPLETE'),
    )
    order_status = models.CharField(max_length=24, choices=STATUS, default='order_created')

    comments = models.TextField(max_length=1000, help_text='Enter comment if required', null=True, blank=True)
    date_created = models.DateField(auto_now_add=True)
    date_delivered = models.DateField("Date Completed", help_text='Enter date requisition was received (YYYY-MM-DD)', null=True, blank=True)

    CONDITION = (
        ('N/a', 'N/A'),
        ('Room Temp', 'ROOM TEMP'),
        ('Frozen', 'FROZEN'),
        ('Cold Block', 'COLD BLOCK'),
    )
    qc_status = models.CharField('Condition Received', max_length=24, choices=CONDITION, default='N/a')
    lot_id = models.CharField('Lot Number', max_length=20, help_text='Enter Lot Number of product upon delivery', null=True, blank=True)
    expiry_date = models.DateField('Expiry Date', help_text='Enter expiry date of Lot (YYYY-MM-DD)', null=True, blank=True)

    @property
    def order_created(self):
        if self.order_status == "Order Created":
            return True
        return False

    @property
    def order_sent(self):
        if self.order_status == "Order Sent":
            return True
        return False

    @property
    def order_preceived(self):
        if self.order_status == "Part Received":
            return True
        return False

    @property
    def order_complete(self):
        if self.order_status == "Complete":
            return True
        return False

    class Meta:
        permissions = (("can_create_new_order", "Able to Create New Order" ), ("can_update_order", "Able to Update Order"), ("can_delete_order", "Able to Delete Order"),)
        ordering = ["-id"]

    def save(self, *args, **kwargs):
        if(self.quantity > 0):
            super(Order, self).save(*args, **kwargs)
        else:
            raise Exception("An order cannot be created for less than 1 product")

    def __str__(self):
        """String for representing the Model object."""
        return f'({self.id}) {self.product_type.name}'

    def get_absolute_url(self):
        """Returns the url to access a detail record for this object."""
        return reverse('order-detail', args=[str(self.id)])

class Requisition(models.Model):
    """Model representing a collection of orders from a single supplier"""
    req_ref = models.CharField('Requisition Reference EROS', max_length=20, help_text='Enter EROS reference number for requisition', null=True, blank=True)
    date_created = models.DateField(auto_now_add=True)
    date_sent = models.DateField(help_text='Enter date requisition was sent for order (YYYY-MM-DD)', null=True, blank=True)

    STATUS = (
        ('To Order', 'TO ORDER'),
        ('Sent', 'SENT'),
    )
    requisition_status = models.CharField(max_length=24, choices=STATUS, default='To Order')

    comments = models.TextField(max_length=1000, help_text='Enter comment if required', null=True, blank=True)

    @property
    def req_order(self):
        if self.requisition_status == "To Order":
            return True
        return False

    @property
    def req_sent(self):
        if self.requisition_status == "Sent":
            return True
        return False

    class Meta:
        permissions = (
            ("can_create_new_requisition", "Able to Create New Requisition" ),
            ("can_update_requisition", "Able to Update Requisition"),
            ("can_delete_requisition", "Able to Delete Requisition"),
            ("can_update_requisition_authoriser", "Able to Update Requisition - Authoriser"),
        )
        ordering=["-id"]


    def __str__(self):
        """String for representing the Model object."""
        # return f'({self.id}) {self.req_ref} - {self.requisition_status}'
        return str(self.id)

    def get_absolute_url(self):
        """Returns the url to access a detail record for this object."""
        return reverse('requisition-detail', args=[str(self.id)])

    # Fields to add - user id, authorizer id, total price of req, attachments,
