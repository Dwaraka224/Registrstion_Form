from django.shortcuts import render
from django.http import HttpResponse
from django.core.mail import send_mail
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
 
 