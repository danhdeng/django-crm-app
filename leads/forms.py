from django import forms
from .models import Lead, User,SalesPerson,Category

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
            'agent',
            'email',
            'phone_number',
            'description',
        )
        
class LeadForm(forms.Form):
    first_name =forms.CharField()
    last_name = forms.CharField()
    age = forms.IntegerField(min_value=0)
    
    
class AssignAgentForm(forms.Form):
    agent = forms.ModelChoiceField(queryset=SalesPerson.objects.none())
    
    def __init__(self, *args, **kwargs):
        request=kwargs.pop('request')
        user=request.user
        agents=SalesPerson.objects.filter(organization=request.user.userprofile)
        super(AssignAgentForm, self).__init__(*args, **kwargs)
        self.fields["agent"].queryset=agents
        
        
class LeadCategoryUpdateForm(forms.ModelForm):
    class Meta:
        model=Lead
        fields =('category',)