from django_filters.rest_framework import DjangoFilterBackend

from school_app.models import School
from school_app.serializers import SchoolSerializer
from rest_framework import viewsets
from rest_framework.filters import SearchFilter, OrderingFilter

class CourseViewSet(viewsets.ModelViewSet):  #  добавляем вьюшку для фронта, с возможностью только чтения
    # этот класс отдает на фронт информацию по курсам
    queryset = School.objects.all()
    serializer_class = SchoolSerializer
