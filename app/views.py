from django.shortcuts import render
from django.http import HttpResponse,HttpResponseRedirect
from django.core.mail import send_mail
from django.urls import reverse
from django.contrib.auth import authenticate,login
# Create your views here.
from app.forms import *
def registration(request):
    ufo=userForm()
    pfo=ProfileForm()
    d={'ufo':ufo,'pfo':pfo}
    if request.method=='POST' and request.FILES:
        ufd=userForm(request.POST)
        pfd=ProfileForm(request.POST,request.FILES)
        if ufd.is_valid() and pfd.is_valid():
           MUFDO=ufd.save(commit=False)
           pw=ufd.cleaned_data['password']
           MUFDO.set_password(pw)
           MUFDO.save()
           MPFDO=pfd.save(commit=False)
           MPFDO.username=MUFDO
           MPFDO.save()
           send_mail('Registration',
                     'Registration is successful completed',
                     'reddydwarakanath800@gmail.com',
                     [MUFDO.email],
                     fail_silently=False)

           return HttpResponse('Registration is successfully')
        else:
           return HttpResponse('Registration is Invalid')

    
    return render(request,'registration.html',d)
def home(request):
    if request.session.get('username'):
        username=request.session.get('username')
        d={'username':username}
        return render(request,'home.html',d)
    return render(request,'home.html')

def user_login(request):
    if request.method=='POST':
        username=request.POST['un']
        password=request.POST['pw']
        AUO=authenticate(username=username,password=password)
        if AUO and AUO.is_active:
            login(request,AUO)
            request.session['username']=username
            return HttpResponseRedirect(reverse('home'))
        else:
            return HttpResponse('Invalid Credentials')
    return render(request,'user_login.html')
 
 