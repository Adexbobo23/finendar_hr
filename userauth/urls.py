from django.urls import path
from .views import ( 
    index, login_participant, register_participant,
    register_company, logout_participant, company_login
    
)

urlpatterns = [
    path('', index, name='index'),
    path('login/', login_participant, name='login'),
    path('company-login/', company_login, name='company_login'),
    path('logout/', logout_participant, name='logout'),
    path('register/', register_participant, name='register'),
    path('company-reg/', register_company, name='company-reg'),
]
