from django.db import models
from school_app.models import School

# создали новое приложение Сотрудники в нем прописываем Классы
class Department(models.Model):
    name = models.CharField(max_length=250)
    description = models.TextField()
    school = models.ForeignKey(School, on_delete=models.CASCADE)

    def __str__(self):
        return self.name

class Position(models.Model):
    name = models.CharField(max_length=45)
    duration = models.DateField()
    is_active = models.BooleanField()
    description = models.TextField()
    department = models.ForeignKey(Department, on_delete=models.CASCADE)

    def __str__(self):
        return self.name


class Employee(models.Model):
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    date_of_birth = models.DateField()
    phone_number = models.CharField(max_length=255, null=True)
    email = models.EmailField(null=True, blank=True)
    M = 'Male'
    F = 'Female'
    GENDER = [
        (M, 'Male'),
        (F, 'Female')
    ]
    gender = models.CharField(max_length=6, choices=GENDER)
    salary = models.DecimalField(max_digits=9, decimal_places=2)
    position = models.ForeignKey(Position, on_delete=models.CASCADE)

    def __str__(self):
        return self.first_name

    def save(self, *args, **kwargs):  # функция save автоматически вызывается во время сохранения
        self.first_name = self.first_name.capitalize()  # первая заглавная остальные маленькие
        self.last_name = self.last_name.capitalize()
        super(Employee, self).save()


