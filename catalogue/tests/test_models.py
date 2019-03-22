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
        producttype = ProductType.objects.get(id=1)
        field_label = producttype._meta.get_field('name').verbose_name
        self.assertEquals(field_label, 'name')

    def test_supplier_label(self):
        producttype=ProductType.objects.get(id=1)
        field_label = producttype._meta.get_field('supplier').verbose_name
        self.assertEquals(field_label, 'supplier')

    def test_description_label(self):
        producttype = ProductType.objects.get(id=1)
        field_label = producttype._meta.get_field('description').verbose_name
        self.assertEquals(field_label, 'description')

    def test_product_EROS_label(self):
        producttype=ProductType.objects.get(id=1)
        field_label = producttype._meta.get_field('product_EROS').verbose_name
        self.assertEquals(field_label, 'Product EROS')

    def test_price_label(self):
        producttype=ProductType.objects.get(id=1)
        field_label = producttype._meta.get_field('price').verbose_name
        self.assertEquals(field_label, 'Price (£)')

    def test_lead_time_label(self):
        producttype=ProductType.objects.get(id=1)
        field_label = producttype._meta.get_field('lead_time').verbose_name
        self.assertEquals(field_label, 'Lead Time (Days)')

    def test_name_max_length(self):
        producttype = ProductType.objects.get(id=1)
        max_length = producttype._meta.get_field('name').max_length
        self.assertEquals(max_length, 200)

        # supplier is a ForeignKey therefore is already tested in the SupplierModelTest

    def test_description_max_length(self):
        producttype = ProductType.objects.get(id=1)
        max_length = producttype._meta.get_field('description').max_length
        self.assertEquals(max_length, 1000)

    def test_product_EROS_max_length(self):
        producttype = ProductType.objects.get(id=1)
        max_length = producttype._meta.get_field('product_EROS').max_length
        self.assertEquals(max_length, 20)

    def test_price_max_digits(self):
        producttype = ProductType.objects.get(id=1)
        max_digits = producttype._meta.get_field('price').max_digits
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

class ProductInstanceModelTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        # Set up non-modified objects used by all test methods
        ProductInstance.objects.create(
            id='90ec5d20-13a2-481e-8e76-ed3675bfce40',
            product_type=ProductType.objects.create(name='Darth Vader Mask', price=300.00),
            stock=12,
            minimum_stock = 10,
            )

    def test_product_type_label(self):
        productinstance = ProductInstance.objects.get(id='90ec5d20-13a2-481e-8e76-ed3675bfce40')
        field_label = productinstance._meta.get_field('product_type').verbose_name
        self.assertEquals(field_label, 'Product')

    def test_id_label(self):
        productinstance=ProductInstance.objects.get(id='90ec5d20-13a2-481e-8e76-ed3675bfce40')
        field_label = productinstance._meta.get_field('id').verbose_name
        self.assertEquals(field_label, 'id')

    def test_team_label(self):
        productinstance = ProductInstance.objects.get(id='90ec5d20-13a2-481e-8e76-ed3675bfce40')
        field_label = productinstance._meta.get_field('team').verbose_name
        self.assertEquals(field_label, 'team')

    def test_storage_label(self):
        productinstance=ProductInstance.objects.get(id='90ec5d20-13a2-481e-8e76-ed3675bfce40')
        field_label = productinstance._meta.get_field('storage').verbose_name
        self.assertEquals(field_label, 'storage')

    def test_stock_label(self):
        productinstance=ProductInstance.objects.get(id='90ec5d20-13a2-481e-8e76-ed3675bfce40')
        field_label = productinstance._meta.get_field('stock').verbose_name
        self.assertEquals(field_label, 'Current Stock')

    def test_minimum_stock_label(self):
        productinstance=ProductInstance.objects.get(id='90ec5d20-13a2-481e-8e76-ed3675bfce40')
        field_label = productinstance._meta.get_field('minimum_stock').verbose_name
        self.assertEquals(field_label, 'Minimum Stock')

    def test_stock_updater_label(self):
        productinstance=ProductInstance.objects.get(id='90ec5d20-13a2-481e-8e76-ed3675bfce40')
        field_label = productinstance._meta.get_field('stock_updater').verbose_name
        self.assertEquals(field_label, 'User')

    def test_date_updated_label(self):
        productinstance=ProductInstance.objects.get(id='90ec5d20-13a2-481e-8e76-ed3675bfce40')
        field_label = productinstance._meta.get_field('date_updated').verbose_name
        self.assertEquals(field_label, 'date updated')

        # product_type is a ForeignKey therefore is already tested in the ProductTypeModelTest

        # id is an automatically generated UUIDField

        # team is a ForeignKey therefore is already tested in the TeamModelTest

        # storage is a ForeignKey therefore is already tested in the StorageModelTest

        # stock is an IntegerField therefore max length/digits cannot be tested

        # minimum_stock is an IntegerField therefore max length/digits cannot be tested

        # stock_updater is pulled from the auth.user model and will already be tested in djago framework

        # date_updated is an automatically generated field

    def test_object_name(self):
        productinstance = ProductInstance.objects.get(id='90ec5d20-13a2-481e-8e76-ed3675bfce40')
        expected_object_name = f'{productinstance.product_type.name}'
        self.assertEquals(expected_object_name, str(productinstance))

    def test_get_absolute_url(self):
        productinstance = ProductInstance.objects.get(id='90ec5d20-13a2-481e-8e76-ed3675bfce40')
        # This will also fail if the urlconf is not defined.
        self.assertEquals(productinstance.get_absolute_url(), '/catalogue/productinstance/90ec5d20-13a2-481e-8e76-ed3675bfce40')

####################################################################

# class OrderModelTest(TestCase):
class OrderModelTest(TestCase):
    @classmethod
    def setUp(cls):
        # Set up non-modified objects used by all test methods
        Order.objects.create(
            id=1,
            quantity=2,
            product_type=ProductType.objects.create(name='Light Saber', price=5999.00)
        )

    def test_team_label(self):
        order = Order.objects.get(id=1)
        field_label = order._meta.get_field('team').verbose_name
        self.assertEquals(field_label, 'team')

    def test_requisition_id_label(self):
        order=Order.objects.get(id=1)
        field_label = order._meta.get_field('requisition_id').verbose_name
        self.assertEquals(field_label, 'Requisition ID')

    def test_product_type_label(self):
        order = Order.objects.get(id=1)
        field_label = order._meta.get_field('product_type').verbose_name
        self.assertEquals(field_label, 'product type')

    def test_quantity_label(self):
        order = Order.objects.get(id=1)
        field_label = order._meta.get_field('quantity').verbose_name
        self.assertEquals(field_label, 'quantity')

    def test_urgency_label(self):
        order=Order.objects.get(id=1)
        field_label = order._meta.get_field('urgency').verbose_name
        self.assertEquals(field_label, 'urgency')

    def test_orderer_label(self):
        order = Order.objects.get(id=1)
        field_label = order._meta.get_field('orderer').verbose_name
        self.assertEquals(field_label, 'orderer')

    def test_order_issue_label(self):
        order=Order.objects.get(id=1)
        field_label = order._meta.get_field('order_issue').verbose_name
        self.assertEquals(field_label, 'order issue')

    def test_order_status_label(self):
        order = Order.objects.get(id=1)
        field_label = order._meta.get_field('order_status').verbose_name
        self.assertEquals(field_label, 'order status')

    def test_comments_label(self):
        order = Order.objects.get(id=1)
        field_label = order._meta.get_field('comments').verbose_name
        self.assertEquals(field_label, 'comments')

    def test_date_created_label(self):
        order=Order.objects.get(id=1)
        field_label = order._meta.get_field('date_created').verbose_name
        self.assertEquals(field_label, 'date created')

    def test_date_delivered_label(self):
        order = Order.objects.get(id=1)
        field_label = order._meta.get_field('date_delivered').verbose_name
        self.assertEquals(field_label, 'Date Completed')

    def test_qc_status_label(self):
        order = Order.objects.get(id=1)
        field_label = order._meta.get_field('qc_status').verbose_name
        self.assertEquals(field_label, 'Condition Received')

    def test_lot_id_label(self):
        order=Order.objects.get(id=1)
        field_label = order._meta.get_field('lot_id').verbose_name
        self.assertEquals(field_label, 'Lot Number')

    def test_expiry_date_label(self):
        order = Order.objects.get(id=1)
        field_label = order._meta.get_field('expiry_date').verbose_name
        self.assertEquals(field_label, 'expiry date')

        # team is a ForeignKey therefore is already tested in the TeamModelTest

        # requisition_id is a ForeignKey therefore is already tested in the RequisitionModelTest

        # product_type is a ForeignKey therefore is already tested in the ProductTypeModelTest

        # quantity is an IntegerField therefore max length/digits cannot be tested

    def test_urgency_max_length(self):
        order = Order.objects.get(id=1)
        max_length = order._meta.get_field('urgency').max_length
        self.assertEquals(max_length, 10)

    def test_order_issue_max_length(self):
        order = Order.objects.get(id=1)
        max_length = order._meta.get_field('order_issue').max_length
        self.assertEquals(max_length, 5)

    def test_order_status_max_length(self):
        order = Order.objects.get(id=1)
        max_length = order._meta.get_field('order_status').max_length
        self.assertEquals(max_length, 24)

    def test_comments_max_length(self):
        order = Order.objects.get(id=1)
        max_length = order._meta.get_field('comments').max_length
        self.assertEquals(max_length, 1000)

        # date_created is an automatically created DateField therefore max length/digits cannot be tested

        # date_delivered  is an DateField therefore max length/digits cannot be tested

    def test_qc_status_max_length(self):
        order = Order.objects.get(id=1)
        max_length = order._meta.get_field('qc_status').max_length
        self.assertEquals(max_length, 24)

    def test_lot_id_max_length(self):
        order = Order.objects.get(id=1)
        max_length = order._meta.get_field('lot_id').max_length
        self.assertEquals(max_length, 20)

    def test_object_name(self):
        order = Order.objects.get(id=1)
        expected_object_name = f'({order.id}) {order.product_type.name}'
        self.assertEquals(expected_object_name, str(order))

    def test_get_absolute_url(self):
        order = Order.objects.get(id=1)
        # This will also fail if the urlconf is not defined.
        self.assertEquals(order.get_absolute_url(), '/catalogue/order/1')

####################################################################

# class RequisitionModelTest(TestCase):
class RequisitionModelTest(TestCase):
    @classmethod
    def setUp(cls):
        # Set up non-modified objects used by all test methods
        Requisition.objects.create(req_ref='H4GF5D6S7A89S')

    def test_req_ref_label(self):
        requisition = Requisition.objects.get(id=1)
        field_label = requisition._meta.get_field('req_ref').verbose_name
        self.assertEquals(field_label, 'Requisition Reference EROS')

    def test_date_created_label(self):
        requisition=Requisition.objects.get(id=1)
        field_label = requisition._meta.get_field('date_created').verbose_name
        self.assertEquals(field_label, 'date created')

    def test_date_sent_label(self):
        requisition = Requisition.objects.get(id=1)
        field_label = requisition._meta.get_field('date_sent').verbose_name
        self.assertEquals(field_label, 'date sent')

    def test_requisition_status_label(self):
        requisition=Requisition.objects.get(id=1)
        field_label = requisition._meta.get_field('requisition_status').verbose_name
        self.assertEquals(field_label, 'requisition status')

    def test_comments_label(self):
        requisition = Requisition.objects.get(id=1)
        field_label = requisition._meta.get_field('comments').verbose_name
        self.assertEquals(field_label, 'comments')

    def test_req_ref_max_length(self):
        requisition = Requisition.objects.get(id=1)
        max_length = requisition._meta.get_field('req_ref').max_length
        self.assertEquals(max_length, 20)

        # date_created is an automatically created DateField therefore max length/digits cannot be tested

        # date_sent is a DateField therefore max length/digits cannot be tested

    def test_requisition_status_max_length(self):
        requisition = Requisition.objects.get(id=1)
        max_length = requisition._meta.get_field('requisition_status').max_length
        self.assertEquals(max_length, 24)

    def test_comments_max_length(self):
        requisition = Requisition.objects.get(id=1)
        max_length = requisition._meta.get_field('comments').max_length
        self.assertEquals(max_length, 1000)

    def test_object_name(self):
        requisition = Requisition.objects.get(id=1)
        expected_object_name = f'{requisition.id}'
        self.assertEquals(expected_object_name, str(requisition))

    def test_get_absolute_url(self):
        requisition = Requisition.objects.get(id=1)
        # This will also fail if the urlconf is not defined.
        self.assertEquals(requisition.get_absolute_url(), '/catalogue/requisition/1')
