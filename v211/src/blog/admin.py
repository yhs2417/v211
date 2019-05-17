from django.contrib.auth.models import User
from django.contrib import admin
from .models import *
from django_summernote.admin import SummernoteModelAdmin

class PostAdmin(admin.ModelAdmin):
    fields=['types','headline','content','author']
    list_display=('id','types','headline','content','pub_date','author')
    
class PostTypeAdmin(admin.ModelAdmin):
    fields=['name']
    list_display=('id','name')
    
    
class ImageAdmin(admin.ModelAdmin):
    fields=['post','image']
    list_display=('post','image')
    
class FileAdmin(admin.ModelAdmin):
    fields=['post','file']
    list_display=('post','file')        

class AchieveAdmin(admin.ModelAdmin):
    fields=['headline','content','author']
    list_display=('id','headline','content','pub_date','author')   

class StudyAdmin(SummernoteModelAdmin):
    fields=['headline','content','author']
    list_display=('id','headline','content','pub_date','author')  
    summernote_feilds='__all__'

admin.site.register(PostType, PostTypeAdmin)
admin.site.register(Post,PostAdmin)
admin.site.register(Image,ImageAdmin)
admin.site.register(File,FileAdmin)
admin.site.register(Achieve,AchieveAdmin)
admin.site.register(Study,StudyAdmin)