from django.urls import path
from school_app.views import SchoolViewSet
# эта юрл внутри нашего приложения
urlpatterns = [
    path('', SchoolViewSet.as_view({'get': 'list', 'post': 'create'}), name='course-list'),
    # path('<int:pk>/', SchoolViewSet.as_view(      # прописали возможность удаления по id (pk)
    #     {
    #         'get': 'retrieve',
    #         'delete': 'destroy',
    #         'put': 'update'
    #     }
    #     ),
    #      name='course-detail'),
    ]