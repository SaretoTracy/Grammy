from django.shortcuts import render
from django.http  import HttpResponse
from .models import Photos
from django.contrib.auth.decorators import login_required


# Create your views here.
def Welcome(request):

    

    return render(request, 'welcome.html')


@login_required(login_url='/accounts/login/')
def Page(request):
    # Function that gets the date
    post = Photos.objects.all()

    
  
    
    return render(request, 'page.html',{'posts':post})
