from django.urls import path
from students_app.views import StudentViewSet
# эта юрл внутри нашего приложения
urlpatterns = [
    path('', StudentViewSet.as_view({'get': 'list', 'post': 'create'}), name='student-list'),
    path('<int:pk>/', StudentViewSet.as_view(      # прописали возможность удаления по id (pk)
        {
            'get': 'retrieve',
            'delete': 'destroy',
            'put': 'update',    # меняет всё
        }
        ),
         name='student-detail'),
    ]