from .models import Photos,Comments
from django import forms
#......
class NewPhotosForm(forms.ModelForm):
   class Meta:
       model = Photos
       exclude = ['profile','likes']

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comments
        exclude = ['user']
      
       
