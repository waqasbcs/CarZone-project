from django.contrib import admin
from .models import Team
from django.utils.html import format_html

# Register your models here.

class TeamAdmin(admin.ModelAdmin):
    list_display = ['thumbnail','first_name', 'last_name', 'designation', 'created_at', ]
    list_display_links = ['thumbnail', 'first_name']
    
    def thumbnail(self, object):
        return format_html('<img src="{}" width="40" style="border-radius:50px"/>'.format(object.photo.url))
    
    thumbnail.short_description = 'Photo'
    search_fields = ['first_name', 'last_name', 'designation',]
    list_filter = ['designation', ]

admin.site.register(Team, TeamAdmin)
