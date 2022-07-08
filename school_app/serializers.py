from school_app.models import School
from rest_framework import serializers


class SchoolSerializer(serializers.ModelSerializer):
    class Meta:                      # класс мета
        model = School
        fields = ['name', 'location', 'phone_numbers']