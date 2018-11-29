from django.db import models
from django.utils import timezone
from datetime import datetime
from django import forms
# Create your models here.



class Post(models.Model):
    author = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    title = models.CharField(max_length=200) #일기 제목 
    song = models.CharField(max_length=200,null=True) #노래제목
    singer = models.CharField(max_length=200,null=True) #가수
    link = models.CharField(max_length=200,null=True) #노래 링크
    text = models.TextField() #일기 내용
    image = models.ImageField(blank=True, null=True)
    created_date = models.DateTimeField(
            default=timezone.now,)
    published_date = models.DateTimeField(
            blank=True, null=True)
    def publish(self):
        self.published_date = timezone.now()
        self.save()
    def __str__(self):
        return self.title

