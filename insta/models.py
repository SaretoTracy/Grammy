from django.db import models
from cloudinary.models import CloudinaryField


class Profile (models.Model):
    profile_pic= CloudinaryField('images/')
    bio = models.CharField(max_length=250)

    def __str__(self):
        return self.bio
    
    def save_profile(self):
        self.save()
    def delete_profile(self):
        self.delete()


class Photos(models.Model):
    image_name = models.CharField(max_length=100)
    image = CloudinaryField('images/')
    caption= models.CharField(max_length=250)
    profile =  models.ManyToManyField('profile')
    Comments= models.CharField(max_length=250)

    def __str__(self):
        return self.caption
    
    def save_photos(self):
        self.save()
    def delete_photos(self):
        self.delete()
