from django.urls import path
from .views import ( 
    participant_dasboard, edit_user_profile, myprofile
)

urlpatterns = [
    path('', participant_dasboard, name='dashboard'),
    path('edit-profile/', edit_user_profile, name='edit_profile'),
    path('myprofile/', myprofile, name='myprofile'),
]
