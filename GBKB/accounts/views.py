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
import joblib
from predictor.models import Review,DataSet
# Create your views here.

def prediction(request):
    
    if request.user.is_authenticated:
        details = get_object_or_404(ExtentionUser, userID=request.user)
        if details.activation != True:
            return redirect('activation')
    else:
        return render(request, 'accounts/signin.html', {'error': "At first, sign-in"})

    if request.method == 'POST':
        lis=[]

        sq= request.POST['sq']
        lis.append(int(sq))
        wr=request.POST['wr']
        lis.append(int(wr))
        br = request.POST['br']
        lis.append(int(br))
        fl = request.POST['fl']
        lis.append(int(fl))
        li = request.POST['li']
        lis.append(int(li))
        rs = request.POST['rs']
        lis.append(int(rs))
        ai = request.POST['ai']
        lis.append(int(ai))

        cls= joblib.load('Finalized_model.sav')
        ans=int(cls.predict([lis]))

        area=['Mirpur','Uttora','Bonani','Dhanmondi','Basundhara','Gulshan']
        lift=['No lift','Lift service available']
        Review(userID=request.user, sqft=lis[0], washRoom=lis[1], bedRoom=lis[2], floor=lis[3],lift=lis[4],roadSize=lis[5],location=lis[6], price=ans).save()
        return render(request, 'prediction/predict.html',{'ans':ans,'ai':ai,'area':area[int(ai)-1],'sq':sq,'wr':wr,'br':br,'fl':fl,'li':li,'Lift':lift[int(li)],'rs':rs})
    ai,sq,wr,br,fl,li,rs=None,None,None,None,None,None,None
    return render(request, 'prediction/predict.html',{'ai':ai,'sq':sq,'wr':wr,'br':br,'fl':fl,'li':li,'rs':rs})



def signin(request):
    if request.user.is_authenticated:
        return redirect('home')
    if request.method == 'POST':
        user =auth.authenticate(username=request.POST['username'],password=request.POST['password'])

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

    Ads = PostAd.objects.all().order_by("-date")
    if request.method == 'GET':
        se = request.GET.get('search')
        lo= request.GET.get('location')
        print (lo, se)
        if lo or se:
            if lo:
                Ads = Ads.filter(location=lo).order_by("-date")
            if se:
                select=[]
                for i in Ads:
                    if se in i.title:
                        select.append(i)

                Ads= select
            return render(request, 'home.html', {'obj': Ads, 'lo': lo,'se':se})

    return render(request, 'home.html',{'obj':Ads})


def activation(request):
    if request.user.is_authenticated:
        details = get_object_or_404(ExtentionUser, userID=request.user)

    else:
        return render(request, 'accounts/signin.html', {'error': "At first, sign-in"})

    m = ""
    if request.method == 'POST':
        mail = request.POST['email']

        email_exist = User.objects.filter(email=mail)
        if email_exist:
            return render(request, 'accounts/activation.html',
                          {'error2': "Error: enter a unique email", })
        else:
            user = get_object_or_404(User, id=request.user.id)
            user.email = mail
            user.save()
            m = "New email address has saved"

    details = get_object_or_404(ExtentionUser, userID=request.user)
    cod = 0
    for i in range(6):
        cod = cod + random.randint(0, 10)
        cod = cod * 10

    details.code = cod

    body = 'Activation Code: ' + str(cod)

    details.save()

    send_mail(
        'Activation Code',
        body,
        settings.EMAIL_HOST_USER,
        [request.user.email],
        fail_silently=False,
    )

    return render(request, 'accounts/activation.html', {'message': m})

def confirmActivation(request):
    if request.user.is_authenticated:
        details = get_object_or_404(ExtentionUser, userID=request.user)


    else:
        return render(request, 'accounts/signin.html', {'error': "At first, sign-in"})


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
        return render(request, 'accounts/signin.html', {'error': "To post your AD you need to sign-in"})

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
    if request.user.is_authenticated:
        details = get_object_or_404(ExtentionUser, userID=request.user)
        if details.activation!=True:
            return redirect('activation')
    else:
        return render(request, 'accounts/signin.html', {'error': "At first, sign-in"})
    obj = get_object_or_404(PostAd, pk=pId)
    extendSellerInfo=get_object_or_404(ExtentionUser, userID=obj.userID)
    return render(request,'AdPosting/detail.html', {'obj': obj,"mobile":extendSellerInfo})

def myAccount(request):
    if request.user.is_authenticated:
        details = get_object_or_404(ExtentionUser, userID=request.user)
        if details.activation!=True:
            return redirect('activation')
    else:
        return render(request, 'accounts/signin.html', {'error': "At first, sign-in"})
    help=Review.objects.all()


    Ads=PostAd.objects.all().filter(userID=request.user).order_by("-date")


    if help:
        return render(request, 'accounts/myAccount.html',{'obj':Ads, "ex":details,'help':True })
    return render(request, 'accounts/myAccount.html',{'obj':Ads, "ex":details})


def changeImage(request):

    if request.user.is_authenticated:
        details = get_object_or_404(ExtentionUser, userID=request.user)
        if details.activation!=True:
            return redirect('activation')
    else:
        return render(request, 'accounts/signin.html', {'error': "At first, sign-in"})

    if request.method == 'POST':
        if request.FILES.get('image'):
            details.image = request.FILES['image']
            details.save()
            Ads = PostAd.objects.all().filter(userID=request.user).order_by("-date")
            return render(request, 'accounts/myAccount.html',
                          {'obj': Ads, "ex": details, "message": "New image saved"})
    Ads=PostAd.objects.all().filter(userID=request.user).order_by("-date")
    return render(request, 'accounts/myAccount.html',{'obj':Ads, "ex":details, "error":"Problem, image couldn't change. selsect .jpg image"})



def changeEmail(request):

    if request.user.is_authenticated:
        details = get_object_or_404(ExtentionUser, userID=request.user)
        if details.activation!=True:
            return redirect('activation')
    else:
        return render(request, 'accounts/signin.html', {'error': "At first, sign-in"})

    if request.method == 'POST':
        mail = request.POST['email']
        print (mail)

        email_exist = User.objects.filter(email=mail)
        if email_exist:
            return render(request, 'accounts/changeEmail.html',
                              {'error': "Error: enter a unique email", })

        else:
            user = get_object_or_404(User, id=request.user.id)
            user.email=mail
            user.save()
            m="New email address is saved"
            details.activation=False
            details.save()

            return redirect('activation')
    return render(request, 'accounts/changeEmail.html')



class delete(DeleteView):
    model=PostAd
    template_name='AdPosting/delete.html'
    success_url = 'myAccount/'



def changeNumber(request):

    if request.user.is_authenticated:
        details = get_object_or_404(ExtentionUser, userID=request.user)
        if details.activation!=True:
            return redirect('activation')
    else:
        return render(request, 'accounts/signin.html', {'error': "At first, sign-in"})

    if request.method == 'POST':
        num=request.POST['number']
        if len(str(num)) >= 11:
            details.mobileNumber = num
            details.save()
            Ads = PostAd.objects.all().filter(userID=request.user).order_by("-date")
            return render(request, 'accounts/myAccount.html',
                          {'obj': Ads, "ex": details, "message2": "New Phone Number is saved"})
    Ads=PostAd.objects.all().filter(userID=request.user).order_by("-date")
    return render(request, 'accounts/myAccount.html',{'obj':Ads, "ex":details, "error2":"Enter Mobile Number Correctly"})


def reviewFromUser(request):
    if request.user.is_authenticated:
        details = get_object_or_404(ExtentionUser, userID=request.user)
        if details.activation!=True:
            return redirect('activation')
    else:
        return render(request, 'accounts/signin.html', {'error': "At first, sign-in"})
    help=Review.objects.all()
    Message="If you know the actual price over any of the predicted price then please enter the price and submit"

    return render(request, 'prediction/review.html', {"help":help,'message':Message})
def reviewSub(request,pId):
    if request.user.is_authenticated:
        details = get_object_or_404(ExtentionUser, userID=request.user)
        if details.activation!=True:
            return redirect('activation')
    else:
        return render(request, 'accounts/signin.html', {'error': "At first, sign-in"})


    obj=get_object_or_404(Review, id=pId)
    if request.method == 'POST':
        price=int(request.POST['actualPrice'])
        print (price)

        predictedPrice=int(obj.price)
        pricedifference=abs(predictedPrice-price)
        print ("price diff:",pricedifference)
        flag=False
        if (predictedPrice < 10000000) and (pricedifference <= 800000):
            print ("less than one cror")
            flag=True
        elif (predictedPrice < 20000000 ) and (predictedPrice > 10000000) and (pricedifference <= 1000000):
            flag=True
        elif (predictedPrice<30000000) and (predictedPrice > 20000000 ) and (predictedPrice > 10000000) and (pricedifference <= 1500000):
            flag=True
        elif (predictedPrice<40000000) and (predictedPrice > 30000000) and (predictedPrice > 20000000 ) and (predictedPrice > 10000000) and (pricedifference <= 2000000):
            flag=True
        elif (predictedPrice<50000000) and (predictedPrice > 40000000) and (predictedPrice > 30000000) and (predictedPrice > 20000000 ) and (predictedPrice > 10000000) and (pricedifference <= 2500000):
            flag=True

        if flag==True:
            print ("saving")
            DataSet(sqft=obj.sqft, washRoom=obj.washRoom, bedRoom=obj.bedRoom, floor=obj.floor, lift=obj.lift,roadSize=obj.roadSize, location=obj.location, price=price).save()
            get_object_or_404(Review, id=pId).delete()


    help = Review.objects.all()
    Message = "You submission noted, you can help us more."
    return render(request, 'prediction/review.html', {"help":help,'message':Message})


def about(request):
    return render(request, 'about/about.html',)

