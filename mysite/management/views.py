import subprocess
import sys
from subprocess import check_output
from uu import decode

from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.db.models.deletion import SET_DEFAULT
from django.shortcuts import HttpResponseRedirect, redirect, render

import Scripts
from management.forms import AddadminForm, AdminSearchForm, CreateVMForm


# Create your views here.
@login_required
def register(request):
    if request.method == 'POST':
        form = AddadminForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('delete_admin')
    else:
        form = AddadminForm()

    return render(request, 'add_admin.html', {'form': form})


@login_required
def search_admin(request):
    form = AdminSearchForm(request.GET)

    if form.is_valid():
        username = form.cleaned_data['username']
        user_list = User.objects.filter(username__icontains=username)
    else:
        user_list = []

    return render(request, 'delete_admin.html', {'form':form, 'user_list':user_list})


@login_required
def delete(request, user_id):
    user = User.objects.get(pk=user_id)
    user.delete()

    return redirect('delete_admin')


@login_required
def manage_vm(request):
    lastest = check_output([
        'powershell.exe',
        'static\\Scripts\\getVM.ps1',
    ])
    name_list = []
    keep = lastest.split()

    name_test = []
    list_test = []
    count = 1
    for _ in keep:
        name_test.append(_.decode('utf8'))
    for arg in name_test:
        if 'gns3vm-' in arg:
            list_test.append(arg)
            count += 1
    print(name_test)
    print(list_test)
    print(count)

    if request.method == 'POST':
        form = CreateVMForm(request.POST)
        if form.is_valid():
            print(request.POST)
            amount = request.POST['vm_amount']
            print(amount)
            print(count)

            clone = subprocess.Popen([
                'powershell.exe',
                'static\\Scripts\\createVM.ps1',
                '-vm_count', amount,
                '-count', str(count),
            ], stdout=sys.stdout)
            print(clone.communicate())
            return redirect('manage_vm')
    else:
        form = CreateVMForm()
    return render(request, 'managevm.html', {'form': form})


@login_required
def delete_vm(request):
    test = check_output([
        'powershell.exe',
        'static\\Scripts\\getVM.ps1',
    ])
    name_list = []
    keep = test.split()

    name_test = []
    list_test = []
    for _ in keep:
        name_test.append(_.decode('utf8'))
    for arg in name_test:
        if 'gns3vm-' in arg:
            list_test.append(arg)

    print(name_test)
    print(list_test)
    print('___________________')
    # print(name_list)
    # print(keep)
    # print(vm.sys.stdout)
    # vm_list = vm.communicate()
    return render(request, 'delete_vm.html', {'list_test': list_test})


def del_vm(request, vm_name):
    delete = check_output([
        'powershell.exe',
        'static\\Scripts\\deleteVM.ps1',
        '-vm_name', vm_name,
    ])
    print(vm_name)
    return redirect('delete_vm')
