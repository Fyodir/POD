from django import forms
from django.core.exceptions import ValidationError
from django.utils.translation import ugettext_lazy as _
from catalogue.models import Order
from django.forms import ModelForm

# Updates product instnance stock_level
class UpdateProductInstanceStockForm(forms.Form):
    stock_level = forms.IntegerField(help_text='Enter current stock')

    def clean_stock_level(self):
        data = self.cleaned_data['stock_level']

        # Check if stock level is entered as lower than 0.
        if data < 0:
            raise ValidationError(_('Invalid stock level - cannot be less than 0'))

        # Remember to always return the cleaned data.
        return data


# IN PROGRESS - form for creating orders for product instances
'''
class OrderModelForm(ModelForm):
    def clean_due_back(self):
       product_type_data = self.cleaned_data['product_type']

       # Check if a date is not in the past.
       if data < datetime.date.today():
           raise ValidationError(_('Invalid date - renewal in past'))

       # Check if a date is in the allowed range (+4 weeks from today).
       if data > datetime.date.today() + datetime.timedelta(weeks=4):
           raise ValidationError(_('Invalid date - renewal more than 4 weeks ahead'))

       # Remember to always return the cleaned data.
       return data

    class Meta:
        model = Order
        fields = ['__all__']

'''
