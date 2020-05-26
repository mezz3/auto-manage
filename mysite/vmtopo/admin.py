from django.contrib import admin
from vmtopo.models import VM_pg
# Register your models here.

class VM_pgAdmin(admin.ModelAdmin):
    list_display = ['id', 'vm_name']

admin.site.register(VM_pg, VM_pgAdmin)