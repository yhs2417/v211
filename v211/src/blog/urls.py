from django.urls import path
from .views import *


app_name='blog'

urlpatterns=[
    path('',index,name='index'),
    path('hobby/<int:type_id>',hobby,name='hobby'),
    path('<int:user_id>/',add_post,name='add_post'),
    path('detail/<int:post_id>',detail,name='detail'),
    path('searching/',searching,name='searching'),
    path('study/',study, name='study'),
    path('study/<int:study_id>',studydetail,name='studydetail')
    
    ]