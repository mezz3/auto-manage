from django import forms
from pkg_resources import require
from django.core.exceptions import ValidationError


class CreatePGForm(forms.Form):
    pg_name = forms.CharField(max_length=100, required=True, label='PortGroup name')
    pg_vlan = forms.IntegerField(label='Vlan ID', required=True)

    pg_name.widget.attrs.update({'class': 'form-control'})
    pg_vlan.widget.attrs.update({'class': 'form-control'})

    def clean_pg_name(self):
        pg_name = self.cleaned_data['pg_name']
        if pg_name == None or pg_name == '':
            raise  forms.ValidationError("ยังไม่ได้ทำการระบุชื่อ")
        return pg_name

    def clean_pg_vlan(self):
        pg_vlan = self.cleaned_data['pg_vlan']
        if pg_vlan == None or pg_vlan == '' or pg_vlan < 0:
            raise  forms.ValidationError("ยังไม่ได้ทำการระบุจำนวน")
        return pg_vlan


# class TemplateForm(forms.Form):
#     temp_amount = forms.IntegerField(label='จำนวนที่ต้องการสร้าง', required=False)


# class DeploySearchForm(forms.Form):
#     deploy_name = forms.CharField(max_length=255, label='ค้นหาชื่อโปรเจค', required=False)

#     deploy_name.widget.attrs.update({'class': 'form-control'})