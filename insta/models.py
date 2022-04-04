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
    liked = models.ManyToManyField(User,blank=True,related_name='liked')
    caption= models.CharField(max_length=250)
    user = models.ForeignKey(User, on_delete=models.CASCADE, default=1)
    pub_date = models.DateTimeField(auto_now_add=True)
    

    def __str__(self):
        return self.caption
    def save_photos(self):
        self.save()
    def delete_photos(self):
        self.delete()
    @property 
    def save_comments(self):
        self.save()
    
    @classmethod
    def display_photos(cls):
        photos = cls.objects.all().order_by('-posted_at')
        return photos
    
 
    @property
    def saved_comments(self):
        return self.comments.all()
    @classmethod
    
    def search_by_image_name(cls, searchname):
        photos = cls.objects.filter(image_name__icontains = searchname).all()
        return photos
    def delete_post(self):
        self.delete()

    @classmethod
    def display_all(cls):
        '''
        Function that dislays post information
        '''
        caption = cls.objects.all()
        return caption
    @property
    def num_likes(self):
        return self.likes.all().count()
LIKE_CHOICES = (
    ('Like', 'Like'),
    ('Unlike','Unlike'),
)    

class Comments(models.Model):
    comment= models.CharField(max_length=255)
    user= models.ForeignKey(User, on_delete=models.CASCADE)
    pub_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.comment

    def save_comment(self):
        self.save()
    @classmethod
    def display_comments_by_photoId(cls,photos_id):
        comments = cls.objects.filter(photos_id = photos_id)
        return comments


