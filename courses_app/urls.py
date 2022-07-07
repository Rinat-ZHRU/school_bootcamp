from django.urls import path
from courses_app.views import CourseViewSet
# эта юрл внутри нашего приложения
urlpatterns = [
    path('', CourseViewSet.as_view({'get': 'list'}), name='course-list'),
    ]
