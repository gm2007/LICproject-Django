from django.db import models

# Create your models here.
class UserForms(models.Model):
    name = models.CharField(max_length = 50)
    email = models.EmailField( max_length=254)
    phonenum = models.IntegerField(max_length=10)
    city = models.CharField(max_length=50)
    pincode = models.IntegerField(max_length=10)


