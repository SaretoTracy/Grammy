from django.db import models
from cloudinary.models import CloudinaryField
from django.utils import timezone
from django.contrib.auth.models import User
from tinymce.models import HTMLField

class Profile (models.Model):
    profile_pic= CloudinaryField('images/')
    bio = models.CharField(max_length=250)
    user = models.ForeignKey(User, on_delete=models.CASCADE, default=1)
    followers = models.IntegerField(default=0)
    following = models.IntegerField(default=0)
    posts = models.IntegerField(default=0)

    def __str__(self):
        return self.bio
    
    def save_profile(self):
        self.save()
    def delete_profile(self):
        self.delete()

class Photos(models.Model):
    image_name = HTMLField()
    image = CloudinaryField('images/')
    caption= models.CharField(max_length=250)
    user = models.ForeignKey(User, on_delete=models.CASCADE, default=1)
    pub_date = models.DateTimeField(auto_now_add=True)
    

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

class Comments(models.Model):
    comment= models.CharField(max_length=255)
    user= models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.comment

class Like(models.Model):
    image=models.ForeignKey(Photos, on_delete = models.CASCADE,related_name="piclikes")
    liking=models.ForeignKey(User, on_delete = models.CASCADE,related_name="userlikes")

    def __str__(self):
        return self.liking

