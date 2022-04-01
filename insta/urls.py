from django.urls import path
from . import views, include


urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.Welcome,name = 'users-welcome'),]