import subprocess
import sys
from os import path
from os.path import split
from subprocess import check_output

from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect, render

from nwtopo.forms import CreateForm, TemplateForm
from nwtopo.models import Template, Deploy


# Create your views here.
@login_required
def nwtopo(request):
    if request.method == 'POST':
        form = CreateForm(request.POST)
        if form.is_valid():
            print(request.POST)
            print(request.POST['temp_name'])

            temp_name = request.POST['temp_name']
            test = check_output([
                'python.exe',
                'static\\Scripts\\createfile.py',
                str(temp_name),
            ])

            Template.objects.create(
                temp_name=form.cleaned_data['temp_name']
            )
            return redirect('nwtopo')
    else:
        form = CreateForm()
    
    template_list = Template.objects.all()

    return render(request, 'nwtopo.html', {'form': form, 'template_list': template_list})


@login_required
def temp_del(request, temp_name):
    # temp_delete = check_output([
    #     'python.exe',
    #     'static\\Scripts\\delete_temp.py',
    #     str(temp_name),
    # ])

    temp = Template.objects.get(pk=temp_name)
    temp.delete()

    return redirect('nwtopo')


@login_required
def temp_clone(request):
    return redirect('nwtopo')


@login_required
def topo(request):
    return render(request, 'topo_nw.html')


@login_required
def deploy(request):
    if request.method == 'POST':
        form = TemplateForm(request.POST)
        if form.is_valid():
            # print(request.POST)
            print(request.POST)
            dic_data = request.POST
            amount = dic_data['temp_amount']
            name = dic_data['title']
            print(amount, name)
            print(type(amount))

            path_file = request.FILES
            print(path_file)

            name_path = path_file['temp_file']
            Deploy.objects.create(
                title=form.cleaned_data['title'],
                # temp_file=form.cleaned_data['temp_file'],
                temp_amount=form.cleaned_data['temp_amount'],
            )
            # test = check_output([
            #     'python.exe',
            #     'static\\Scripts\\sendfile.py',
            #     str(name_path),
            # ])

            return redirect('report')
    else:
        form = TemplateForm()
    return render(request, 'deploy.html', {'form': form})


@login_required
def report(request):
    # form = CreateTempForm(request.POST)
    return render(request, 'ip_report.html')
