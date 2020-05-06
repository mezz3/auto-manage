from django.shortcuts import render, HttpResponseRedirect, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.db.models.deletion import SET_DEFAULT
import subprocess, sys, Scripts

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
    if request.method == 'POST':
        form = CreateVMForm(request.POST)
        if form.is_valid():
            # form.save()
            print(request.POST)
            clone = subprocess.Popen([
                'powershell.exe',
                'static\\Scripts\\createVM.ps1',
            ], stdout=sys.stdout)
            print(clone.communicate())
            return redirect('manage_vm')
    else:
        form = CreateVMForm()
    return render(request, 'managevm.html', {'form': form})


@login_required
def delete_vm(request):
    return render(request, 'delete_vm.html')