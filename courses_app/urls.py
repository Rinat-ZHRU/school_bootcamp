from django.urls import path
from courses_app.views import CourseViewSet
# эта юрл внутри нашего приложения
urlpatterns = [
    path('', CourseViewSet.as_view({'get': 'list', 'post': 'create'}), name='course-list'),
    path('<int:pk>/', CourseViewSet.as_view(      # прописали возможность удаления по id (pk)
        {
            'get': 'retrieve',
            'delete': 'destroy',
            'put': 'update'
        }
        ),
         name='course-detail'),
    ]
