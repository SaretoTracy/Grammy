
from . import views, include
from django.urls import path,register_converter,include, re_path
from django.contrib.auth import views as auth_views
from . import views as app_views
from . import views
urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.Welcome,na me = 'welcome'),
    path('page/',views.Page,name = 'page'),
    path('accounts/', include('django_registration.backends.one_step.urls')),
    path('accounts/', include('django.contrib.auth.urls')),
    path('new/photos', views.new_photos, name='new-photos'),
    re_path(r'^like/(?P<image_id>\d+)', app_views.like, name='like'),
    path('like/<int:image_id>>', views.like, name='like'),
)

    ]

if settings.DEBUG:
        urlpatterns += static(settings.MEDIA_URL,
                              document_root=settings.MEDIA_ROOT)