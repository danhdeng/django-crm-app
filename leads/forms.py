from django import forms
from .models import Lead, User

from django.contrib.auth.forms import UserCreationForm

class UserForm(UserCreationForm):
    class Meta:
        model = User
        fields = (
            'username',
            'password1',
            'password2')
class LeadModelForm(forms.ModelForm):
    class Meta:
        model=Lead
        fields =(
            'first_name',
            'last_name',
            'age',
            'agent'
        )
        
class LeadForm(forms.Form):
    first_name =forms.CharField()
    last_name = forms.CharField()
    age = forms.IntegerField(min_value=0)
