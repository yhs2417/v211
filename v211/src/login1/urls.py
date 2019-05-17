from django.urls import path
from .views import *
from django.contrib.auth import views

app_name='login1'

urlpatterns=[
    path('',signup,name='signup'),
    path('signin/',signin,name='signin'),
    path('logout/',views.logout,name='logout')
    
    ]