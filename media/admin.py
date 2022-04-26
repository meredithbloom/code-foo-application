from django.contrib import admin
from .models import Media

# Register your models here.
class MediaAdmin(admin.ModelAdmin):
    list_display = ('media_type', 'name',)

admin.site.register(Media, MediaAdmin) 