from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required

# Create your views here.
@login_required
def vmtopo(request):
    return render(request, template_name='vmtopo.html')

@login_required
def topo(request):
    return render(request, template_name='topo.html')