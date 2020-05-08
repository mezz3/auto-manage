from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
import subprocess
import sys
from subprocess import check_output

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
    # form = CreateTempForm(request.POST, request.FILES)
    # if request.method == 'POST':
    #     if form.is_valid():
    #         form = CreateTempForm(request.POST)
    #         print(request.POST)
    #         # print(request.FILES)
    #         # amount = request.POST['vm_amount']
    #         # print(amount)
    #         # print(count)

    #         # clone = subprocess.Popen([
    #         #     'powershell.exe',
    #         #     'static\\Scripts\\createVM.ps1',
    #         #     '-vm_count', amount,
    #         #     '-count', str(count),
    #         # ], stdout=sys.stdout)
    #         # print(clone.communicate())
    #         return redirect('deploy')
    # else:
    #     form = CreateTempForm()
    if request.method == 'POST':
        form = CreateTempForm(request.POST, request.FILES)
        if form.is_valid():
            print(request.POST)
            print(request.FILES)
            # form.save()
            test = check_output([
                'python.exe',
                'static\\Scripts\\sendfile.py',
            ])
            # script = 

            return redirect('deploy')
    else:
        form = CreateTempForm()
    return render(request, 'deploy.html', {'form': form})


@login_required
def report(request):
    # form = CreateTempForm(request.POST)
    return render(request, 'ip_report.html')