
from . import views, include
from django.urls import path,register_converter,include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.Welcome,name = 'welcome'),
    path('',views.Page,name = 'page'),
    path('accounts/', include('django_registration.backends.one_step.urls')),
    path('accounts/', include('django.contrib.auth.urls')),
    ]