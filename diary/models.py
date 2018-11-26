from django.db import models
from django.utils import timezone
from datetime import datetime
from imagekit.models import ImageSpecField
from imagekit.processors import Thumbnail
# Create your models here.



class Post(models.Model):
    author = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    title = models.CharField(max_length=200) #일기 제목 
    song = models.CharField(max_length=200,null=True) #노래제목
    singer = models.CharField(max_length=200,null=True) #가수
    link = models.URLField(null=True) #노래 링크
    text = models.TextField() #일기 내용
    photo = models.ImageField(null=True)
    photo_thumbnail = ImageSpecField(
	source='photo',
	processors = [Thumbnail(300, 300)], # 처리할 작업 목룍
	format = 'JPEG',		# 최종 저장 포맷
	options = {'quality': 100})
    created_date = models.DateTimeField(
            default=timezone.now)
    published_date = models.DateTimeField(
            blank=True, null=True)
    now = timezone.now()
    d_time = now.strftime("%m.%d")
    def publish(self):
        self.published_date = timezone.now()
        self.save()
    def __str__(self):
        return self.title
