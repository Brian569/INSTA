from django.contrib import admin
from .models import (
    Profile,
    Image
)

@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    list_display = ('bio','name')
    

@admin.register(Image)
class ImageAdmin(admin.ModelAdmin):
    list_display = ('image', 'image_name', 'profile')
