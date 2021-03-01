from django import forms
from django.contrib.auth.forms import UserCreationForm
from users.models import CustomUser


class SingUpForm(UserCreationForm):
    '''
    email = forms.EmailField(max_length=254, help_text='Informe um E-mail valido.',
                             widget=forms.EmailInput(attrs={'placeholder': 'E-mail'}))
    '''
    email = forms.EmailField(max_length=254, help_text='Informe um E-mail valido.')

    class Meta:
        model = CustomUser
        fields = ('username', 'email', 'password1', 'password2',)
