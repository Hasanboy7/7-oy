from .models import CrudModel
from django import forms

class CrudForm(forms.ModelForm):
    class Meta:
        model=CrudModel
        fields='__all__'
        