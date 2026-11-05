from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect, render

from accounts.forms import LoginForm, RegistrationForm, ProfileForm


def register_view(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)

        if form.is_valid():
            user = form.save()
            login(request, user)

            return redirect('product:home')

    else:
        form = RegistrationForm()

    context = {
        'form': form
    }

    return render(request, 'register.html', context)


def login_view(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)

        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')

            user = authenticate(username=username, password=password)

            if user is not None:
                login(request, user)

                return redirect('product:home')

    else:
        form = LoginForm()

    context = {
        'form': form
    }

    return render(request, 'login.html', context)


@login_required
def logout_view(request):
    logout(request)
    return redirect('product:home')


@login_required
def profile_view(request):
    user = request.user
    if request.method == 'POST':
        form = ProfileForm(request.POST, request.FILES, instance=user)
        if form.is_valid():
            form.save()
            return redirect('accounts:profile')
    else:
        form = ProfileForm(instance=user)

    context = {
        'user': user,
        'form': form,
    }

    return render(request, 'profile.html', context)


