from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .forms import UserProfileForm
from .models import UserProfile

# Create your views here.

@login_required(login_url='login')
def participant_dasboard(request):
    user = request.user
    user_profile = UserProfile.objects.get(user=user)

    return render(request, 'preview/dashboard.html', {'user_profile': user_profile})


@login_required(login_url='login')
def edit_user_profile(request):
    if request.method == 'POST':
        form = UserProfileForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Profile updated successfully!')
            return redirect('dashboard')
    else:
        form = UserProfileForm()

    return render(request, 'preview/edit-profile.html', {'form': form})


def myprofile(request):
    # Assuming the user is logged in
    user = request.user
    user_profile = UserProfile.objects.get(user=user)

    return render(request, 'preview/my-profile.html', {'user_profile': user_profile})