
from . import views, include
from django.urls import path,register_converter,include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.Welcome,na me = 'welcome'),
    path('page/',views.Page,name = 'page'),
    path('accounts/', include('django_registration.backends.one_step.urls')),
    path('accounts/', include('django.contrib.auth.urls')),
    ]

if settings.DEBUG:
        urlpatterns += static(settings.MEDIA_URL,
                              document_root=settings.MEDIA_ROOT)