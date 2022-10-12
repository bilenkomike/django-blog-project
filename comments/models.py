from django.db import models

from posts.models import Post
from accounts.models import Account

from datetime import datetime


# Create your models here.


# ### COMMENTS
# id: INT
# post: FOREIGN [post]
# user: FOREIGN[User]
# comment: TEXT
# date: datetime


class Comment(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    user = models.ForeignKey(Account, on_delete=models.CASCADE)
    comment = models.TextField(max_length=500)
    date = models.DateTimeField(default=datetime.now)

    def __str__(self):
        return self.comment[:20] + '...'