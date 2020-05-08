from django.shortcuts import render
from django.contrib.auth.decorators import login_required

from nwtopo.forms import CreateForm, CreateTempForm

# Create your views here.
@login_required
def nwtopo(request):
    form = CreateForm(request.POST)
    return render(request, 'nwtopo.html', {'form': form})


@login_required
def topo(request):
    return render(request, 'topo_nw.html')


@login_required
def deploy(request):
    form = CreateTempForm(request.POST, request.FILES)
    return render(request, 'deploy.html', {'form': form})


@login_required
def report(request):
    # form = CreateTempForm(request.POST)
    return render(request, 'ip_report.html')