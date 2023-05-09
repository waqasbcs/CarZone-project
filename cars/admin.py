from django.contrib import admin
from .models import car
from django.utils.html import format_html

# Register your models here.

class carAdmin(admin.ModelAdmin):
     def thumbnail(self, object):
      return format_html('<img src="{}" width="40" style="border-radius:50px"/>'.format(object.car_photo .url))
     thumbnail.short_description = 'car photo'
     list_display = ('id','thumbnail','car_title','city','color','year','body_style','fuel_type','is_feature')
     list_display_links = ['thumbnail', 'id',]
     list_editable = ('is_feature',) 
     search_fields = ['id','car_title','city','color','year','body_style','fuel_type',]
     list_filter = ['car_title','city','model','color' ]
    
admin.site.register(car,carAdmin)
    

