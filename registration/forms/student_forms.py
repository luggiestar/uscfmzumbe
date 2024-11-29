from django import forms
from ..models import User, Programme, Committee, Position
from django_select2.forms import Select2Widget


class StudentForm(forms.ModelForm):
    programme = forms.ModelChoiceField(queryset=Programme.objects.all(), widget=Select2Widget)
    committee = forms.ModelChoiceField(queryset=Committee.objects.all(), widget=Select2Widget)
    email = forms.EmailField(
        required=False,
        help_text='**Leave blank if student does not have email**'
    )

    class Meta:
        model = User
        fields = ('first_name', 'middle_name', 'last_name', 'sex', 'phone', 'email')


class CommitteeForm(forms.ModelForm):
    class Meta:
        model = Committee
        fields = ('name', 'abb')


class MessageForm(forms.Form):
    MESSAGE_FILTER_CHOICES = [
        ('', 'All members'),
        ('finalist', 'Finalist'),
        ('associate', 'Associate'),
    ]

    message = forms.CharField(
        widget=forms.Textarea(attrs={
            'class': 'form-control',
            'placeholder': 'Enter message',
            'rows': 8
        })
    )
    filter = forms.ChoiceField(
        choices=MESSAGE_FILTER_CHOICES,
        widget=Select2Widget(attrs={
            'class': 'form-control'
        })
    )



class PositionForm(forms.ModelForm):
    name = forms.CharField(
        widget=forms.TextInput(
            attrs={
                'placeholder': 'Enter valid position name'
            }
        ),
        label="Position name"
    )

    class Meta:
        fields = ('name',)
        model = Position

class StudentUploadForm(forms.Form):
    file = forms.FileField()


class SelfStudentRegistrationForm(forms.ModelForm):
    programme = forms.ModelChoiceField(queryset=Programme.objects.all(), widget=Select2Widget)
    committee = forms.ModelChoiceField(queryset=Committee.objects.all(), widget=Select2Widget)
    email = forms.EmailField(
        required=False,
        help_text='**Leave blank if student does not have email**'
    )

    class Meta:
        model = User
        fields = ('first_name', 'middle_name', 'last_name', 'sex', 'phone', 'email')