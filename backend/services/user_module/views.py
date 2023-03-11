from django.shortcuts import render, redirect

from django.contrib.auth import authenticate, login

from services.user_module.forms import RegistrationForm, AuthForm

from django.contrib.auth import get_user_model

from settings import SITE_URL

User = get_user_model()


def registration(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            user = User.objects.create_user(email=form.data['email'],
                                            username=form.data['username'],
                                            password=form.data['password'],)

            user.first_name = form.data['first_name']
            user.last_name = form.data['last_name']

            user.save()

            return redirect('auth')
        else:
            return render(request, 'registration.html', context={'form': form})


def auth(request):
    if request.method == 'POST':
        form = AuthForm(request.POST)
        if form.is_valid():
            user = authenticate(username=form.data['username'],
                                password=form.data['password'])
            if user is not None:
                login(request, user)
                return redirect('index')
            else:

                return render(request, 'auth.html', context={'form': form, 'SITE_URL': SITE_URL})
    else:
        form = AuthForm()
        return render(request, 'auth.html', context={'form': form, 'SITE_URL': SITE_URL)