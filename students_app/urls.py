from django.urls import path
from students_app.views import StudentViewSet
# эта юрл внутри нашего приложения
urlpatterns = [
    path('', StudentViewSet.as_view({'get': 'list', 'post': 'create'}), name='student-list'),
    ]