from django.contrib import admin
from .models import Contact


class ContactAdmin(admin.ModelAdmin):
    list_display = ('id', 'fullname', 'email')
    list_display_links = ('id', 'fullname', 'email')

# Register your models here.
admin.site.register(Contact, ContactAdmin)