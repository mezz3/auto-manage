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

    temp.widget.attrs.update({'class': 'form-control'})