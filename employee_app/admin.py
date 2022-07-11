from django.contrib import admin
from employee_app.models import Department, Position, Employee

admin.site.register(Employee)  # зарегили для вывода в админке
admin.site.register(Department)
admin.site.register(Position)