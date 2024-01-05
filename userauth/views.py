from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate, logout
from .forms import ParticipantRegistrationForm, CompanyRegistrationForm
from django.contrib import messages
from django.contrib.auth.forms import AuthenticationForm

# Create your views here.

def index(request):
    return render(request, 'preview/index.html')

# All Registration 
def register_participant(request):
    if request.method == 'POST':
        form = ParticipantRegistrationForm(request.POST)
        if form.is_valid():
            user = form.save()
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
            login(request, user)
            return redirect('company_dashbaord')
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


def company_login(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(request, username=username, password=password)
            print(user)  # Add this line to print the user
            if user is not None:
                if hasattr(user, 'company'):
                    login(request, user)
                    messages.success(request, f"Welcome, {user.username}!")
                    return redirect('company_dashboard')
                else:
                    messages.error(request, "User is not a company.")
            else:
                print("Authentication failed for user:", username)
                messages.error(request, "Invalid username or password.")
        else:
            print("Form is not valid. Errors:", form.errors)
    else:
        form = AuthenticationForm()

    return render(request, 'preview/company_login.html', {'form': form})


def logout_participant(request):
    logout(request)
    return redirect('index')