from django.db import models


class Course(models.Model):
    name = models.CharField(max_length=255)  # наименование курсов
    duration = models.PositiveIntegerField()  # длительность курсов
    price = models.DecimalField(max_digits=8, decimal_places=2)  # количество цифр общее и после запятой
    is_active = models.BooleanField(default=True)

    class Meta:
        ordering = ['-name']  # очередность
        unique_together = (
            'name',
            'duration',
            'price',
        )

    def __str__(self):          #
        return self.name



