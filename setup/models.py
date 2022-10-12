from django.db import models
from accounts.models import Account


# Create your models here.


# ### SETUP
# id: INT
# main_photo: STR
# instagram: STR
# vk: STR
# pinterest: STR
# twitter: STR
# owner: FOREIGN [user]
# description: TEXT
# subtitle: STR






class Setup(models.Model):
    mian_photo = models.ImageField(upload_to='setup/photos/')
    instagram = models.CharField(max_length=255, blank=True)
    vk = models.CharField(max_length=255, blank=True)
    pinterest = models.CharField(max_length=255, blank=True)
    twitter = models.CharField(max_length=255, blank=True)
    owner = models.ForeignKey(Account, on_delete=models.CASCADE)
    description = models.TextField(max_length=500)
    subtitle = models.CharField(max_length=500)
    