from django import forms
from .choices import STATUS_CHOICES


class PaymentCreateForm(forms.Form):
    """ Form for creating payments """
    amount = forms.IntegerField(required=True)
    purpose_of_payment = forms.CharField(required=True)


class PaymentEditForm(forms.Form):
    """ Form for editing payments """
    amount = forms.IntegerField(required=True)
    purpose_of_payment = forms.CharField(required=True)
    status = forms.ChoiceField(choices=STATUS_CHOICES, required=True)
