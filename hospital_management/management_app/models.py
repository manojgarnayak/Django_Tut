from django.db import models

# Create your models here.

class Details(models.Model):
    sno = models.IntegerField(primary_key = True)
    patient_details = models.CharField(max_length = 50) 
    phone = models.IntegerField()
    email_id = models.EmailField()
    disease_desc = models.CharField(max_length = 150)

    def __str__(self):
        return self.patient_details