from django import forms
from django_select2.forms import Select2Widget
from ..models import Bill, StudentBillPayment


class BillForm(forms.ModelForm):

    class Meta:
        fields = ('amount', )
        model = Bill


class StudentPaymentForm(forms.Form):
    amount = forms.DecimalField(max_digits=10, decimal_places=2, min_value=0)
    method = forms.ChoiceField(
        choices=StudentBillPayment.METHOD,
        widget=Select2Widget(attrs={'class': 'form-control select2'}),
        label="Method"
    )