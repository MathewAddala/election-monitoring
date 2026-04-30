from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .forms import RegisterForm, ProfileForm


def login_view(request):
    if request.user.is_authenticated:
        return redirect('dashboard:home')
    if request.method == 'POST':
        user = authenticate(request,
                            username=request.POST['username'],
                            password=request.POST['password'])
        if user:
            login(request, user)
            messages.success(request, f'Welcome back, {user.first_name or user.username}!')
            return redirect('dashboard:home')
        messages.error(request, 'Invalid credentials. Please try again.')
    return render(request, 'accounts/login.html')


def logout_view(request):
    logout(request)
    return redirect('accounts:login')


def register_view(request):
    form = RegisterForm(request.POST or None)
    if form.is_valid():
        form.save()
        messages.success(request, 'Account created! Please log in.')
        return redirect('accounts:login')
    return render(request, 'accounts/register.html', {'form': form})


@login_required
def profile_view(request):
    form = ProfileForm(request.POST or None, request.FILES or None, instance=request.user)
    if form.is_valid():
        form.save()
        messages.success(request, 'Profile updated.')
        return redirect('accounts:profile')
    return render(request, 'accounts/profile.html', {'form': form})