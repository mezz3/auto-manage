from django.shortcuts import render
from django.contrib.auth.decorators import login_required

# Create your views here.
@login_required
def nwtopo(request):
    return render(request, template_name='nwtopo.html')

@login_required
def topo(request):
    return render(request, template_name='topo_nw.html')