import csv
import subprocess
import sys
from os import path
from os.path import split
from subprocess import check_output
from tabulate import tabulate
import gns3fy
import requests

from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required

from vmtopo.forms import CreatePGForm

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
    return render(request, 'topo.html')


@login_required
def del_port(request, pg_name):
    return render(request, 'vmtopo.html')