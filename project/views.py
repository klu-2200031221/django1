from django.contrib.auth import authenticate
from django.shortcuts import render
from requests import auth

from project.models import Faculty


# Create your views here.
def projecthomepage(request):
    return render(request, 'projecthomepage.html')


def adminhomepage(request):
    return render(request, 'adminhomepage.html')


def studenthomepage(request):
    return render(request, 'studenthomepage.html')


def facultyhomepage(request):
    return render(request, 'facultyhomepage.html')

from django.contrib.auth.models import User,auth
from django.contrib.auth.models import User
from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib import auth
def register(request):
    return render(request, 'register.html')





def register1(request):
    if request.method == 'POST':
        username = request.POST['username']
        pass1 = request.POST['password']
        pass2 = request.POST['password1']
        if pass1 == pass2:
            if User.objects.filter(username=username).exists():
                messages.info(request, 'OOPS! Username already exist.')
                return render(request, 'register.html')
            else:
                user = User.objects.create_user(username=username, password=pass1)
                user.save()
                messages.info(request, 'Account created successfully!!!')
                return render(request, 'projecthomepage.html')
        else:
            messages.info(request, 'password doesnot match.')
            return render(request, 'register.html')


def login(request):
    return render(request, 'login.html')




def login2(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = auth.authenticate(request, username=username, password=password)
        if user is not None:
            auth.login(request, user)
            if len(username) == 10:
                return redirect('studenthomepage')
            elif len(username) == 4:
                return redirect('facultyhomepage')
            elif len(username) == 5:
                return redirect('adminhomepage')
            else:
                return redirect('projecthomepage')
        else:
            messages.error(request, 'Invalid username or password.')
            return render(request, 'login.html')
    else:
        return render(request, 'login.html')

def logout(request):
    auth.logout(request)
    return render(request, 'projecthomepage.html')

