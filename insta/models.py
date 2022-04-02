from django.db import models
from cloudinary.models import CloudinaryField

class Profile (models.Model):
    profile_pic= CloudinaryField('image')
    bio = models.CharField(max_length=250)

    def __str__(self):
        return self.profile
    
    def save_profile(self):
        self.save()
    def delete_profile(self):
        self.delete()


class Photos(models.Model):
    image_name = models.CharField(max_length=100)
    image = CloudinaryField('image')
    caption= models.CharField(max_length=250)
    profile =  models.ManyToManyField('profile')
    Comments= models.CharField(max_length=250)

    def __str__(self):
        return self.photos
    
    def save_photos(self):
        self.save()
    def delete_photos(self):
        self.delete()
