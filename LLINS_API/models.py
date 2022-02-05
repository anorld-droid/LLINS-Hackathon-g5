from pickle import FALSE
from django.db import models


class PatientsData(models.Model):
    year = models.IntegerField()
    month = models.CharField()
    totalpatients = models.IntegerField()
    patientswithnets = models.IntegerField()
    patientswithoutnets = models.IntegerField()

    class Meta:
        ordering = ['year']


class Nets(models.Model):
    budgeted = models.IntegerField()
    issued = models.IntegerField()
