from django.db import models

# Create your models here.
class LoginDetail(models.Model):
    fullname =  models.CharField(max_length=50)
    password =  models.CharField(max_length=50)
    email = models.CharField(max_length=50)