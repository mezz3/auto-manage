import subprocess
import sys
from os import path
from os.path import split
from subprocess import check_output

from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect, render

from nwtopo.forms import CreateForm, TemplateForm
from nwtopo.models import Clone, Deploy, Template


# Create your views here.
@login_required
def nwtopo(request):
    template_list = Template.objects.all()
    clone_list = Clone.objects.all()
    keep = []
    for i in clone_list:
        arg = i.name_clone
        keep.append(arg)
    print(keep)

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

    return render(request, 'nwtopo.html', {'form': form, 'template_list': template_list, 'keep': keep})


@login_required
def temp_del(request, temp_id, temp_name):
    temp_delete = check_output([
        'python.exe',
        'static\\Scripts\\delete_temp.py',
        str(temp_name),
    ])

    temp = Template.objects.get(pk=temp_id)
    temp.delete()

    name_clone = temp_name
    clone = Clone.objects.filter(name_clone=temp_name)
    clone.delete()

    return redirect('nwtopo')


@login_required
def temp_clone(request, temp_name):
    clone = check_output([
        'python.exe',
        'static\\Scripts\\clone_file.py',
        str(temp_name),
    ])

    clone_list = Clone.objects.all()
    all_clone = []
    count = 0
    for i in clone_list:
        arg = i.name_clone
        all_clone.append(arg)
        count += 1

    # count = 1
    if count == 0:
        Template.objects.create(
            temp_name=temp_name + "-" + str(1)
        )
        Clone.objects.create(
            name_clone=temp_name + "-" + str(1)
        )
    else:
        Template.objects.create(
            temp_name=temp_name + "-" + str(count+1)
        )
        Clone.objects.create(
            name_clone=temp_name + "-" + str(count+1)
        )

    return redirect('nwtopo')


@login_required
def topo(request):
    return render(request, 'topo_nw.html')


@login_required
def deploy(request):
    if request.method == 'POST':
        form = TemplateForm(request.POST)
        if form.is_valid():
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

            return redirect('report')
    else:
        form = TemplateForm()
    return render(request, 'deploy.html', {'form': form})


@login_required
def report(request):
    return render(request, 'ip_report.html')
