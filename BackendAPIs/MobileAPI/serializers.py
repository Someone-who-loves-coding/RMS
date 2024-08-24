from rest_framework import serializers
from .models import Employeetable,PeripheralRequest

class EmployeeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Employeetable
        fields = '__all__'  # Use '__all__' directly, not in a list

class PeripheralRequestSerializer(serializers.ModelSerializer):
    class Meta:
        model = PeripheralRequest
        fields = ['category', 'subject', 'reason', 'employee_id']
