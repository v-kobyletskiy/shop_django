from django import forms

class CreateOrderForm(forms.Form):
    first_name = forms.CharField(
        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'First Name'})
    )
    last_name = forms.CharField(
        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Last Name'})
    )
    phone_number = forms.CharField(
        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Phone Number'})
    )
    requires_delivery = forms.ChoiceField(
        widget=forms.RadioSelect(),
        choices=[('0', False), ('1', True)],
        initial=0,
    )
    delivery_address = forms.CharField(
        widget=forms.Textarea(attrs={
            'class': 'form-control',
            'id': 'delivery-address',
            'rows': 2,
            'placeholder': 'Delivery Address'})
    )
    payment_on_get = forms.ChoiceField(
        widget=forms.RadioSelect(),
        choices=[('0', False), ('1', True)],
        initial='card',
    )
