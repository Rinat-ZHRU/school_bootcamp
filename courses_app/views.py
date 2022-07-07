from courses_app.models import Course
from courses_app.serializers import CourseSerializer
from rest_framework import viewsets


class CourseViewSet(viewsets.ReadOnlyModelViewSet):  #  добавляем вьюшку для фронта, с возможностью только чтения
    # этот класс отдает на фронт информацию по курсам
    queryset = Course.objects.all()
    serializer_class = CourseSerializer


