# from crypt import methods
from django.contrib import messages
from django.contrib.auth import logout
from django.contrib.auth.models import User, auth
from django.http import HttpResponse
from django.shortcuts import redirect, render


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
            print('user: ')
            return redirect('/index')
        else:
            messages.info(request, 'ชื่อผู้ใช้งาน หรือรหัสผิดพลาด')
            return redirect('login')

    else:
        return render(request, template_name='login.html')


def log_out(request):
    auth.logout(request)
    return redirect('login')


def index(request):
    return render(request, template_name='index.html')
