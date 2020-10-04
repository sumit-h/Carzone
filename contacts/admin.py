from django.contrib import admin
from .models import Contact
# Register your models here.
class contactAdmin(admin.ModelAdmin):
    list_display = ('id','first_name','last_name','email','city','car_title','create_date')
    list_display_links = ('id','first_name','last_name','email')
    search_fields = ('first_name','last_name','email','car_title')
    list_per_page = 25
admin.site.register(Contact, contactAdmin)
