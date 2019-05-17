from django.http.response import  HttpResponseRedirect
from django.urls import reverse
from django.shortcuts import render, get_object_or_404
from .models import *
from .forms import *
from datetime import datetime
from django.contrib.auth import login, authenticate,views
from django.contrib.auth.decorators import login_required   
from django.contrib.auth.models import User
from django.views.generic.list import ListView
from django.core.paginator import Paginator,EmptyPage,PageNotAnInteger


def index(request):
    type_res=PostType.objects.all()
    data1={'posttype_data':type_res}
    months=[]
    for i in range(12):
        obj_achieve=Achieve.objects.filter(headline__startswith='19-0%s'%str(i+1)).order_by('headline')
        #data1[str(i+1)]=obj_achieve
        months.append(obj_achieve)
    data1['months']=months
    '''
    paginator = Paginator(obj_achieve,7)
    page = request.GET.get('page')
    
    try:
        posts = paginator.page(page)
    except PageNotAnInteger:
        posts = paginator.page(1)
    except EmptyPage:
        posts = paginator.page(paginator.num_pages)'''
    
   
    return render(request,'index.html',data1)
               


def hobby(request,type_id):
    res=get_object_or_404(PostType,pk=type_id)
    obj=res.post_set.all()
    
    type_res=PostType.objects.all()
    return render(request,'hobby.html',{'post_data':obj,'posttype_data':type_res})

def study(request):
    res=Study.objects.all()
    
    type_res=PostType.objects.all()
    return render(request,'study.html',{'study':res,'posttype_data':type_res})

def studydetail(request,study_id):
    res=get_object_or_404(Study,pk=study_id)
    type_res=PostType.objects.all()
    return render(request,'studydetail.html',{'detail':res,'posttype_data':type_res})

def detail(request,post_id):
    res1=get_object_or_404(PostType,pk=post_id)
    return render(request,'detail.html',{'data':res1})
    
    
@login_required
def add_post(request,user_id):
    if request.method=='GET':
        form=PostForm()
        return render(request,'addpost.html',{'form':form})
    elif request.method=='POST':
        form=PostForm(request.POST)
        if form.is_valid():
            obj=form.save(commit=False)
            obj.pub_date=datetime.now()
            user=User.objects.get(id=user_id)
           
            obj.author=user
            obj.save()
            
            for i in request.FILES.getlist('images'):
                image = Image(post=obj,image=i)   
                image.save()                   
          
            for i in request.FILES.getlist('files'):
                file = File(post=obj,file=i)
                file.save()
            return HttpResponseRedirect(reverse('blog:index'))
        
def searching(request):
    q=request.GET.get('searching') 
    t=request.GET.get('types')
   
    if t=='head':
        res=Post.objects.filter(headline=q)
    elif t=='author':
        user=User.objects.get(username=q)
        res=user.post_set.all
        print(res)
    return render(request,'index.html',{'query':res})    