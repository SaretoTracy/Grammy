from .models import Photos,Comments, Profile
from django.contrib.auth.models import User
from django import forms
#......
class NewPhotosForm(forms.ModelForm):
   class Meta:
       model = Photos
       exclude = ['profile','likes','comments']

class CommentForm(forms.ModelForm):
    def __init__(self,*args,**kwargs):
        super().__init__(*args,**kwargs)
        self.fields['comment'].widget=forms.TextInput()
        self.fields['comment'].widget.attrs['placeholder']='Leave a comment...'
    class Meta:
        model = Comments
        fields = ('comment',)

class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        exclude = ['user', 'followers', 'following', 'posts']
      
       
