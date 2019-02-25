from django import forms
from django.core.exceptions import ValidationError
from django.utils.translation import ugettext_lazy as _
from catalogue.models import Order
from django.forms import ModelForm
from django.contrib.auth.models import User


# Updates product instance stock_level
class UpdateProductInstanceStockForm(forms.Form):
    stock_level = forms.IntegerField(help_text='Enter current stock')

    def clean_stock_level(self):
        data = self.cleaned_data['stock_level']

        # Check if stock level is entered as lower than 0.
        if data < 0:
            raise ValidationError(_('Invalid stock level - cannot be less than 0'))

        # Remember to always return the cleaned data.
        return data


# IN PROGRESS - 2 versions of a form for creating orders for product instances

# class OrderModelForm(ModelForm):
#
#     class Meta:
#         model = Order
#         fields = '__all__'
#         labels = {
#             'product_type': _('Product'),
#             'requisition_id': _('Requisition ID'),
#             'quantity': _('Quantity'),
#             'date_created': _('Date order created'),
#             'orderer': _('Orderer')
#         }
#
# class OrderForm(forms.Form):
#     product_type = forms.ForeignKey('ProductType', on_delete=models.SET_NULL, null=True)
#     requisition_id = forms.ForeignKey('Requisition', on_delete=models.SET_NULL, null=True, blank=True)
#     quantity = forms.IntegerField(help_text='Enter required quantity')
#     date_created = forms.DateTimeField(auto_now_add=True)
#     orderer = forms.ForeignKey(User, on_delete=models.SET_NULL, null=True)
