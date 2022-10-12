from django.contrib import admin
from .models import Work
# Register your models here.
class WorkAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'link', 'date')
    list_display_links = ('id', 'title', 'link')



admin.site.register(Work, WorkAdmin)
    