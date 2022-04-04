from django.shortcuts import render, redirect
from django.http  import HttpResponse
from .models import Photos,Comments,Profile
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

def like_post(request):
    user = request.user
    if request.method == "POST":
        image_id = request.POST.get('image_id')
        post = Photos.objects.get(id=image_id)
        
        if user in post.liked.all():
            post.liked.remove(user)
        else:
            post.liked.add(user)
        like, created = Like.objects.get_or_create(user=user,image_id=image_id)
        
        if not created:
            if like.value == 'Like':
                like.value = 'Unlike'
            else:
                like.value = 'Like' 
        like.save()           
    return redirect('singlepage.html')


@login_required(login_url='/accounts/login/')
def commentFunction(request,image_id):
  commentform = CommentForm()
  photo = Photos.objects.filter(pk = image_id).first()
  if request.method == 'POST':
    commentform = CommentForm(request.POST)
    if commentform.is_valid():
      comment = commentform.save(commit = False)
      comment.user = request.user
      comment.photo = photo
      comment.save() 
    else:
      commentform= CommentForm()
  return redirect('singlepost.html',{"commentform": commentform})

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
@login_required(login_url='/accounts/login/')
def single_image(request, image_id):
    try:
        image = Photos.objects.get(id=image_id)
    except ObjectDoesNotExist:
        raise Http404()

    return render(request, 'singlepost.html', {'image': image})
