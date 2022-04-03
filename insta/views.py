from django.shortcuts import render, redirect
from django.http  import HttpResponse
from .models import Photos,Comments,Like
from django.contrib.auth.decorators import login_required
from .forms import NewPhotosForm,CommentForm

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

def like(request, photos_id):
    current_user=request.user
    image=Photos.objects.get(id=photos_id)
    new_like.created=like.objects.get_or_create(liker=current_user,image=image)
    new_like.save ()

    return HttpResponseRedirect(request.Meta['HTTP_REFERER'])

@login_required(login_url='/accounts/login/')
def comment(request):
    current_user = request.user
    if request.method == 'POST':
        form = CommentForm(request.POST, request.FILES)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.user = current_user
            comment.save()
        return redirect('home')
    else:
        form= CommentForm()
    return render(request, 'home', {'form': form})


