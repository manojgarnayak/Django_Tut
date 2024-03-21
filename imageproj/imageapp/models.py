from django.db import models

# Create your models here.

class Details(models.Model):
    name = models.CharField(max_length = 50)
    phone = models.CharField(max_length = 50)
    email = models.CharField(max_length = 100)
    password = models.CharField(max_length = 50)
    profile = models.ImageField()

    def __str__(self):
        return self.name