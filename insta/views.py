from django.shortcuts import render
from django.http  import HttpResponse
from .models import Photos
from django.contrib.auth.decorators import login_required


# Create your views here.
def Welcome(request):

    # Function that gets the date
    post = Photos.objects.all()

    return render(request, 'welcome.html',{'posts':post})


@login_required(login_url='/accounts/login/')
def Page(request):

    
  
    
    return render(request, 'page.html')
