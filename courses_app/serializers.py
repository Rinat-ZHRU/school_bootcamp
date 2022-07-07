from rest_framework.validators import UniqueTogetherValidator
from courses_app.models import Course
from rest_framework import serializers


class CourseSerializer(serializers.ModelSerializer):
    class Meta:                      # класс мета
        model = Course
        fields = ['name', 'duration', 'price', 'is_active']

        # такое можно сделать если с фронта будет информация метод post
        # для админки нужно прописать это в модельках
        # validators = [
        #     UniqueTogetherValidator(            # валидация, для уникализации)
        #         queryset=Course.objects.all(),
        #         fields=['name', 'duration', 'price']
        #
        #     )
        # ]