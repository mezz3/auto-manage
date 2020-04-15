from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def vmtopo(request):
    return render(request, 'vmtopo.html')