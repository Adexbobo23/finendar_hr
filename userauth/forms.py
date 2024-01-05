from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import get_user_model
from .models import Company

class ParticipantRegistrationForm(UserCreationForm):
    email = forms.EmailField()
    first_name = forms.CharField(max_length=30, required=True)
    last_name = forms.CharField(max_length=30, required=True)
    agreed_to_terms = forms.BooleanField()

    class Meta:
        model = get_user_model()
        fields = ['first_name', 'last_name', 'username', 'email', 'password1', 'password2', 'agreed_to_terms']



class CompanyRegistrationForm(UserCreationForm):
    first_name = forms.CharField(max_length=30, required=True)
    last_name = forms.CharField(max_length=30, required=True)
    company_name = forms.CharField(max_length=255, required=False)
    company_type = forms.ChoiceField(
        choices=[
            ('digital_agency', 'Digital Agency'),
            ('digital_marketing_agency', 'Digital Marketing Agency'),
            ('software_company', 'Software Company'),
        ],
        initial='digital_agency',
        widget=forms.Select(attrs={'class': 'select1'}),
    )
    agreed_to_terms = forms.BooleanField()

    class Meta:
        model = Company
        fields = ['first_name', 'last_name', 'username', 'email', 'password1', 'password2', 'company_name', 'company_type', 'agreed_to_terms']