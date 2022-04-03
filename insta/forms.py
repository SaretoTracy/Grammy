from .models import Photos
from django import forms
#......
class NewPhotosForm(forms.ModelForm):
   class Meta:
       model = Photos
       exclude = ['profile']
      
       
