from django.urls import path
from employee_app.views import EmployeeViewSet, DepartmentViewSet, PositionViewSet

# эта юрл внутри нашего приложения
urlpatterns = [
    path('department/', DepartmentViewSet.as_view({'get': 'list'}), name='department-list'),
    path('position/', PositionViewSet.as_view({'get': 'list'}), name='position-list'),
    path('', EmployeeViewSet.as_view({'get': 'list', 'post': 'create'}), name='employee-list'),

    path('<int:pk>/', EmployeeViewSet.as_view(      # прописали возможность удаления по id (pk)
        {
            'get': 'retrieve',            #  типы запросов
            'delete': 'destroy',
            'put': 'update'
        }
    ),
         name='employee-detail'),
    ]