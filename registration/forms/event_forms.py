from django.forms import ModelForm
from django import forms
from django_select2.forms import Select2Widget
from ..models import *


class EventForm(ModelForm):
    class Meta:
        model = Event
        fields = ['title', 'description', 'location', 'projection', 'committee_amount', 'member_amount',
                  'event_date', 'start_time', 'end_time']
        widgets = {
            'description': forms.TextInput(attrs={'rows': '10'}),
            'event_date': forms.DateInput(attrs={'type': 'date'}),
            'start_time': forms.TimeInput(attrs={'type': 'time'}),
            'end_time': forms.TimeInput(attrs={'type': 'time'}),
        }


class EventPaymentForm(forms.Form):
    amount = forms.DecimalField(max_digits=10, decimal_places=2, min_value=0)
    method = forms.ChoiceField(
        choices=EventCollection.METHOD,
        widget=Select2Widget(attrs={'class': 'form-control select2'}),
        label="Method"
    )


class EventCommitteeForm(ModelForm):
    student = forms.ModelChoiceField(
        queryset=Student.objects.all(),
        widget=Select2Widget(attrs={'class': 'form-control select2'}),
    )

    position = forms.ModelChoiceField(
        queryset=Position.objects.all(),
        widget=Select2Widget(attrs={'class': 'form-control select2'}),
    )

    class Meta:
        model = EventCommittee
        fields = ['student', 'position']

