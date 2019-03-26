import datetime

from django.test import TestCase
from django.utils import timezone

from catalogue.forms import UpdateProductInstanceStockForm, OrderForm

class UpdateProductInstanceStockFormTest(TestCase):
    def test_stock_level_update_field_label(self):
        form = UpdateProductInstanceStockForm()
        self.assertTrue(form.fields['stock_level'].label == None or form.fields['stock_level'].label == 'stock level')

    def test_stock_level_update_field_help_text(self):
        form = UpdateProductInstanceStockForm()
        self.assertEqual(form.fields['stock_level'].help_text, 'Enter current stock')

    def test_stock_level_not_below_zero(self):
        level = -1
        form = UpdateProductInstanceStockForm(data={'stock_level': level})
        self.assertFalse(form.is_valid())

####################################################################

# class OrderFormTest(TestCase):
class OrderFormTest(TestCase):
    def test_team_label(self):
        form = OrderForm()
        self.assertTrue(form.fields['team'].label == 'Team')

    def test_requisition_id_label(self):
        form = OrderForm()
        self.assertTrue(form.fields['requisition_id'].label == 'Requisition ID')

    def test_product_type_label(self):
        form = OrderForm()
        self.assertTrue(form.fields['product_type'].label == 'Product Type')

    def test_quantity_label(self):
        form = OrderForm()
        self.assertTrue(form.fields['quantity'].label == 'Quantity')

    def test_quantity_help_text(self):
        form = OrderForm()
        self.assertEqual(form.fields['quantity'].help_text, 'Enter required quantity')

    def test_urgency_label(self):
        form = OrderForm()
        self.assertTrue(form.fields['urgency'].label == 'Urgency')

    # def test_orderer_label(self):       # Not present in form
    #     form = OrderForm()
    #     self.assertTrue(form.fields['orderer'].label == 'orderer')

    def test_order_issue_label(self):
        form = OrderForm()
        self.assertTrue(form.fields['order_issue'].label == 'Order issue')

    def test_order_status_label(self):
        form = OrderForm()
        self.assertTrue(form.fields['order_status'].label == 'Order status')


    def test_comments_label(self):
        form = OrderForm()
        self.assertTrue(form.fields['comments'].label == 'Comments')

    def test_comments_help_text(self):
        form = OrderForm()
        self.assertEqual(form.fields['comments'].help_text, 'Enter comment if required')

    # def test_date_created_label(self):       # Not present in form
    #     form = OrderForm()
    #     self.assertTrue(form.fields['date_created'].label == 'Date Created')

    def test_date_completed_label(self):
        form = OrderForm()
        self.assertTrue(form.fields['date_delivered'].label == 'Date Completed')

    def test_date_completed_help_text(self):
        form = OrderForm()
        self.assertEqual(form.fields['date_delivered'].help_text, 'Enter date requisition was received (YYYY-MM-DD)')

    def test_qc_status_label(self):
        form = OrderForm()
        self.assertTrue(form.fields['qc_status'].label == 'Condition Received')

    def test_lot_id_label(self):
        form = OrderForm()
        self.assertTrue(form.fields['lot_id'].label == 'Lot Number')

    def test_lot_id_help_text(self):
        form = OrderForm()
        self.assertEqual(form.fields['lot_id'].help_text, 'Enter Lot Number of product upon delivery')

    def test_expiry_date_label(self):
        form = OrderForm()
        self.assertTrue(form.fields['expiry_date'].label == 'Expiry Date')

    def test_expiry_date_help_text(self):
        form = OrderForm()
        self.assertEqual(form.fields['expiry_date'].help_text, 'Enter expiry date of Lot (YYYY-MM-DD)')

####################################################################
