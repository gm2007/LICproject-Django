from django.urls import path
from .views import StartHome

urlpatterns = [
    path('', StartHome.as_view())
]
