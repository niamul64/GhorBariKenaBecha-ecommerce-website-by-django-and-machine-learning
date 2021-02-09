from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.models import User
from django.contrib import auth
from django.views.generic import ListView,detail
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from django.views.generic.edit import DeleteView
from django.contrib.auth import authenticate, login
from .models import ExtentionUser, PostAd
from .forms import UserReg, ExtentUser
# Create your views here.
def signin(request):
    if request.method == 'POST':
        user =auth.authenticate(username=request.POST['username'],password=request.POST['password'])
        print (request.POST['username'])
        if user is not None:
            auth.login(request, user)
            return redirect('home')
        else:
            return render(request, 'accounts/signin.html',{'error':"incorrect user name or password"})
    return render(request, 'accounts/signin.html')
def signout(request):
    if request.method == 'POST':
        auth.logout(request)

    return redirect('home')

def signup(request):
    if request.user.is_authenticated:
        return redirect('home')

    e=''
    if request.method == 'POST':
        form1 = UserReg(request.POST)
        form2 = ExtentUser(request.POST)

        if form1.is_valid() and form2.is_valid() and len(form2.cleaned_data['mobileNumber'])==11 :

            userSaved=form1.save()
            ExtentionUser(userID =userSaved, mobileNumber=form2.cleaned_data['mobileNumber']).save()
            auth.login(request, userSaved)
            return redirect('home')
        else:
            return render(request, 'signup.html',{'error': "fill the form correctly and choose a unique username", 'form1': form1, 'form2': form2})
    form1=UserReg()
    form2=ExtentUser()
    return render(request, 'accounts/signup.html', {'error':e , 'form1':form1,'form2':form2})



def home(request):
    return render(request, 'home.html')
