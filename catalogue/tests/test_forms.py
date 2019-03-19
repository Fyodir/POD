import datetime

from django.test import TestCase
from django.utils import timezone

from catalogue.forms import UpdateProductInstanceStockForm

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
