from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.models import User
from django.contrib import auth
from django.views.generic import ListView,detail
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from django.views.generic.edit import DeleteView
from django.contrib.auth import authenticate, login
from .models import ExtentionUser, PostAd
from .forms import UserReg, ExtentUser, PostAdForm
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


    Ads=PostAd.objects.all().order_by("-date")


    return render(request, 'home.html',{'obj':Ads})


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

    return render(request,'accounts/activation.html', {'error':"Wrong activation code"})

def postAd(request):
    if request.user.is_authenticated:
        details = get_object_or_404(ExtentionUser, userID=request.user)

        if details.activation!=True:
            return redirect('activation')
    else:
        return render(request, 'accounts/signin.html', {'error': "To post your AD you need to sign-in first"})

    e=''
    if request.method == 'POST':

        form = PostAdForm(request.POST, request.FILES)
        if form.is_valid():

            frm=form.save(commit=False)
            frm.userID=request.user
            frm.save()
            # AD =PostAd(userID=request.user, title=form.cleaned_data['title'], location=form.cleaned_data['location'], sqft=form.cleaned_data['sqft'],washRoom=form.cleaned_data['washRoom'],bedRoom=form.cleaned_data['bedRoom'], description=form.cleaned_data['description'],roadSize=form.cleaned_data['roadSize'], lift=form.cleaned_data['lift'], floor=form.cleaned_data['floor'], price=form.cleaned_data['price'])
            # print ("AD saved")
            # if request.FILES.get['img1']:
            #     print("got img")
            #     AD.img1 = request.FILES['img1']
            # if request.FILES.get('img2'):
            #     AD.img2 = request.FILES['img2']
            # if request.FILES.get('img3'):
            #     AD.img3 = request.FILES['img3']
            # AD.save()

            Ads = PostAd.objects.all().order_by("-date")

            return render(request, 'home.html', {'obj': Ads,'message':"Your AD is posted"})
        else:
            return render(request, 'AdPosting/postAd.html',{'error': "Fill the form correctly", 'form': form})

    form=PostAdForm()
    return render(request, 'AdPosting/postAd.html', {'error':e , 'form':form})


def detail(request, pId ):
    obj = get_object_or_404(PostAd, pk=pId)
    extendSellerInfo=get_object_or_404(ExtentionUser, userID=obj.userID)
    return render(request,'AdPosting/detail.html', {'obj': obj,"mobile":extendSellerInfo})