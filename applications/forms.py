from django import forms
from .models import Job

class JobForm(forms.ModelForm):
    class Meta:
        model = Job
        fields = [
            'job_title',
            'job_category',
            'vacancies',
            'salary_type',
            'job_fixed_price',
            'job_range_price_one',
            'job_range_price_two',
            'job_type',
            'experience_level',
            'job_tag',
            'deadline',
            'location',
            'job_description',
            'job_image',
        ]

    agreed_to_terms = forms.BooleanField()

    widgets = {
        'job_title': forms.TextInput(attrs={'placeholder': 'Senior UI/UX Engineer'}),
        'vacancies': forms.TextInput(attrs={'placeholder': '07 Person'}),
        'experiences': forms.TextInput(attrs={'placeholder': 'Type Experiences'}),
        'deadline': forms.DateInput(attrs={'type': 'date'}),
    }
