"""gram URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from insta import views 
from django.urls import path, include,re_path

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.Welcome,name = 'welcome'),
    path('page/',views.Page,name = 'page'),
    path('accounts/', include('django_registration.backends.one_step.urls')),
    path('accounts/', include('django.contrib.auth.urls')),
    path('tinymce/', include('tinymce.urls')),
    path('new/photos', views.new_photos, name='new-photos'),
    
    path('search/', views.search, name='search'),
    path('profile/',views.profile,name="profile" ),
    path('updateprofile/', views.updateprofile, name='updateprofile'),
    path('image/<int:image_id>', views.single_image, name='image'),
    # path('comment/<int:photos_id>',views.commentFunction,name='comment'),
    re_path(r'^comment/(?P<image_id>\d+)$',views.commentFunction,name='comment'),

    # re_path(r'^like/(?P<image_id>\d+)', views.like, name='like'),

]
