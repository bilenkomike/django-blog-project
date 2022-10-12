from django.db import models
from datetime import datetime






### posts
# id: INT
# title: STR(200)
# date: datetime
# tag: STR
# description: TEXT
# views: INT
# video: STR
# main_photo: STR
# photo_1:STR
# photo_2:STR
# photo_3:STR



# Create your models here.
class Post(models.Model):
    title = models.CharField(max_length=200, blank=True)
    tag = models.CharField(max_length=200, blank=True)
    description = models.TextField()
    views = models.IntegerField(default=0)
    video = models.FileField(upload_to='videos/%Y/%m/%d',blank=True, verbose_name="", null=True)
    video_link = models.TextField(blank=True)
    date = models.DateTimeField(default=datetime.now)
    photo_main = models.ImageField(upload_to="photos/%Y/%m/%d", blank=True)
    photo_1 = models.ImageField(upload_to="photos/%Y/%m/%d", blank=True)
    photo_2 = models.ImageField(upload_to="photos/%Y/%m/%d", blank=True)
    photo_3 = models.ImageField(upload_to="photos/%Y/%m/%d", blank=True)
    
    def __str__(self):
        return self.title