from django.contrib import admin
from .models import Team
from django.utils.html import format_html
# Register your models here.
class TeamAdmin(admin.ModelAdmin):
    def thumbnail(self,object):
        return format_html('<img src="{}" width="40" style="border-radius:50px;"  />'.format(object.photo.url))
# format(object.photo.url)) goes into src
    thumbnail.short_description = 'photo'   # to change name thumbnail to ph
    list_display = ('id','thumbnail','first_name','designation','craeted_date')
    list_display_links = ('id','first_name','thumbnail')
    search_fields = ('first_name','last_name')
    list_filter = ('designation',)
admin.site.register(Team,TeamAdmin)
