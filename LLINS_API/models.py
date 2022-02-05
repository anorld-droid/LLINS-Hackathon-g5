from pickle import FALSE
from django.db import models


class PatientsData(models.Model):
    year = models.IntegerField()
    month = models.CharField(max_length=10)
    totalpatients = models.IntegerField()
    patientswithnets = models.IntegerField()
    patientswithoutnets = models.IntegerField()


class Nets(models.Model):
    year = models.IntegerField()
    month = models.CharField(max_length=10)
    budgeted = models.IntegerField()
    issued = models.IntegerField()
