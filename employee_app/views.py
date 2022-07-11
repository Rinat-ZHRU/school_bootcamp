from django.shortcuts import render
from django_filters.rest_framework import DjangoFilterBackend

from employee_app.models import Department, Position, Employee
from employee_app.serializers import DepartmentSerializer, PositionSerializer, EmploeeSerializer
from rest_framework import viewsets
from rest_framework.filters import SearchFilter, OrderingFilter


'''    
CRUD
C = create
R = retrieve
U = update
d = destroy
'''
class DepartmentViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Department.objects.all().order_by('-id')  # вытащить из БД все объекты
    serializer_class = DepartmentSerializer

class PositionViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Position.objects.all().order_by('-id')   # вытащить из БД все объекты
    serializer_class = PositionSerializer

class EmployeeViewSet(viewsets.ModelViewSet):  #  добавляем вьюшку для фронта, с возможностью редактирования
    # этот класс отдает на фронт информацию по студентам
    queryset = Employee.objects.all().order_by('first_name')
    serializer_class = EmploeeSerializer
    # добавили фильтры
    filter_backends = [DjangoFilterBackend, SearchFilter, OrderingFilter]
    lookup_field = 'pk'   # есть по умолчанию поэтому не нужен
    search_fields = ['first_name', 'last_name']  # поисковой фильтр по фамилии и курсам
    ordering_fields = ['first_name', 'last_name']  # выборный фильтр по фамилии и курсам
    filterset_fields = ['position']  # деление по позициям (выборка)

