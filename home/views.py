from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from .forms import RegistrationForm
from django.contrib.auth.decorators import login_required
from .models import Property
import os


def login_view(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('home')
        else:
            error_message = "Invalid login credentials"
            return render(request, 'registration/login.html', {'error_message': error_message})
    return render(request, 'registration/login.html')


def logout_view(request):
    logout(request)
    return redirect('login')


def register_view(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('login')
    else:
        form = RegistrationForm()
    return render(request, 'registration/registration.html', {'form': form})

def home_view(request):
    # if not request.user.is_authenticated:
    #     return redirect('login')

    properties = Property.objects.all()


    context = {
        'properties': properties,
    }

    print(context)

    return render(request, 'home.html', context)
