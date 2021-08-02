from django import forms
from django.forms import fields
from django.contrib.auth import get_user_model

User=get_user_model()

class SalesPersonForm(forms.ModelForm):
    class Meta:
        model =User
        fields = (
            'email',
            'username',
            'first_name',
            'last_name',
        )
        
    