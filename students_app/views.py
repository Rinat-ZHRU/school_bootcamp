from django_filters.rest_framework import DjangoFilterBackend

from students_app.models import Student
from students_app.serializers import StudentSerializer
from rest_framework import viewsets
from rest_framework.filters import SearchFilter, OrderingFilter


class StudentViewSet(viewsets.ModelViewSet):  #  добавляем вьюшку для фронта, с возможностью редактирования
    # этот класс отдает на фронт информацию по студентам
    queryset = Student.objects.all()
    serializer_class = StudentSerializer
    # добавили фильтры
    filter_backends = [DjangoFilterBackend, SearchFilter, OrderingFilter]
    search_fields = ['last_name', 'course']  # поисковой фильтр по фамилии и курсам
    ordering_fields = ['last_name', 'course']  # выборный фильтр по фамилии и курсам

