from hashlib import blake2b
from django.db import models

from django.contrib.auth.models import User


# Account
# id: INT
# user: FOREIGN [User]
# photo: STR(200)


# Create your models here.
class Account(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    photo = models.ImageField(upload_to='avatars/%Y/%m/%d', null=True, blank=True)
    phone = models.CharField(max_length=200, blank=True, null=True)

    def __str__(self):
        return self.user.username