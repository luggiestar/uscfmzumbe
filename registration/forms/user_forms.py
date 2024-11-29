from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django import forms
from ..models import User
from django_select2.forms import Select2Widget


class CustomUserCreationForm(UserCreationForm):
    class Meta:
        model = User
        fields = ('username',)


class CustomUserChangeForm(UserChangeForm):
    class Meta:
        model = User
        fields = ('username',)


class ChangePasswordForm(forms.Form):
    current_password = forms.CharField(
        widget=forms.PasswordInput(),
        label='Current Password'
    )

    new_password = forms.CharField(
        widget=forms.PasswordInput(),
        label='New Password'
    )

    confirm_password = forms.CharField(
        widget=forms.PasswordInput(),
        label='Confirm Password'
    )


class UserForm(forms.ModelForm):
    email = forms.EmailField(
        required=False,
        help_text='**Leave blank if student does not have email**'
    )

    class Meta:
        model = User
        fields = ('first_name', 'middle_name', 'last_name', 'sex', 'phone', 'email')


# class ExcomForm(forms.ModelForm):
#     leader = forms.ModelChoiceField(queryset=Student.objects.filter(level='degree', is_associate=False), widget=Select2Widget)
#     position = forms.ModelChoiceField(queryset=Position.objects.all(), widget=Select2Widget)
#     Year = forms.ModelChoiceField(queryset=Year.objects.all(), widget=Select2Widget)
#
#     class Meta:
#         model = Excom
#         fields = ('leader', 'position', 'Year')
