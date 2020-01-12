from django.shortcuts import render
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponseRedirect, HttpResponse,JsonResponse,HttpRequest
from django.urls import reverse
from django.contrib import messages,auth
from django.conf import settings
from django.contrib.auth.models import User
from .controller.UserController import UserController
from .models import *

def home(request):
    return render(request,'index.html')


# User Login
def login(request):
    if request.method == 'POST':
        username = request.POST.get('email', '')
        password = request.POST.get('pass', '')

        user = auth.authenticate(username=username, password=password)

        if user:
            if user.is_active:
                auth.login(request, user)
                return render(request,'home.html')
        else:
            messages.error(request, "User does not exist.")
            return HttpResponseRedirect(reverse('login'))
    else:
        return render(request, 'login.html')

def signup(request):
    if request.method == 'POST':
        ctrl = UserController()
        existUser = User.objects.filter(email=request.POST['email']).exists()
        if existUser:
            messages.error(request,'User already exist for email.')
            return HttpResponseRedirect(reverse('signup'))
        else:
            usersignup = ctrl.userSignup(request.POST)
            if usersignup:
                user = User.objects.get(username=request.POST['email'])
                user.is_active = True
                user.backend = settings.AUTHENTICATION_BACKENDS[0]
                auth.logout(request)
                auth.login(request, user)
                user.save()

            return render(request,'home.html')
    else:
        return render(request,'signup.html')




def user_logout(request):
    auth.logout(request)
    return HttpResponseRedirect(reverse('home'))


def chat_save(request):
    if request.method == 'POST':
        que = request.POST['question']
        chatHistory = Chat.objects.get()
