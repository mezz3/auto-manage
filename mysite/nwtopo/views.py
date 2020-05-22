import subprocess
import sys
from os import path
from os.path import split
import requests
from subprocess import check_output
import gns3fy
from tabulate import tabulate

from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect, render
from django.views.generic import RedirectView
from django.http import HttpResponse, HttpResponseRedirect

from nwtopo.forms import CreateForm, TemplateForm, DeploySearchForm
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
def create_topo(request, temp_name):
    # scraping data to get id
    url = 'http://10.0.15.21/v2/projects'
    web_data = requests.get(url)
    text = web_data.json()

    dic = {}
    for i in text:
        key = i['name']
        if key not in dic.keys():
            dic[key] = i['project_id']

    # get id project!
    name = temp_name
    temp_id = dic[name]
    print(temp_id, name)



    return HttpResponseRedirect('http://10.0.15.21/static/web-ui/server/1/project/' + temp_id)


@login_required
def deploy(request):
    if request.method == 'POST':
        form = TemplateForm(request.POST)
        if form.is_valid():
            print(request.POST)
            print('******')

            Deploy.objects.create(
                temp_amount=form.cleaned_data['temp_amount']
            )
            return redirect('deploy_temp')
    else:
        form = TemplateForm()

    return render(request, 'deploy.html', {'form': form})


@login_required
def deploy_temp(request):
    template_list = Template.objects.all()
    clone_list = Clone.objects.all()
    keep = []
    for i in clone_list:
        arg = i.name_clone
        keep.append(arg)
    return render(request, 'deploy_temp.html', {'template_list': template_list, 'keep': keep})


@login_required
def deploy_temp_succ(request, temp_name):
    print('--------------------')
    deploy_list = Deploy.objects.all()
    lastest = Deploy.objects.latest('id')
    num = int(lastest.temp_amount)
    temp_name = temp_name
    print(type(lastest), lastest.temp_amount, temp_name)

    for i in range(num):
        test = check_output([
            'python.exe',
            'static\\Scripts\\clone_file.py',
            str(temp_name),
        ])
    return redirect('report')


@login_required
def report(request):
    # form = ItemSearchForm(request.GET)
    # if form.is_valid():
    #     item_name = form.cleaned_data['item_name']

    #     item_list = Item.objects.filter(item_name__icontains=item_name)
        
    template_list = Template.objects.all()

    url = 'http://10.0.15.21/v2/projects'
    web_data = requests.get(url)
    text = web_data.json()

    dic = {}
    for i in text:
        key = i['name']
        if key not in dic.keys():
            dic[key] = i['project_id']
    keep_deploy = []
    for i in dic.keys():
        keep_deploy.append(i)
    print(keep_deploy)
    temp_template = []
    for temp in template_list:
        temp_template.append(temp.temp_name)
    print(temp_template)

    temp_deploy = set(keep_deploy) - set(temp_template)
    print(temp_deploy)
    
    return render(request, 'ip_report.html', {'temp_template': temp_template, 'temp_deploy': temp_deploy})


@login_required
def create_report(request, temp_name):
    template_list = Template.objects.all()

    url = 'http://10.0.15.21/v2/projects'
    web_data = requests.get(url)
    text = web_data.json()

    dic = {}
    for i in text:
        key = i['name']
        if key not in dic.keys():
            dic[key] = i['project_id']
    keep_deploy = []
    for i in dic.keys():
        keep_deploy.append(i)
    print(keep_deploy)
    temp_template = []
    for temp in template_list:
        temp_template.append(temp.temp_name)
    print(temp_template)

    temp_deploy = set(keep_deploy) - set(temp_template)
    print(temp_deploy)

    report = []
    for i in temp_deploy:
        # print('for:', i)
        if temp_name in i:
            # print('if', i)
            if len(i) <= len(temp_name)+3:
                report.append(i)
    print('test***************', report)

    # create report csv
    for i in report:
        # gns3_server = gns3fy.Gns3Connector("http://10.0.15.21")
        # lab = gns3fy.Project(name=i, connector=gns3_server)
        # nodes_summary = lab.nodes_summary(is_print=False)
        # print(tabulate(nodes_summary, headers=["Node", "Status", "Console Port", "ID"]))
        print(i)

    return render(request, 'file_report.html')


@login_required
def file_report(request):
    return render(request, 'file_report.html')


@login_required
def deploy_del(request, deploy_name):
    temp_delete = check_output([
        'python.exe',
        'static\\Scripts\\delete_temp.py',
        str(deploy_name),
    ])

    return redirect('report')