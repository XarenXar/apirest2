from django.db import models

# Create your models here.
class Datos(models.Model):
    company_Id = models.CharField(max_length=100)
    zubale_Id = models.IntegerField(default=0)
    determinante = models.IntegerField(default=0)

