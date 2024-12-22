from django.db import models

# Create your models here.
class emp(models.Model):
    name = models.CharField(max_length=150)
    email= models.EmailField()
    phone= models.CharField(max_length=10)
    address =models.CharField(max_length=250)