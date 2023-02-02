from django.shortcuts import render, redirect
from .models import UserForms
from .form import ClientValidationForm


def index(request):
    Var_pr = UserForms.objects.all()
    form=ClientValidationForm()
    if request.method == 'POST':
        # print(form.cleaned_data['name'], 'This is the ', 'requested data')
        if form.is_valid():
            print('data saved')
            form.save()
            return redirect(request,"LICapp1/index.html",{'form':form})
    print(Var_pr)
    return render(request,"LICapp1/index.html",{'form':form, 'Var_pr': Var_pr})

def FirstPgOpen(request):
    return render(request, "LICapp1/openpg1.html")