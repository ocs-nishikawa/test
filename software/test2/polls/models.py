from django.db import models
from django.utils import timezone

class Userid_Table(models.Model):
    user_id = models.CharField(primary_key=True , max_length = 40 , blank=False,null=False, default="Not entered")
    user_pw = models.CharField( max_length= 40 , blank=False,null=False, default="Not entered")

class Classroom_Table(models.Model):
    classroom_id = models.AutoField(primary_key=True , max_length = 40 , blank=False , null=False)
    classroom_name = models.TextField(blank=False , null=False , max_length= 40 , default="Not entered")
    user_id = models.CharField( max_length = 40 , blank=False,null=False, default="Not entered")
    equipment_number = models.TextField(blank=False, null=False , default="Not entered" , max_length= 32)

class Co2_Table(models.Model):
    co2_id = models.AutoField(primary_key=True , max_length = 40 , blank=False , null=False, default="Not entered")
    CO2conce = models.IntegerField(blank=False , null=False, default="Not entered")
    date = models.DateTimeField(blank=False , null=False , default=timezone.now)
    peoplenumber = models.IntegerField(blank=False , null=False , default= '-1')
    classroom_id = models.CharField( max_length = 40 , blank=False , null=False, default="Not entered")