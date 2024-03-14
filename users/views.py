from django.shortcuts import render


def login(request):

    context = {
        'title': 'Fucking shop - Authorisation',
    }
    return render(request, 'users/login.html', context)


def registration(request):

    context = {
        'title': 'Fucking shop - Registration',
    }
    return render(request, 'users/registration.html', context)


def profile(request):

    context = {
        'title': 'Fucking shop - Profile',
    }
    return render(request, 'users/profile.html', context)


def logout(request):
    ...
