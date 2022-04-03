from django.db import models
from cloudinary.models import CloudinaryField
from django.utils import timezone
from tinymce.models import HTMLField

class Profile (models.Model):
    profile_pic= CloudinaryField('images/')
    bio = models.CharField(max_length=250)

    def __str__(self):
        return self.bio
    
    def save_profile(self):
        self.save()
    def delete_profile(self):
        self.delete()
class Comments(models.Model):
    '''
    Class that handles user comments
    '''
    message = models.TextField()
    pub_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.message


class Photos(models.Model):
    image_name = HTMLField()
    image = CloudinaryField('images/')
    caption= models.CharField(max_length=250)
    profile =  models.ManyToManyField('profile')
    likes = models.PositiveIntegerField(default=0)
    date = models.DateTimeField(default=timezone.now)
    comments = models.ForeignKey(Comments, on_delete=models.CASCADE)

    def __str__(self):
        return self.caption
    
    def save_photos(self):
        self.save()
    def delete_photos(self):
        self.delete()
    @classmethod
    def display_all(cls):
        '''
        Function that dislays post information
        '''
        caption = cls.objects.all()
        return caption
