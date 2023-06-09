from django import forms
from django.contrib.auth import get_user_model


User = get_user_model()


class RegistrationForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ('first_name', 'last_name', 'email', 'username', 'password')


class AuthForm(forms.Form):
    class Meta:
        fields = ('username', 'password')