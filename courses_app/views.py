from django_filters.rest_framework import DjangoFilterBackend

from courses_app.models import Course
from courses_app.serializers import CourseSerializer
from rest_framework import viewsets
from rest_framework.filters import SearchFilter, OrderingFilter

class CourseViewSet(viewsets.ModelViewSet):  #  добавляем вьюшку для фронта, с возможностью только чтения
    # этот класс отдает на фронт информацию по курсам
    queryset = Course.objects.all()
    serializer_class = CourseSerializer
    # добавили фильтры
    filter_backends = [DjangoFilterBackend, SearchFilter, OrderingFilter]
    #filterset_fields = ['name', 'duration']
    search_fields = ['name', 'duration']     # поисковой фильтр по имени и сроку
    ordering_fields = ['name', 'price']     # выборный фильтр по имени и цене


