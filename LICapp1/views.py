from .UserFom import UserForms
from django.shortcuts import render
from django.http import JsonResponse, HttpResponse
from django.views.generic.edit import FormView
from django.contrib.auth.forms import UserCreationForm

class StartHome(FormView):
    template_name = "LICapp1/index.html"
    form_class = UserCreationForm
    # usrfm_var = UserForms()
    # return HttpResponse({'Name': 'Newjoiner', 'sex':'male', 'dob':'18-09-2001' }),
    # return render(request, "LICapp1/index.html",{'form':usrfm_var})
# Create your views here.

# def form_validate(request):
#     usrfm_var = UserForms()
    