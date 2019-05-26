# -*- coding: utf-8 -*-

from django import forms
from .models import UserModel

class SignUpForm(forms.ModelForm):
    class Meta:
        model = UserModel
        fields = ['email', 'username', 'name', 'password']