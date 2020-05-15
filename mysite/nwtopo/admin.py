from django.contrib import admin
from nwtopo.models import Deploy, Template
# Register your models here.

class TemplateAdmin(admin.ModelAdmin):
    list_display = ['id', 'temp_name']

class DeployAdmin(admin.ModelAdmin):
    list_display = ['id', 'title', 'temp_amount']


admin.site.register(Deploy, DeployAdmin)
admin.site.register(Template, TemplateAdmin)