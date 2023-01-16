from django import forms

from .models import UserForms


class ClientValidationForm(forms.ModelForm):
    class Meta:
        model = UserForms
        fields = ['name','email','phonenum','city','pincode',]
        
