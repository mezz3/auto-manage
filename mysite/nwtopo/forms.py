from django import forms


TEMP_CHOICES =( 
    ("1", "Vlan test"), 
    ("2", "Inter VLAN"),
)


class CreateForm(forms.Form):
    temp_name = forms.CharField(max_length=255, required=False, label='Template name')
    temp_description = forms.CharField(max_length=255, required=False, label='Template description')


class CreateTempForm(forms.Form):
    temp = forms.ChoiceField(required=False, choices = TEMP_CHOICES, label='Template ที่ต้องการสร้าง')
    temp_file = forms.FileField(required=False, label='Template File ที่ต้องการสร้าง')
    temp_amount = forms.IntegerField(label='จำนวนที่ต้องการสร้าง', required=False)

    temp.widget.attrs.update({'class': 'form-control'})
    temp_file.widget.attrs.update({'class': 'form-control'})
    temp_amount.widget.attrs.update({'class': 'form-control'})