from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate, logout
from .forms import ParticipantRegistrationForm, CompanyRegistrationForm
from django.contrib import messages
from django.contrib.auth.forms import AuthenticationForm
from .backend import CustomBackend
from participant.models import UserProfile

# Create your views here.

def index(request):
    return render(request, 'preview/index.html')

# All Registration 
def register_participant(request):
    if request.method == 'POST':
        form = ParticipantRegistrationForm(request.POST)
        if form.is_valid():
            user = form.save()

            # Create UserProfile for the user
            UserProfile.objects.create(user=user)

            login(request, user)
            return redirect('dashboard')
    else:
        form = ParticipantRegistrationForm()
    return render(request, 'preview/register.html', {'form': form})


def register_company(request):
    if request.method == 'POST':
        form = CompanyRegistrationForm(request.POST)
        if form.is_valid():
            user = form.save()
            
            # Explicitly set the authentication backend
            user.backend = 'django.contrib.auth.backends.ModelBackend'
            
            login(request, user)
            return redirect('company_dashboard')
    else:
        form = CompanyRegistrationForm()
    return render(request, 'preview/company-register.html', {'form': form})


# All Login
def login_participant(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username') 
            password = form.cleaned_data.get('password')
            user = authenticate(request, username=username, password=password)

            if user is not None:
                login(request, user)
                messages.success(request, f"Welcome, {user.username}!")
                return redirect('dashboard')
            else:
                messages.error(request, "Invalid email or password.")
    else:
        form = AuthenticationForm()

    return render(request, 'preview/login.html', {'form': form})



# views.py
from django.contrib.auth import authenticate, login
from django.contrib import messages
from django.shortcuts import render, redirect
from django.contrib.auth.forms import AuthenticationForm
from .forms import CompanyAuthenticationForm

def company_login(request):
    if request.method == 'POST':
        form = CompanyAuthenticationForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(request, username=username, password=password)

            if user is not None:
                if hasattr(user, 'company'):
                    login(request, user)
                    messages.success(request, f"Welcome, {user.username}!")
                    return redirect('company_dashboard')
                else:
                    messages.error(request, "User is not a company.")
            else:
                messages.error(request, "Invalid username or password.")
        else:
            messages.error(request, "Form is not valid.")
    else:
        form = CompanyAuthenticationForm()

    return render(request, 'preview/company_login.html', {'form': form})




def logout_participant(request):
    logout(request)
    return redirect('index')