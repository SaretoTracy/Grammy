from django.contrib import admin
from .models import Profile,Photos,Comments

# Register your models here.
class PhotosAdmin(admin.ModelAdmin):

    admin.site.register(Photos)
    admin.site.register(Profile)
    admin.site.register(Comments)
    