from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from .forms import RegistrationForm
from .models import Property, PropertyImage
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

    # featured_Property = Property.objects.get(featured_property=True)
    #  images = PropertyImage.objects.filter(property_id=featured_Property.id)
    # return render(request, 'home.html', {'property': featured_Property,
    # 'images': images})
    properties = Property.objects.get(featured_property=True)

    context = {
        'properties': properties,
    }
    return render(request, 'home.html', context)


def event_view(request):
    return render(request, 'event.html')


def profile_view(request):
    return render(request, 'profile.html')
