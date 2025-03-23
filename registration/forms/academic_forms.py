from django.forms import ModelForm
from django import forms
from django_select2.forms import Select2Widget
from ..models import *


class DepartmentsForm(ModelForm):
    unit = forms.ModelChoiceField(
        queryset=Unit.objects.all().order_by('name'),
        widget=Select2Widget,
        label="Faculty/School")

    class Meta:
        fields = ('name', 'abb', 'unit')
        model = Department


class ProgrammeForm(ModelForm):
    department = forms.ModelChoiceField(
        queryset=Department.objects.all().order_by('name'),
        widget=Select2Widget(attrs={'class': 'form-control select2'}),
        label="Department")

    level = forms.ModelChoiceField(
        queryset=Level.objects.all().order_by('name'),
        widget=Select2Widget(attrs={'class': 'form-control select2'}),
        label="Level")

    duration = forms.ChoiceField(
        choices=Programme.DURATION,
        widget=Select2Widget(attrs={'class': 'form-control select2'}),
        label="Level"
    )
    class Meta:
        fields = ('name', 'abb', 'level', 'duration', 'department')
        model = Programme


class UnitForm(ModelForm):
    name = forms.CharField(
        label="Unit name",
        required=True
    )

    class Meta:
        fields = ('name', 'abb')
        model = Unit


class YearForm(ModelForm):
    name = forms.CharField(
        widget=forms.TextInput(
            attrs={
                'placeholder': 'YYYY/YYYY'
            }
        ),
        label="Year name"
    )

    class Meta:
        fields = ('name',)
        model = Year


class SemesterForm(forms.ModelForm):
    year = forms.ModelChoiceField(
        queryset=Year.objects.all().order_by('name'),
        widget=Select2Widget(attrs={'class': 'form-control select2'}),
        label="Years"
    )
    class Meta:
        fields = ('name', 'year')
        model = Semester

