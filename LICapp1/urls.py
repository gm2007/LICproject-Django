from django.urls import path

from .views import *

urlpatterns = [
    path('', index,name='home'),
    path('Open1pg', FirstPgOpen,name='Open1pg'),

]
