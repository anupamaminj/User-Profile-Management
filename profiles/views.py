from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from .models import UserProfile
from .forms import LoginForm, UserProfileForm
import re


# Login View
def login_view(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            mobile_number = form.cleaned_data['mobile_number']
            if not re.match(r'^\d{10}$', mobile_number):
                messages.error(request, 'Invalid mobile number format.')
            elif UserProfile.objects.filter(mobile_number=mobile_number).exists():
                return redirect('profile', mobile_number=mobile_number)
            else:
                messages.error(request, 'Mobile number not found.')
    else:
        form = LoginForm()
    return render(request, 'profiles/login.html', {'form': form})

# Profile View (Display Only)
def profile_view(request, mobile_number):
    user = get_object_or_404(UserProfile, mobile_number=mobile_number)
    return render(request, 'profiles/profile.html', {'user': user})

# Update Profile View
def update_profile_view(request, mobile_number):
    user = get_object_or_404(UserProfile, mobile_number=mobile_number)
    if request.method == 'POST':
        form = UserProfileForm(request.POST, instance=user)
        if form.is_valid():
            form.save()
            messages.success(request, 'Profile updated successfully!')
            return redirect('profile', mobile_number=mobile_number)
    else:
        form = UserProfileForm(instance=user)
    return render(request, 'profiles/update_profile.html', {'form': form, 'user': user})
