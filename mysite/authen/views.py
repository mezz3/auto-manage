from django.contrib.auth import logout
from django.http import HttpResponse
from django.shortcuts import redirect, render


# Create your views here.
def login(request):
    return render(request, template_name='login.html')


def log_out(request):
    logout(request)
    return redirect('login')


def index(request):
    return render(request, template_name='index.html')
