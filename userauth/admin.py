from django.contrib import admin
from .models import Participant, Company

# Register your models here.
class UserAdmin(admin.ModelAdmin):
    search_fields  = ['first_name', 'last_name' ,'username', 'email']
    list_display  = ['first_name',  'last_name','username', 'email']


class CompanyUser(admin.ModelAdmin):
    search_fields  = ['first_name', 'last_name' ,'username', 'email', 'company_name', 'company_type']
    list_display  = ['first_name',  'last_name','username', 'email', 'company_name', 'company_type']


admin.site.register(Participant, UserAdmin)
admin.site.register(Company, CompanyUser)