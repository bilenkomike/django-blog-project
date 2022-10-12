from django.db import models
from accounts.models import Account
# Create your models here.

# ### CONTACT
# id: INT
# fullname: STR
# user_id: INT [?authenticated]
# email: STR
# message:TEXT


class Contact(models.Model):
    fullname = models.CharField(max_length=255)
    email = models.CharField(max_length=200)
    user = models.ForeignKey(Account, on_delete=models.CASCADE,blank=True, null=True)
    message = models.TextField()

    def __str__(self):
        return self.email