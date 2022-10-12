from django.db import models
from datetime import datetime

### STORIES
# id: INT
# title: STR
# date: DATETIME
# video: VIDEO

# Create your models here.
class Story(models.Model):
    title = models.CharField(max_length=200)
    date = models.DateField(default=datetime.now)
    video = models.FileField(upload_to='stories/%Y/%m/%d/', verbose_name="", null=True)

    def __str__(self):
        return self.title


    class Meta:
        verbose_name = 'Story'
        verbose_name_plural = 'Stories'