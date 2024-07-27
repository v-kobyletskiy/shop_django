import re

from django import forms

class CreateOrderForm(forms.Form):
    first_name = forms.CharField()
    last_name = forms.CharField()
    phone_number = forms.CharField()
    requires_delivery = forms.ChoiceField(
        choices=[
            ('0', False),
            ('1', True)
        ],)
    delivery_address = forms.CharField(required=False)
    payment_on_get = forms.ChoiceField(
        choices=[
            ('0', False),
            ('1', True)
        ],)

    def clean_phone_number(self):
        phone_number = self.cleaned_data['phone_number']

        if not phone_number.isdigit():
            raise forms.ValidationError('Phone number must contain only digits')

        pattern = re.compile(r'^\d{10}$')
        if not pattern.match(phone_number):
            raise forms.ValidationError('Invalid phone number')

        return phone_number
