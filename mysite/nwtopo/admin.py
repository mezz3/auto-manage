from django.contrib import admin
from nwtopo.models import Template
# Register your models here.


class TemplateAdmin(admin.ModelAdmin):
    list_display = ['id', 'title', 'temp_amount']


admin.site.register(Template, TemplateAdmin)