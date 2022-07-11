
from django.contrib import admin
from django.urls import path, include
#
urlpatterns = [                   # упорядочивание юрлэшек внутри главной
    path('admin/', admin.site.urls),
    path('courses/', include('courses_app.urls')),
    path('students/', include('students_app.urls')),
    path('employee/', include('employee_app.urls')),
    path('', include('auth_app.urls')),
]
