from django.shortcuts import render, HttpResponseRedirect, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.db.models.deletion import SET_DEFAULT

from management.forms import AddadminForm

# Create your views here.
@login_required
def register(request):
    if request.method == 'POST':
        form = AddadminForm(request.POST)
        # print(request.POST)
        if form.is_valid():
            form.save()
            return redirect('index')
    else:
        form = AddadminForm()

    return render(request, 'add_admin.html', {'form': form})

@login_required
def delete_admin(request):
    return render(request, 'delete_admin.html')