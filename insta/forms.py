from .models import Photos,Comments, Profile
from django.contrib.auth.models import User
from django import forms
#......
class NewPhotosForm(forms.ModelForm):
   class Meta:
       model = Photos
       exclude = ['profile','likes',Comments]

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comments
        exclude = ['user']


class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        exclude = ['user', 'followers', 'following', 'posts']
      
       
