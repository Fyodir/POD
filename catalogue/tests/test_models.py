from django.test import TestCase
import random

from catalogue.models import *

class TeamModelTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        # Set up non-modified objects used by all test methods
        Team.objects.create(name='Laboratory Team Alpha')

    def test_name_label(self):
        team = Team.objects.get(id=1)
        field_label = team._meta.get_field('name').verbose_name
        self.assertEquals(field_label, 'name')

    def test_name_max_length(self):
        team = Team.objects.get(id=1)
        max_length = team._meta.get_field('name').max_length
        self.assertEquals(max_length, 200)

    def test_object_name(self):
        team = Team.objects.get(id=1)
        expected_object_name = f'{team.name}'
        self.assertEquals(expected_object_name, str(team))

    def test_get_absolute_url(self):
        team = Team.objects.get(id=1)
        # This will also fail if the urlconf is not defined.
        self.assertEquals(team.get_absolute_url(), '/catalogue/team/1')

####################################################################

class SupplierModelTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        # Set up non-modified objects used by all test methods
        Supplier.objects.create(name='Illumina')

    def test_name_label(self):
        supplier = Supplier.objects.get(id=1)
        field_label = supplier._meta.get_field('name').verbose_name
        self.assertEquals(field_label, 'name')

    def test_phone_label(self):
        supplier=Supplier.objects.get(id=1)
        field_label = supplier._meta.get_field('phone').verbose_name
        self.assertEquals(field_label, 'phone')

    def test_email_label(self):
        supplier = Supplier.objects.get(id=1)
        field_label = supplier._meta.get_field('email').verbose_name
        self.assertEquals(field_label, 'email')

    def test_address_label(self):
        supplier=Supplier.objects.get(id=1)
        field_label = supplier._meta.get_field('address').verbose_name
        self.assertEquals(field_label, 'address')

    def test_comments_label(self):
        supplier=Supplier.objects.get(id=1)
        field_label = supplier._meta.get_field('comments').verbose_name
        self.assertEquals(field_label, 'comments')

    def test_name_max_length(self):
        supplier = Supplier.objects.get(id=1)
        max_length = supplier._meta.get_field('name').max_length
        self.assertEquals(max_length, 200)

    def test_phone_max_length(self):
        supplier = Supplier.objects.get(id=1)
        max_length = supplier._meta.get_field('phone').max_length
        self.assertEquals(max_length, 50)

    def test_email_max_length(self):
        supplier = Supplier.objects.get(id=1)
        max_length = supplier._meta.get_field('email').max_length
        self.assertEquals(max_length, 50)

    def test_address_max_length(self):
        supplier = Supplier.objects.get(id=1)
        max_length = supplier._meta.get_field('address').max_length
        self.assertEquals(max_length, 200)

    def test_comments_max_length(self):
        supplier = Supplier.objects.get(id=1)
        max_length = supplier._meta.get_field('comments').max_length
        self.assertEquals(max_length, 200)

    def test_object_name(self):
        supplier = Supplier.objects.get(id=1)
        expected_object_name = f'{supplier.name}'
        self.assertEquals(expected_object_name, str(supplier))

    def test_get_absolute_url(self):
        supplier = Supplier.objects.get(id=1)
        # This will also fail if the urlconf is not defined.
        self.assertEquals(supplier.get_absolute_url(), '/catalogue/supplier/1')

####################################################################

class ProductTypeModelTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        # Set up non-modified objects used by all test methods
        ProductType.objects.create(name='Illumina', price=36.00),

    def test_name_label(self):
        productype = ProductType.objects.get(id=1)
        field_label = productype._meta.get_field('name').verbose_name
        self.assertEquals(field_label, 'name')

    def test_supplier_label(self):
        productype=ProductType.objects.get(id=1)
        field_label = productype._meta.get_field('supplier').verbose_name
        self.assertEquals(field_label, 'supplier')

    def test_description_label(self):
        productype = ProductType.objects.get(id=1)
        field_label = productype._meta.get_field('description').verbose_name
        self.assertEquals(field_label, 'description')

    def test_product_EROS_label(self):
        productype=ProductType.objects.get(id=1)
        field_label = productype._meta.get_field('product_EROS').verbose_name
        self.assertEquals(field_label, 'Product EROS')

    def test_price_label(self):
        productype=ProductType.objects.get(id=1)
        field_label = productype._meta.get_field('price').verbose_name
        self.assertEquals(field_label, 'Price (£)')

    def test_lead_time_label(self):
        productype=ProductType.objects.get(id=1)
        field_label = productype._meta.get_field('lead_time').verbose_name
        self.assertEquals(field_label, 'Lead Time (Days)')

    def test_name_max_length(self):
        productype = ProductType.objects.get(id=1)
        max_length = productype._meta.get_field('name').max_length
        self.assertEquals(max_length, 200)

        # supplier is a ForeignKey therefore is already tested in the SupplierModelTest

    def test_description_max_length(self):
        productype = ProductType.objects.get(id=1)
        max_length = productype._meta.get_field('description').max_length
        self.assertEquals(max_length, 1000)

    def test_product_EROS_max_length(self):
        productype = ProductType.objects.get(id=1)
        max_length = productype._meta.get_field('product_EROS').max_length
        self.assertEquals(max_length, 20)

    def test_price_max_digits(self):
        productype = ProductType.objects.get(id=1)
        max_digits = productype._meta.get_field('price').max_digits
        self.assertEquals(max_digits, 8)

        #lead_time is an IntegerField and therefore cannot possess a max length

    def test_object_name(self):
        productype = ProductType.objects.get(id=1)
        expected_object_name = f'{productype.supplier} - {productype.name}'
        self.assertEquals(expected_object_name, str(productype))

    def test_get_absolute_url(self):
        productype = ProductType.objects.get(id=1)
        # This will also fail if the urlconf is not defined.
        self.assertEquals(productype.get_absolute_url(), '/catalogue/producttype/1')

####################################################################

class TemperatureModelTest(TestCase):
    @classmethod
    def setUp(cls):
        # Set up non-modified objects used by all test methods
        minimum_temp = random.randint(-101,101)
        maximum_temp = minimum_temp + random.randint(1,21)
        Temperature.objects.create(
            name='Hoth',
            minimum=minimum_temp,
            maximum=maximum_temp
        )

    def test_name_label(self):
        temperature = Temperature.objects.get(id=1)
        field_label = temperature._meta.get_field('name').verbose_name
        self.assertEquals(field_label, 'name')

    def test_minimum_label(self):
        temperature=Temperature.objects.get(id=1)
        field_label = temperature._meta.get_field('minimum').verbose_name
        self.assertEquals(field_label, 'minimum')

    def test_maximum_label(self):
        temperature = Temperature.objects.get(id=1)
        field_label = temperature._meta.get_field('maximum').verbose_name
        self.assertEquals(field_label, 'maximum')

    def test_name_max_length(self):
        temperature = Temperature.objects.get(id=1)
        max_length = temperature._meta.get_field('name').max_length
        self.assertEquals(max_length, 200)

    def test_minimum_max_digits(self):
        temperature = Temperature.objects.get(id=1)
        max_digits = temperature._meta.get_field('minimum').max_digits
        self.assertEquals(max_digits, 6)

    def test_maximum_max_digits(self):
        temperature = Temperature.objects.get(id=1)
        max_digits = temperature._meta.get_field('maximum').max_digits
        self.assertEquals(max_digits, 6)

    def test_object_name(self):
        temperature = Temperature.objects.get(id=1)
        expected_object_name = f'{temperature.name}'
        self.assertEquals(expected_object_name, str(temperature))

    def test_get_absolute_url(self):
        temperature = Temperature.objects.get(id=1)
        # This will also fail if the urlconf is not defined.
        self.assertEquals(temperature.get_absolute_url(), '/catalogue/temperature/1')

        #Add test to ensure maximum test is ALWAYS higher than minimum test

####################################################################

class StorageModelTest(TestCase):
    @classmethod
    def setUp(cls):
        # Set up non-modified objects used by all test methods
        Storage.objects.create(name='Freezer A')

    def test_name_label(self):
        storage = Storage.objects.get(id=1)
        field_label = storage._meta.get_field('name').verbose_name
        self.assertEquals(field_label, 'name')

    def test_location_label(self):
        storage=Storage.objects.get(id=1)
        field_label = storage._meta.get_field('location').verbose_name
        self.assertEquals(field_label, 'location')

    def test_temp_range_label(self):
        storage = Storage.objects.get(id=1)
        field_label = storage._meta.get_field('temp_range').verbose_name
        self.assertEquals(field_label, 'temp range')

    def test_name_max_length(self):
        storage = Storage.objects.get(id=1)
        max_length = storage._meta.get_field('name').max_length
        self.assertEquals(max_length, 200)

    def test_location_max_length(self):
        storage = Storage.objects.get(id=1)
        max_length = storage._meta.get_field('location').max_length
        self.assertEquals(max_length, 200)

    # not required to test "temp_range" max length as it is a foreign key

    def test_object_name(self):
        storage = Storage.objects.get(id=1)
        expected_object_name = f'{storage.name} ({storage.location})'
        self.assertEquals(expected_object_name, str(storage))

    def test_get_absolute_url(self):
        storage = Storage.objects.get(id=1)
        # This will also fail if the urlconf is not defined.
        self.assertEquals(storage.get_absolute_url(), '/catalogue/storage/1')

####################################################################

# class ProductInstnaceModelTest(TestCase):

####################################################################

# class OrderModelTest(TestCase):

####################################################################

# class RequisitionModelTest(TestCase):

####################################################################
