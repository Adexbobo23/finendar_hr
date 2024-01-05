from django.db import models
from django.conf import settings

class UserProfile(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    current_job_place = models.CharField(max_length=255)
    designation = models.CharField(max_length=255)
    year_of_experience = models.CharField(max_length=10)
    qualification = models.CharField(max_length=255)
    email = models.EmailField()
    phone_number = models.CharField(max_length=20)
    website_link = models.URLField()
    language = models.CharField(max_length=255)
    career_objective = models.TextField()

    # Social Links
    facebook = models.URLField()
    twitter = models.URLField()
    linkedin = models.URLField()
    pinterest = models.URLField()
    dribbble = models.URLField()
    behance = models.URLField()

    # Personal Information
    father_name = models.CharField(max_length=255)
    mother_name = models.CharField(max_length=255)
    national_id = models.CharField(max_length=20)
    present_address = models.CharField(max_length=255)
    permanent_address = models.CharField(max_length=255)
    marital_status = models.CharField(max_length=20)
    gender = models.CharField(max_length=20)
    religion = models.CharField(max_length=255)
    blood_group = models.CharField(max_length=5)
    height = models.CharField(max_length=10)
    weight = models.CharField(max_length=10)

    # Education
    education_level = models.CharField(max_length=255)
    major = models.CharField(max_length=255)
    institute = models.CharField(max_length=255)
    result_gpa = models.CharField(max_length=10)
    starting_period_education = models.DateField()
    ending_period_education = models.DateField()

    # Employment
    company_name = models.CharField(max_length=255)
    designation_employment = models.CharField(max_length=255)
    starting_period_employment = models.DateField()
    ending_period_employment = models.DateField()
    responsibility = models.TextField()

    def __str__(self):
        return f"{self.first_name} {self.last_name}"
