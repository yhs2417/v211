from django.db import models
from datetime import datetime
from django.conf import settings
from django.utils import timezone

class PostType(models.Model):
    name=models.CharField('게시판 종류',max_length=100)
    
    def __str__(self):
        return self.name


class Post(models.Model):
    
    types=models.ForeignKey(PostType,on_delete=models.CASCADE)
    headline=models.CharField('제목',max_length=100)
    content=models.TextField('내용')
    pub_date=models.DateTimeField(default=timezone.now)
    author=models.ForeignKey(settings.AUTH_USER_MODEL,on_delete=models.CASCADE)
  
    def __str__(self):
        return self.headline
  
class Achieve(models.Model):
    
    headline=models.CharField('제목',max_length=100)
    content=models.TextField('내용')
    pub_date=models.DateTimeField(default=timezone.now)
    author=models.ForeignKey(settings.AUTH_USER_MODEL,on_delete=models.CASCADE)
  
    def __str__(self):
        return self.headline

class Study(models.Model):
    
    headline=models.CharField('제목',max_length=100)
    content=models.TextField('내용')
    pub_date=models.DateTimeField(default=timezone.now)
    author=models.ForeignKey(settings.AUTH_USER_MODEL,on_delete=models.CASCADE)
  
    def __str__(self):
        return self.headline
    
class Image(models.Model):
    post=models.ForeignKey(Post,on_delete=models.CASCADE)
    image=models.ImageField('이미지파일',upload_to='image/%Y/%m/%d')
    
    def delete(self,using=None,keep_parents=False):
        self.image.delete()
        return models.Model.delete(self,using=using,keep_parents=keep_parents)
    
class File(models.Model):
    post=models.ForeignKey(Post,on_delete=models.CASCADE)
    file=models.FileField('파일 업로드',upload_to='file/%Y/%m/%d')
    
    def delete(self,using=None,keep_parents=False):
        self.file.delete()
        return models.Model.delete(self,using=using,keep_parents=keep_parents)