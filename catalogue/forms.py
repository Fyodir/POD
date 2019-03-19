from django import forms
from django.core.exceptions import ValidationError
from django.utils.translation import ugettext_lazy as _
from catalogue.models import Order
from django.forms import ModelForm
from django.contrib.auth.models import User
from catalogue.models import *


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

class OrderForm(forms.ModelForm):

    # Orders can only be placed on Requisitions with a stustus of "Incomplete, To Order"
    def __init__(self, *args, **kwargs):
        super(OrderForm, self).__init__(*args, **kwargs)
        self.fields['requisition_id'].queryset = Requisition.objects.filter(requisition_status="To Order")

    class Meta:
        model = Order
        exclude = ["orderer",]
