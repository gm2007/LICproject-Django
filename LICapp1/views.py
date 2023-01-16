from django.shortcuts import render

from .form import ClientValidationForm


def index(request):
    form=ClientValidationForm()
    return render(request,"LICapp1/index.html",{'form':form})