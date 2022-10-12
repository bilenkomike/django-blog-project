from django.contrib import admin

from .models import Comment
# Register your models here.

class CommentAdmin(admin.ModelAdmin):
    list_display = ('id','user', 'post','date')
    list_display_links = ('id','user','post')
    search_fields = ('comment', 'user', 'post')

admin.site.register(Comment, CommentAdmin)