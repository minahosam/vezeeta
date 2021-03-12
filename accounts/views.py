from django.shortcuts import redirect, render
from .models import user_info
from .forms import new_user,UserInfoForm
from django.contrib.auth import authenticate,login
from django.urls import reverse
from django.contrib import messages
def signup(request):
    if request.method=='POST':
        signupform=new_user(request.POST)
        if signupform.is_valid():
            signupform.save()
            username1=signupform.cleaned_data['username']
            password1=signupform.cleaned_data['password2']
            user1=signupform.save()#authenticate(username=username1, password=password1)
            login(request,user1,backend='django.contrib.auth.backends.ModelBackend')
            messages.success(request, 'register succeful')
            return redirect('index:index')
    else:
        signupform=new_user() 
    return render(request,'registration/signup.html',{'form1':signupform})
def profile(request):
    return redirect('index:index')