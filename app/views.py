from django.shortcuts import render

# Create your views here.
from app.forms import *
def registration(request):
    ufo=userForm()
    pfo=ProfileForm()
    d={'ufo':ufo,'pfo':pfo}
    
    return render(request,'registration.html',d)
 
 