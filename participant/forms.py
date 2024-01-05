from django import forms
from .models import UserProfile

class UserProfileForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        fields = [
            'first_name', 'last_name', 'current_job_place', 'designation',
            'year_of_experience', 'qualification', 'email', 'phone_number',
            'website_link', 'language', 'career_objective', 'facebook',
            'twitter', 'linkedin', 'pinterest', 'dribbble', 'behance',
            'father_name', 'mother_name',  'national_id',
            'present_address', 'permanent_address', 'marital_status', 'gender',
            'religion', 'blood_group', 'height', 'weight', 'education_level',
            'major', 'institute', 'result_gpa', 'starting_period_education',
            'ending_period_education', 'company_name', 'designation_employment',
            'starting_period_employment', 'ending_period_employment',
            'responsibility'
        ]

        # Optionally, you can specify widgets or other form attributes for customization
        widgets = {
            'starting_period_education': forms.DateInput(attrs={'type': 'date'}),
            'ending_period_education': forms.DateInput(attrs={'type': 'date'}),
            'starting_period_employment': forms.DateInput(attrs={'type': 'date'}),
            'ending_period_employment': forms.DateInput(attrs={'type': 'date'}),
        }

    def __init__(self, *args, **kwargs):
        super(UserProfileForm, self).__init__(*args, **kwargs)

        # Make all fields not required
        for field in self.fields:
            self.fields[field].required = False
