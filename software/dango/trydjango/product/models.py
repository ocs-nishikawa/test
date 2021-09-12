from django.db import models
from django.db.models.expressions import F
from django.utils import timezone

# Create your models here.
class Product(models.Model):
    userid = models.CharField( max_length = 40 , )
    passfield = models.CharField( max_length= 40 , ) 
    classroomname = models.TextField(blank=True , null=True , max_length= 40 , default="no name")
    equipmentnumber = models.TextField(blank=True, null=True , default= 'no name' , max_length= 32)
    CO2conce = models.IntegerField(blank=True, null=True )
    date = models.DateTimeField(blank=True, null=False , default=timezone.now)
    peoplenumber = models.IntegerField(blank=True, null=False , default= '-1' )