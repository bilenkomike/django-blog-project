from django.db import models
from datetime import datetime
# Create your models here.
### works 
# id: INT
# title: STR
# link: STR
# photo_main: STR
# photo_1: STR [blank]
# photo_2: STR [blank]
# photo_3: STR [blank]
# views: INT
# tag1: STR
# tag2: STR
# tag3: STR



class Work(models.Model):
    title = models.CharField(max_length=200)
    link = models.CharField(max_length=200)
    description = models.TextField()
    photo_main = models.ImageField(upload_to='photos/%Y/%m/%d/')
    photo_1 = models.ImageField(upload_to='photos/%Y/%m/%d/', blank=True)
    photo_2 = models.ImageField(upload_to='photos/%Y/%m/%d/', blank=True)
    photo_3 = models.ImageField(upload_to='photos/%Y/%m/%d/', blank=True)
    date = models.DateField(default=datetime.now)
    views = models.IntegerField(default=0)
    tag_1 = models.CharField(max_length=200)
    tag_2 = models.CharField(max_length=200, blank=True)
    tag_3 = models.CharField(max_length=200, blank=True)

    def __str__(self):
        return self.title