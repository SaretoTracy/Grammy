from django.contrib import admin
from .models import Profile,Photos

# Register your models here.
class PhotosAdmin(admin.ModelAdmin):

    admin.site.register(Photos)
    admin.site.register(Profile)