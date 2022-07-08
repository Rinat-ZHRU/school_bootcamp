from django.db import models

# создали новое приложение Сотрудники в нем прописываем Классы
class Department(models.Model):
    name = models.CharField(max_length=50)
    description = models.TextField()

class Position(models.Model):   # Должность
    name = models.CharField(max_length=50)
    duration = models.PositiveIntegerField()  # длительность
    is_active = models.BooleanField(default=True)
    description = models.TextField()
   # permition = models.CharField(max_length=50)
    department = models.ManyToManyField(Department, null=True, blank=True)   # связка с классом Department

class Employee(models.Model):

    GENDER_FEMALE = 'F'
    GENDER_MALE = 'M'

    GENDER_CHOICES = (
        (GENDER_FEMALE, 'Female'),
        (GENDER_MALE, 'Male'),
    )

    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    date_of_birth = models.DateField(null=True, blank=True)
    phone_number = models.CharField(max_length=20)
    email = models.EmailField()
    gender = models.CharField(max_length=1, choices=GENDER_CHOICES)
    position = models.ForeignKey(Position, null=True, blank=True)  # связка с классом Position
    salary = models.DecimalField(max_digits=8, decimal_places=2)



