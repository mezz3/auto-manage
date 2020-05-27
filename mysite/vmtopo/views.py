import csv
import subprocess
import sys
from os import path
from os.path import split
from subprocess import check_output
from tabulate import tabulate
import gns3fy
import requests
import time

from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required

from vmtopo.forms import CreatePGForm, CreateVM_pgForm
from vmtopo.models import VM_pg

# Create your views here.
@login_required
def vmtopo(request):
    port_group = check_output([
        'powershell.exe',
        'static\\Scripts\\port_group.ps1',
    ])
    # print(port_group)
    txt = ''
    keep = port_group.split()
    for _ in keep:
        txt = txt + ' ' + _.decode('utf8')

    print(txt)
    b = {' Name Port User ---- ---- ---- 10.0.15.39 443 VSPHERE.LOCAL\Administrator ': '', 'VLanId': '', 'Name': '', ':': ''}
    for x,y in b.items():
        txt = txt.replace(x, y)
    txt = txt.split('   ')

    name_port = []
    vlan = []
    count = 0
    for arg in txt:
        if count % 2 == 0:
            name_port.append(arg.replace('  ', ''))
        else:
            vlan.append(arg)
        count += 1
    print(name_port)
    print(vlan)

    if request.method == 'POST':
        form = CreatePGForm(request.POST)
        if form.is_valid():
            print(request.POST)
            pg_name = request.POST['pg_name']
            pg_vlan = request.POST['pg_vlan']

            test = check_output([
                'powershell.exe',
                'static\\Scripts\\create_portgroup.ps1',
                str(pg_name),
                str(pg_vlan),
            ])
            return redirect('vmtopo')
    else:
        form = CreatePGForm()

    return render(request, 'vmtopo.html', {'form': form, 'name_port': name_port, 'vlan': vlan})


@login_required
def topo(request, pg_name):
    detail_pg = check_output([
        'powershell.exe',
        'static\\Scripts\\get_detailPG.ps1',
        str(pg_name),
    ])

    txt = ''
    keep = detail_pg.split()
    for _ in keep:
        txt = txt + ' ' + _.decode('utf8')

    b = {' Name Port User ---- ---- ---- 10.0.15.39 443 VSPHERE.LOCAL\Administrator ': '', 'PowerState': '', 'Name': '', ':': ''}
    for x,y in b.items():
        txt = txt.replace(x, y)
    txt = txt.split('   ')
    print(txt)

    name_vm = []
    state = []
    count = 0
    for arg in txt:
        if count % 2 == 0 and arg != '  Port User ---- ---- ---- 10.0.15.39 443 VSPHERE.LOCAL\\Administrator':
            name_vm.append(arg.replace('  ', ''))
        else:
            state.append(arg)
        count += 1
    print(name_vm)
    print(state)

    return render(request, 'topo.html', {'name_vm': name_vm, 'state': state})


@login_required
def start_vm(request, vm_name):
    start_vm = check_output([
        'powershell.exe',
        'static\\Scripts\\start_vm.ps1',
        str(vm_name),
    ])
    # print(pg_name)
    return redirect('vmtopo')


@login_required
def stop_vm(request, vm_name):
    stop_vm = check_output([
        'powershell.exe',
        'static\\Scripts\\stop_vm.ps1',
        str(vm_name),
    ])
    # print(pg_name)
    return redirect('vmtopo')


@login_required
def remove_vm(request, vm_name):
    remove_vm = check_output([
        'powershell.exe',
        'static\\Scripts\\deleteVM.ps1',
        str(vm_name),
    ])

    return redirect('vmtopo')


@login_required
def del_port(request, pg_name):
    del_pg = check_output([
        'powershell.exe',
        'static\\Scripts\\delete_port.ps1',
        str(pg_name),
    ])
    print('def delete port', pg_name)

    return redirect('vmtopo')


@login_required
def vm_pg(request):
    if request.method == 'POST':
        form = CreateVM_pgForm(request.POST)
        if form.is_valid():
            print(request.POST)
            vm_os = request.POST['vm_os']
            vm_name = request.POST['vm_name']

            VM_pg.objects.create(
                vm_name=form.cleaned_data['vm_name']
            )
            # pg_vlan = request.POST['pg_vlan']

            if vm_os == '1':
                vm_os = 'win10_vm_for_4thproject'
            elif vm_os == '2':
                pass

            test = check_output([
                'powershell.exe',
                'static\\Scripts\\createVM_pg.ps1',
                str(vm_os),
                str(vm_name),
            ])

            time.sleep(120)
            return redirect('createVM_pg')
    else:
        form = CreateVM_pgForm()

    return render(request, 'vm_pg.html', {'form': form})


@login_required
def createVM_pg(request):
    port_group = check_output([
        'powershell.exe',
        'static\\Scripts\\port_group.ps1',
    ])
    # print(port_group)
    txt = ''
    keep = port_group.split()
    for _ in keep:
        txt = txt + ' ' + _.decode('utf8')

    print(txt)
    b = {' Name Port User ---- ---- ---- 10.0.15.39 443 VSPHERE.LOCAL\Administrator ': '', 'VLanId': '', 'Name': '', ':': ''}
    for x,y in b.items():
        txt = txt.replace(x, y)
    txt = txt.split('   ')

    name_port = []
    vlan = []
    count = 0
    for arg in txt:
        if count % 2 == 0:
            name_port.append(arg.replace('  ', ''))
        else:
            vlan.append(arg)
        count += 1
    # print(name_port)
    # print(vlan)

    return render(request, 'create_pg.html', {'name_port': name_port, 'vlan': vlan})


@login_required
def choose_pg(request, pg_name):
    deploy_list = VM_pg.objects.all()
    lastest = VM_pg.objects.latest('id')
    vm_name = str(lastest.vm_name)

    print(vm_name, pg_name)
    port_group = check_output([
        'powershell.exe',
        'static\\Scripts\\choose_pg.ps1',
        str(vm_name),
        str(pg_name),
    ])
    return redirect('vmtopo')