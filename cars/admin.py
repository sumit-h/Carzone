from django.contrib import admin
from .models import Car
from django.utils.html import format_html

# Register your models here.

class CarAdmin(admin.ModelAdmin):
    def thumbnail(self,object):
        return format_html('<img src="{}" width="40" style="border-radius:50px;"  />'.format(object.car_photo.url))
        thumbnail.short_description = 'Car Images'
    list_display=['id','thumbnail','car_title','color','year','state','city','price','body_style','is_featured']
    list_display_links=['id','thumbnail','car_title']
    list_editable = ('is_featured',)
    search_fields = ('city','color','body_style','car_title','id')
    list_filter = ('city','color','fuel_type','is_featured')
admin.site.register(Car,CarAdmin)
