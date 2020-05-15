from django import forms
from pkg_resources import require
from django.core.exceptions import ValidationError

TEMP_CHOICES =( 
    ("1", "Vlan test"), 
    ("2", "Inter VLAN"),
)


class CreateForm(forms.Form):
    temp_name = forms.CharField(max_length=255, required=False, label='Template name')
    # temp_description = forms.CharField(max_length=255, required=False, label='Template description')

    temp_name.widget.attrs.update({'class': 'form-control'})

    def clean_temp_name(self):
        temp_name = self.cleaned_data['temp_name']
        if temp_name == None:
            raise  forms.ValidationError("ยังไม่ได้ทำการระบุชื่อ")
        return temp_name

class TemplateForm(forms.Form):
    title = forms.ChoiceField(required=False, choices = TEMP_CHOICES, label='Template ที่ต้องการสร้าง')
    # title = forms.CharField(required=False, label='ชื่อ Template ที่ต้องการสร้าง')
    # temp_file = forms.FileField(required=False, label='Template File')
    temp_amount = forms.IntegerField(label='จำนวนที่ต้องการสร้าง', required=False)

    # temp.widget.attrs.update({'class': 'form-control'})
    title.widget.attrs.update({'class': 'form-control'})
    # temp_file.widget.attrs.update({'class': 'form-control'})
    temp_amount.widget.attrs.update({'class': 'form-control'})

    def clean_temp_amount(self):
        temp_amount = self.cleaned_data['temp_amount']
        try:
            if temp_amount <= 0:
                raise  forms.ValidationError("จำนวนที่ต้องการ deploy ต้องมากกว่า 0")
            return temp_amount
        except TypeError:
            raise  forms.ValidationError("กรุณาใส่จำนวนที่ต้องการ deploy")
            return temp_amount

    # def clean_temp_file(self):
    #     temp_file = self.cleaned_data['temp_file']
    #     if temp_file == None:
    #         raise  forms.ValidationError("ยังไม่ได้ทำการเลือกไฟล์")
    #     return temp_file

    def clean_title(self):
        title = self.cleaned_data['title']
        if title == None:
            raise  forms.ValidationError("ยังไม่ได้ทำการระบุชื่อ")
        return title
