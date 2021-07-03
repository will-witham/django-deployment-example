from django.shortcuts import render, redirect
from basic_app.forms import UserForm,UserProfileInfoForm
from django.contrib import messages

from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponseRedirect, HttpResponse
from django.urls import reverse
from django.contrib.auth.decorators import login_required

# Create your views here.

def index(request):
    return render(request, 'basic_app/index.html')

@login_required
def user_logout(request):
    logout(request)
    return HttpResponseRedirect(reverse('index'))
    messages.success(request,'You have been logged out')

@login_required
def special(request):
    return render(request, 'basic_app/special.html')    

def register(request):
    registered = False

    if request.method == 'POST':
        print('chugga_chugga')
        user_form = UserForm(request.POST)
        profile_form = UserProfileInfoForm(request.POST)
        print('get up')
        if user_form.is_valid() and profile_form.is_valid():
            print('good to go cobba')
            user = user_form.save()
            user.set_password(user.password)
            user.save()
            messages.success(request,f'Acccount Created for {user.username}')
            profile = profile_form.save(commit=False)
            profile.user = user

            if 'profile_pic' in request.FILES:
                profile.profile_pic = request.FILES['profile_pic']

            profile.save()
            registered = True
        else:
            print(user_form.errors,profile_form.errors)
            print('fark')
    else:
        user_form = UserForm()
        profile_form = UserProfileInfoForm()

    return render(request, 'basic_app/registration.html',
                                    {'user_form':user_form,
                                    'profile_form':profile_form,
                                    'registered':registered})
def user_login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(username=username,password=password)
        if user:
            if user.is_active:
                login(request,user)
                return HttpResponseRedirect(reverse('index'))
                messages.success(request,'You are logged in')
            else:
                # return HttpResponse('Account Not Active')
                messages.warning(request,'Account not Active')
                return HttpResponseRedirect(reverse('user_login'))
        else:
            print('Someone tried to login and failed')
            print(f'Username: {username} and password {password}')
            messages.warning(request,'Invalid login details')
            return HttpResponseRedirect(reverse('user_login'))
    else:
        return render(request, 'basic_app/login.html')
