from django.test import TestCase

from catalogue.models import *

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
