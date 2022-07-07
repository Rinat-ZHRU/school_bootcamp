from students_app.models import Student
from students_app.serializers import StudentSerializer
from rest_framework import viewsets


class StudentViewSet(viewsets.ModelViewSet):  #  добавляем вьюшку для фронта, с возможностью только чтения
    # этот класс отдает на фронт информацию по студентам
    queryset = Student.objects.all()
    serializer_class = StudentSerializer
