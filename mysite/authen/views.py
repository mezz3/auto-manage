# from crypt import methods
from django.contrib import messages
from django.contrib.auth import logout
from django.contrib.auth.models import User, auth
from django.http import HttpResponse
from django.shortcuts import redirect, render
from django.contrib.auth.decorators import login_required
# from Script import VMware.VimAutomation.Core
import subprocess, sys, Scripts


# Create your views here.
def login(request):
    if request.user.is_authenticated:
        return redirect('/index')
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        user = auth.authenticate(username=username, password=password)
        if user is not None:
            auth.login(request, user)
            # print('user: ')
            # import subprocess
            handle = subprocess.Popen([
                'powershell.exe',
                'static\\Scripts\\login.ps1',
            ], stdout=sys.stdout)
            # output = handle.stdout.read().decode('utf-8')
            print(handle.communicate())
            return redirect('/index')
        else:
            messages.info(request, 'ชื่อผู้ใช้งาน หรือรหัสผิดพลาด')
            return redirect('login')

    else:
        return render(request, template_name='login.html')

@login_required
def change_password(request):
    context = {}
    if request.method == 'POST':
        username = request.user
        password1 = request.POST.get('password1')
        password2 = request.POST.get('password2')

        if password1 == password2:
            username.set_password(password1)
            username.save()   
            logout(request)
            return redirect('login')
        else:
            context['error'] = 'รหัสผ่านไม่ตรงกัน.'

    return render(request, template_name='change_password.html' , context=context)


def log_out(request):
    auth.logout(request)
    return redirect('login')

@login_required
def index(request):
    return render(request, template_name='index.html')

@login_required
def profile(request):
    return render(request, template_name='profile.html')
