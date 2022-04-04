from django.shortcuts import render, redirect
from django.http  import HttpResponse
from .models import Photos,Comments,Like,Profile
from django.contrib.auth.decorators import login_required
from .forms import NewPhotosForm,CommentForm,ProfileForm

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

@login_required(login_url='/accounts/login/')
def search(request):
    if 'image' in request.GET and request.GET['image']:
        searchname = request.GET.get('image')
        searchimage= Photos.search_by_image_name(searchname)
        message = f"{searchname}"

        return render(request, 'search.html', {"message": message, "image": searchimage})
    else:
        message ="You havent searched any images "
        return render(request, 'search.html',{"message": message})

@login_required(login_url='accounts/login/')

@login_required(login_url='/accounts/login/')
def profile(request):
    image = Photos.objects.all()
    profile = Profile.objects.all()
    return render(request, 'profile.html', {"profile": profile, "image": image})


@login_required(login_url='/accounts/login/')
def updateprofile(request):
    current_user = request.user
    if request.method == 'POST':
        profileform = ProfileForm(request.POST, request.FILES)
        if profileform.is_valid():
            profile = profileform.save(commit=False)
            profile.user = current_user
            profile.save()
        return redirect('profile')
    else:
        profileform= ProfileForm()
    return render(request, 'update.html', {'profileform': profileform})