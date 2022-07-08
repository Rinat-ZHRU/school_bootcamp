from students_app.models import Student
from rest_framework import serializers


class StudentSerializer(serializers.ModelSerializer):
    class Meta:                      # класс мета
        model = Student
        fields = ['first_name', 'last_name', 'date_of_birth', 'phone_number', 'email', 'gender', 'course']
    # попытка вывести наименование курсов вместо id
    # def to_representation(self, instance):
    #     response = super().to_representation(instance)
    #     serializers_student = StudentSerializer(instance=instance.students)
    #     response["course"] = serializers_student.data
    #     return response

    # def to_representation(self, instance):
    #     response = super().to_representation(instance)
    #     serializers_school = SchoolSerializer(instance=instance.school)
    #     response["school"] = serializers_school.data
    #     return response
