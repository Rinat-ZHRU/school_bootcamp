from employee_app.models import Department, Position, Employee
from rest_framework import serializers


class DepartmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Department
        fields = '__all__'  # все поля

class PositionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Position
        fields = '__all__'

class EmploeeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Employee
        fields = '__all__'