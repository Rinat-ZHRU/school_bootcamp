
from django.contrib import admin
from django.urls import path, include
#
urlpatterns = [
    path('admin/', admin.site.urls),
    path('courses/', include('courses_app.urls')),  # упорядочивание юрлэшек внутри главной
    path('students/', include('students_app.urls')),  # упорядочивание юрлэшек внутри главной
]
