from django.urls import path
from . import views, include


urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.Welcome,name = 'users-welcome'),
    path('accounts/', include('django_registration.backends.one_step.urls')),
    path('accounts/', include('django.contrib.auth.urls')),
    ]