from rest_framework import serializers
from LLINS_API.models import PatientsData, Nets


class PatientSerializer(serializers.ModelSerializer):
    class Meta:
        model = PatientsData
        fields = ['year', 'month', 'totalpatients',
                  'patientswithnets', 'patientswithoutnets']
