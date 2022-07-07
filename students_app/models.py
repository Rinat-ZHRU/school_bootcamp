from django.db import models
from courses_app.models import Course


class Student(models.Model):
    GENDER_FEMALE = 'Female'
    GENDER_MALE = 'Male'

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
    course = models.ForeignKey(Course,                               # связка 1 ко многим
                                 on_delete = models.CASCADE,
                                 null=True, blank=True)

    class Meta:
        ordering = ['first_name']  # очередность
        unique_together = (
            'first_name',
            'last_name',
            'date_of_birth',
            'phone_number',
            'email',
            'gender',
            'course',
        )

    # функция для  изменения регистра в имени и фамилии
    def save(self, *args, **kwargs):
        for field_name in ['first_name', 'last_name']:
            val = getattr(self, field_name, False) # ищет атрибут объекта
            if val:
                setattr(self, field_name, val.capitalize())  # меняем первую букву на заглавную
        super(Student, self).save(*args, **kwargs)

    # def __str__(self):          #
    #     return self.first_name

    # второй способ (намного проще, но работает дольше)))
    # def save(self, *args, **kwargs):  # функция save автоматически вызывается во время сохранения
    #     self.first_name = self.first_name.capitalize()  # первая заглавная остальные маленькие
    #     self.last_name = self.last_name.capitalize()
    #     super(Student, self).save()