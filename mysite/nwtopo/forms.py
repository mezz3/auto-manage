from django import forms


class CreateForm(forms.Form):
    temp_name = forms.CharField(max_length=255, required=False, label='Template name')
    temp_description = forms.CharField(max_length=255, required=False, label='Template description')