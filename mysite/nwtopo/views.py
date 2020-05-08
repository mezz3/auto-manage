import subprocess
import sys
from os import path
from os.path import split
from subprocess import check_output

from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect, render

from nwtopo.forms import CreateForm, TemplateForm
from nwtopo.models import Template


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
    if request.method == 'POST':
        form = TemplateForm(request.POST, request.FILES)
        if form.is_valid():
            # print(request.POST)
            print(request.POST)
            path_file = request.FILES
            print(path_file)
            name_path = path_file['temp_file']
            Template.objects.create(
                title=form.cleaned_data['title'],
                temp_file=form.cleaned_data['temp_file'],
                temp_amount=form.cleaned_data['temp_amount'],
            )
            test = check_output([
                'python.exe',
                'static\\Scripts\\sendfile.py',
                str(name_path),
            ])

            return redirect('report')
    else:
        form = TemplateForm()
    return render(request, 'deploy.html', {'form': form})


@login_required
def report(request):
    # form = CreateTempForm(request.POST)
    return render(request, 'ip_report.html')
