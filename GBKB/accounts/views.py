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
from django.core.mail import send_mail
import random
from django.conf import settings
# Create your views here.

def signin(request):
    if request.user.is_authenticated:
        return redirect('home')
    if request.method == 'POST':
        user =auth.authenticate(username=request.POST['username'],password=request.POST['password'])
        print (request.POST['username'])
        if user is not None:
            auth.login(request, user)
            if request.user.is_authenticated:
                exU = get_object_or_404(ExtentionUser, userID=request.user)
                if exU.activation != True:
                    return redirect('activation')
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

            email_exist = User.objects.filter(email=form1.cleaned_data['email'])
            if email_exist:
                return render(request, 'accounts/signup.html',
                              {'error': "fill the form correctly and choose a unique email", 'form1': form1,
                               'form2': form2})
            else:
                userSaved = form1.save()
                ExtentionUser(userID=userSaved, mobileNumber=form2.cleaned_data['mobileNumber']).save()
                auth.login(request, userSaved)
                #is_active = false
                #can be used to make account inactive
                return redirect('activation')
        else:
            return render(request, 'accounts/signup.html',{'error': "fill the form correctly and choose a unique username", 'form1': form1, 'form2': form2})
    form1=UserReg()
    form2=ExtentUser()
    return render(request, 'accounts/signup.html', {'error':e , 'form1':form1,'form2':form2})


def home(request):
    if request.user.is_authenticated:
        details = get_object_or_404(ExtentionUser, userID=request.user)

        if details.activation!=True:
            return redirect('activation')

    return render(request, 'home.html')


def activation(request):

    m=""
    if request.method == 'POST':
        mail = request.POST['email']

        email_exist = User.objects.filter(email=mail)
        if email_exist:
            return render(request, 'accounts/activation.html',
                              {'error2': "Error: enter a unique email", })
        else:
            user = get_object_or_404(User, id=request.user.id)
            user.email=mail
            user.save()
            m="New email address has saved"





    details = get_object_or_404(ExtentionUser, userID=request.user)
    cod=0
    for i in range(6):
        cod=cod+random.randint(0,10)
        cod=cod*10

    details.code=cod

    body= 'Activation Code: '+str(cod)

    details.save()

    send_mail(
        'Activation Code',
        body,
        settings.EMAIL_HOST_USER,
        [request.user.email],
        fail_silently=False,
        )



    return render(request,'accounts/activation.html',{'message':m})

def confirmActivation(request):
    details = get_object_or_404(ExtentionUser, userID=request.user)

    if request.method == 'POST':
        code = int(request.POST['code'])

        if code==details.code:
            details.activation=True
            details.save()
            return redirect('home')


    return render(request,'accounts/activation.html',{'error':"Wrong activation code"} )



