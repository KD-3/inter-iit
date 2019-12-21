from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import password_validation

from django.core.validators import RegexValidator


class ContractorRegisterForm(UserCreationForm):
    password1 = forms.CharField(
        label='Password',
        strip=False,
        widget=forms.PasswordInput(attrs={'class': 'form-control'}),
        help_text=password_validation.password_validators_help_text_html(),
    )
    password2 = forms.CharField(
        label='Password confirmation',
        strip=False,
        widget=forms.PasswordInput(attrs={'class': 'form-control'}),
        help_text='Enter the same password as before, for verification.',
    )
    username = forms.CharField(max_length=11, label="Username",
                               required=True)
    phone = forms.CharField(max_length=15, label="Phone")

    class Meta:
        model = User
        fields = ('username', 'password1', 'password2',)
