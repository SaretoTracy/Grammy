from django.shortcuts import render
from django.http  import HttpResponse
from django.contrib.auth.decorators import login_required


# Create your views here.
def Welcome(request):

    return render(request, 'welcome.html')


@login_required(login_url='/accounts/login/')
def Page(request):
    return render(request, 'page.html')
