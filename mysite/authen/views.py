from django.http import HttpResponse
from django.shortcuts import render


# Create your views here.
def login(request):
    return render(request, template_name='login.html')


def index(request):
    return render(request, template_name='index.html')
