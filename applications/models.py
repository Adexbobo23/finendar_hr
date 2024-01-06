from django.db import models

class Job(models.Model):
    FIXED_SALARY = 'fixedSalary'
    HOURLY_WAGE = 'hourlyWage'
    PROJECT_BASED = 'projectBased'

    JOB_CATEGORY_CHOICES = [
        (FIXED_SALARY, 'Fixed Salary'),
        (HOURLY_WAGE, 'Hourly Wage'),
        (PROJECT_BASED, 'Project Based'),
    ]

    job_title = models.CharField(max_length=255)
    job_category = models.CharField(max_length=20, choices=JOB_CATEGORY_CHOICES)
    vacancies = models.CharField(max_length=255, null=True, blank=True)
    salary_type = models.CharField(max_length=20, choices=[
        ('fixedPrice', 'Fixed Salary'),
        ('rangePrice', 'Salary Range'),
        ('negotiable', 'Negotiable'),
    ])
    job_fixed_price = models.CharField(max_length=20, null=True, blank=True)
    job_range_price_one = models.CharField(max_length=20, null=True, blank=True)
    job_range_price_two = models.CharField(max_length=20, null=True, blank=True)
    job_type = models.CharField(max_length=255)
    experience_level = models.CharField(max_length=255)
    job_tag = models.CharField(max_length=255)
    deadline = models.DateField()
    location = models.CharField(max_length=255, null=True, blank=True) 
    job_description = models.TextField()
    job_image = models.ImageField(upload_to='job_images/', null=True, blank=True)

    def __str__(self):
        return self.job_title
