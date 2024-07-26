from rest_framework import serializers
from django.contrib.auth.models import User
from .models import PatientRecord, Department

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id','username', 'first_name', 'last_name', 'email']

class DepartmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Department
        fields = ['id', 'name', 'diagnostics', 'location', 'specialization']

class PatientRecordSerializer(serializers.ModelSerializer):
    class Meta:
        model = PatientRecord
        fields = ['id', 'patient', 'created_date', 'diagnostics', 'observation', 'treatments', 'department', 'misc']