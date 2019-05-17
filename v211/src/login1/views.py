from django.http.response import  HttpResponseRedirect
from django.urls import reverse
from django.shortcuts import render, get_object_or_404
from .models import *
from .forms import *
from datetime import datetime
from django.contrib.auth import login, authenticate,views


def signup(request):
    if request.method=='GET':
        form=UserForm()
        return render(request,'signup.html',{'form':form})
    elif request.method=='POST':
        form=UserForm(request.POST)
        if form.is_valid():
            new=User.objects.create_user(
                username=request.POST.get('username'), 
                email=request.POST.get('email'),
                password=request.POST.get('password'))
            
            #form.save()
            return HttpResponseRedirect(reverse('vote:index'))
        else:
            render(request,'signup.html',{'error':'입력오류입니다'})

def signin(request):
    if request.method=='GET':
        form=UserForm()
        return render(request,'signin.html',{'form':form})
    elif request.method=='POST':
        form=UserForm(request.POST)
        #user_name=User.objects.get(username=request.POST.get('username'))
        user_name=request.POST.get('username')
        user_pass=request.POST.get('password')
        user1=authenticate(username=user_name,password=user_pass)
        login(request,user1)
        return HttpResponseRedirect(reverse('vote:index'))
                    