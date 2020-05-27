from django import forms
from pkg_resources import require
from django.core.exceptions import ValidationError


OS_CHOICES = [
    (1, 'Windows10'),
    (2, 'Linux'),
    ]


class CreatePGForm(forms.Form):
    pg_name = forms.CharField(max_length=100, required=True, label='PortGroup name')
    pg_vlan = forms.IntegerField(label='Vlan ID', required=True)

    pg_name.widget.attrs.update({'class': 'form-control'})
    pg_vlan.widget.attrs.update({'class': 'form-control'})

    def clean_pg_name(self):
        pg_name = self.cleaned_data['pg_name']
        if pg_name == None or pg_name == '':
            raise  forms.ValidationError("ยังไม่ได้ทำการระบุชื่อ")
        if ' ' in pg_name:
            raise  forms.ValidationError("ห้ามมีช่องว่างภายในชื่อ")
        return pg_name

    def clean_pg_vlan(self):
        pg_vlan = self.cleaned_data['pg_vlan']
        if pg_vlan == None or pg_vlan == '' or pg_vlan < 0:
            raise  forms.ValidationError("ยังไม่ได้ทำการระบุจำนวน")
        return pg_vlan


class CreateVM_pgForm(forms.Form):
    vm_os = forms.ChoiceField(choices = OS_CHOICES, required=True, label='VM OS')
    vm_name = forms.CharField(max_length=100, required=True, label='VM name')
    # vm_vlan = forms.IntegerField(label='Vlan ID', required=True)

    vm_name.widget.attrs.update({'class': 'form-control'})
    vm_os.widget.attrs.update({'class': 'form-control'})
    # vm_vlan.widget.attrs.update({'class': 'form-control'})
