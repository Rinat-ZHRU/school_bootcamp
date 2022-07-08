from django.db import models

class School(models.Model):
    name = models.CharField(max_length=200)
    location = models.CharField(max_length=250)
    phone_numbers = models.CharField(max_length=20)

    class Meta:
        ordering = ['name']  # очередность
        unique_together = (
            'name',
            'location',
            'phone_numbers',
        )

    def __str__(self):          #
        return self.name
