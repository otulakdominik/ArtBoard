from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


class SignUpForm(UserCreationForm):
    birth_date = forms.DateField(help_text='Required. Format: YYYY-MM-DD')
    email = forms.EmailField()
    first_name = forms.CharField()
    last_name = forms.CharField()
    avatar = forms.ImageField(required=False,)
    facebook_url = forms.URLField(required=False,)

    class Meta:
        model = User
        fields = (
            'username',
            'email',
            'password1',
            'password2',
            'first_name',
            'last_name',
            'birth_date',
            'avatar',
            'facebook_url',
        )
