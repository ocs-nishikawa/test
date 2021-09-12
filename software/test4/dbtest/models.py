from django.db import models

class RaspiTable(models.Model):
    user_id = models.TextField(blank=True, null=True)
    pass_field = models.TextField(db_column='pass', blank=True, null=True)  # Field renamed because it was a Python reserved word.
    classroom_name = models.TextField(blank=True, null=True)
    equipment_number = models.TextField(blank=True, null=True)
    concentration = models.IntegerField(blank=True, null=True)
    date = models.TextField(blank=True, null=True)
    number = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'RasPi_table'
