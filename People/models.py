from django.db import models

# Create your models here.
class People(models.Model):
    name = models.CharField(max_length=70)
    last_name = models.CharField(max_length=200)
    age = models.IntegerField()
    DOB =models.DateField(default = True, null = True, blank=True )
    relationship = models.CharField(max_length=300)