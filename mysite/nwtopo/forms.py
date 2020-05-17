from django import forms
from pkg_resources import require
from django.core.exceptions import ValidationError


class CreateForm(forms.Form):
    temp_name = forms.CharField(max_length=100, required=True, label='Template name')

    temp_name.widget.attrs.update({'class': 'form-control'})

    def clean_temp_name(self):
        temp_name = self.cleaned_data['temp_name']
        if temp_name == None or temp_name == '':
            raise  forms.ValidationError("ยังไม่ได้ทำการระบุชื่อ")
        return temp_name


class TemplateForm(forms.Form):
    temp_amount = forms.IntegerField(label='จำนวนที่ต้องการสร้าง', required=False)


class DeploySearchForm(forms.Form):
    deploy_name = forms.CharField(max_length=255, label='ค้นหาชื่อโปรเจค', required=False)

    deploy_name.widget.attrs.update({'class': 'form-control'})