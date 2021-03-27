from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth import get_user_model

from accounts.forms import LoginForm, SignUpForm

USER = get_user_model()


# Create your views here.
def login_view(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            user = authenticate(username=form.cleaned_data['username'], password=form.cleaned_data['password'])
            if user:
                login(request, user)
                return redirect('/accounts/profile')
            else:
                print('Auth Credential is not found.')
    elif request.method == 'GET':
        if request.user.is_authenticated:
            return redirect('/accounts/profile')
        form = LoginForm()

    return render(request, 'accounts/login.html', {'form': form})


@login_required(login_url='/accounts/login')
def profile_view(request):
    return render(request, 'accounts/profile.html')


def logout_view(request):
    logout(request)
    return redirect('/accounts/login/')


def signup_view(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            user = USER(username=form.cleaned_data['username'],
                        first_name=form.cleaned_data['first_name'],
                        last_name=form.cleaned_data['last_name'])
            user.save()
            user.set_password(form.cleaned_data['password'])
            user.save()
        return redirect('/accounts/login')

    elif request.method == 'GET':
        print('this is get signup')
        form = SignUpForm()
    return render(request, 'accounts/signup.html', {'form': form})
