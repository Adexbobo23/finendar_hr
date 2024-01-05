from django.contrib.auth.models import AbstractUser, Group, Permission
from django.db import models

class Participant(AbstractUser):
    # Additional fields can be added here if needed
    agreed_to_terms = models.BooleanField(default=False)

    def __str__(self):
        return self.username

    # Add related_name arguments
    groups = models.ManyToManyField(Group, related_name='participants')
    user_permissions = models.ManyToManyField(Permission, related_name='participant_permissions')


class Company(AbstractUser):
    # Additional fields
    company_name = models.CharField(max_length=255, blank=True)
    company_type = models.CharField(max_length=255, choices=[
        ('digital_agency', 'Digital Agency'),
        ('digital_marketing_agency', 'Digital Marketing Agency'),
        ('software_company', 'Software Company'),
    ], default='digital_agency')
    agreed_to_terms = models.BooleanField(default=False)

    class Meta:
        db_table = 'company'

    # Add related_name arguments
    groups = models.ManyToManyField(Group, related_name='companies')
    user_permissions = models.ManyToManyField(Permission, related_name='company_permissions')
