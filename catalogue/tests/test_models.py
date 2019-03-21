from django.test import TestCase

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

    def test_agent_label(self):
        supplier=Supplier.objects.get(id=1)
        field_label = supplier._meta.get_field('agent').verbose_name
        self.assertEquals(field_label, 'agent')

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

    def test_agent_max_length(self):
        supplier = Supplier.objects.get(id=1)
        max_length = supplier._meta.get_field('agent').max_length
        self.assertEquals(max_length, 200)

    def test_object_name(self):
        supplier = Supplier.objects.get(id=1)
        expected_object_name = f'{supplier.name}'
        self.assertEquals(expected_object_name, str(supplier))

    def test_get_absolute_url(self):
        supplier = Supplier.objects.get(id=1)
        # This will also fail if the urlconf is not defined.
        self.assertEquals(supplier.get_absolute_url(), '/catalogue/supplier/1')

class TemperatureModelTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        # Set up non-modified objects used by all test methods
        Temperature.objects.create(name='test temperature range')

    def test_name_label(self):
        temperature = Temperature.objects.get(id=1)
        field_label = temperature._meta.get_field('name').verbose_name
        self.assertEquals(field_label, 'name')

    def test_minimum_label(self):
        temperature = Temperature.objects.get(id=1)
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
        max_length = temperature._meta.get_field('minimum').max_length
        self.assertEquals(max_digits, 6)

    def test_maximum_max_digits(self):
        temperature = Temperature.objects.get(id=1)
        max_length = temperature._meta.get_field('maximum').max_length
        self.assertEquals(max_digits, 6)

    def test_object_name(self):
        temperature = Temperature.objects.get(id=1)
        expected_object_name = f'{temperature.name}'
        self.assertEquals(expected_object_name, str(temperature))

    def test_get_absolute_url(self):
        temperature = Temperature.objects.get(id=1)
        # This will also fail if the urlconf is not defined.
        self.assertEquals(temperature.get_absolute_url(), '/catalogue/temperature/1')
