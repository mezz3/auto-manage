from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def vmtopo(request):
    return render(request, template_name='vmtopo.html')


def topo(request):
    return render(request, template_name='topo.html')