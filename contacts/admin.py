from django.contrib import admin
from . models import contact

# Register your models here.
class ContactAdmin(admin.ModelAdmin):
      list_display = ('id','first_name','last_name','email','car_title','city','create_date')
      list_display_links = ('id','first_name','last_name')
      search_fields = ('id','first_name','last_name')
      list_per_page = 25
    
admin.site.register(contact,ContactAdmin)