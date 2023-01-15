from .models import UserForms
from django.forms import BaseForm, ModelForm
from django.contrib.auth.forms import UserCreationForm
class UsrFom(ModelForm):
    class Meta:
        model = UserForms
        fields = '__all__'
        
        
