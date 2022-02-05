from rest_framework import serializers
from LLINS_API.models import Patients, Net


class PatientSerializer(serializers.ModelSerializer):
    class Meta:
        model = Patients
        fields = ['Year', 'Month', 'County', 'SubCounty',
                  'PatientsReceived', 'PatientsNets', 'PatientswithoutNets']


class NetsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Net
        fields = ['Year', 'Month', 'County', 'SubCounty', 'netsProvided'
                  'netsIssued']
