from django.shortcuts import render
from django.http  import HttpResponse
from .models import Photos
from django.contrib.auth.decorators import login_required
from .forms import NewPhotosForm

# Create your views here.
def Welcome(request):

    

    return render(request, 'welcome.html')


@login_required(login_url='/accounts/login/')
def Page(request):
    # Function that gets the date
    post = Photos.objects.all()
    
    return render(request, 'page.html',{'posts':post})

@login_required(login_url='/accounts/login/')
def new_photos(request):
   current_user = request.user
   if request.method == 'POST':
       form = NewPhotosForm(request.POST, request.FILES)
       if form.is_valid():
           photos = form.save(commit=False)
           photos.editor = current_user
           photos.save()
       return redirect('page')
 
   else:
       form = NewPhotosForm()
   return render(request, 'new_photos.html', {"form": form})

