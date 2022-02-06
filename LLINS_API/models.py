from django.db import models
import datetime


class Net(models.Model):
    YEAR_CHOICES = []
    for r in range(2019, (datetime.datetime.now().year + 1)):
        YEAR_CHOICES.append((r, r))
    Year = models.IntegerField('year', choices=YEAR_CHOICES, default=datetime.datetime.now().year)
    MONTH_CHOICE = [(m, m) for m in range(1, 13)]
    Month = models.IntegerField(choices=MONTH_CHOICE, default=datetime.datetime.now().month)
    CountyChoices = (
        ('kisumu', 'Kisumu'),
        ('vihiga', 'Vihiga'),
        ('busia', 'Busia'),
    )
    County = models.CharField(max_length=30, choices=CountyChoices, default='Kisumu')
    subCounty_choices = (
        ('kisumu west', 'Kisumu West'),
        ('kisumu central', 'Kisumu Central'),
        ('kisumu east', 'Kisumu East'),
        ('seme', 'Seme'),
        ('muhoroni', 'Muhoroni'),
        ('nyando', 'Nyando'),
        ('nyakach', 'Nyakach'),
        ('sabatia', 'Sabatia,'),
        ('vihiga', 'vihiga'),
        ('luanda', 'Luanda'),
        ('emuhaya', 'Emuhaya'),
        ('hamisi', 'Hamisi'),
        ('teso north', 'Teso North'),
        ('teso south', 'Teso South'),
        ('nambale', 'Nambale'),
        ('matayos', 'Matayos'),
        ('butula', 'Butula'),
        ('samia', 'Samia'),
        ('bunyala', 'Bunyala'),
    )
    SubCounty = models.CharField(max_length=30, choices=subCounty_choices, default='muhoroni')
    netsProvided = models.IntegerField()
    netsIssued = models.IntegerField()

    def __str__(self):
        return self.County + self.SubCounty + str(self.Year) + str(self.Month)

    class Meta:
        ordering = 'Year', 'County', 'SubCounty'


class Patients(models.Model):
    YEAR_CHOICES = []
    for r in range(2019, (datetime.datetime.now().year + 1)):
        YEAR_CHOICES.append((r, r))
    Year = models.IntegerField('year', choices=YEAR_CHOICES, default=datetime.datetime.now().year)
    MONTH_CHOICE = [(m, m) for m in range(1, 13)]
    Month = models.IntegerField(choices=MONTH_CHOICE, default=datetime.datetime.now().month)
    CountyChoices = (
        ('kisumu', 'Kisumu'),
        ('vihiga', 'Vihiga'),
        ('busia', 'Busia'),
    )
    County = models.CharField(max_length=30, choices=CountyChoices, default='Kisumu')
    subCounty_choices = (
        ('kisumu west', 'Kisumu West'),
        ('kisumu central', 'Kisumu Central'),
        ('kisumu east', 'Kisumu East'),
        ('seme', 'Seme'),
        ('muhoroni', 'Muhoroni'),
        ('nyando', 'Nyando'),
        ('nyakach', 'Nyakach'),
        ('sabatia', 'Sabatia,'),
        ('vihiga', 'vihiga'),
        ('luanda', 'Luanda'),
        ('emuhaya', 'Emuhaya'),
        ('hamisi', 'Hamisi'),
        ('teso north', 'Teso North'),
        ('teso south', 'Teso South'),
        ('nambale', 'Nambale'),
        ('matayos', 'Matayos'),
        ('butula', 'Butula'),
        ('samia', 'Samia'),
        ('bunyala', 'Bunyala'),
    )
    SubCounty = models.CharField(max_length=30, choices=subCounty_choices, default='muhoroni')
    PatientsReceived = models.IntegerField()
    PatientsNets = models.IntegerField()
    PatientswithoutNets = models.IntegerField()

    def __str__(self):
        return self.County + self.SubCounty + str(self.Year) + str(self.Month)

    class Meta:
        ordering = 'Year', 'County', 'SubCounty'
