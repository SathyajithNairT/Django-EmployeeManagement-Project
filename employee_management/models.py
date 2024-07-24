from django.db import models

# Create your models here.

class Employee(models.Model):
    name = models.CharField(max_length = 100)
    designation = models.CharField(max_length = 50)
    gender = models.CharField(max_length = 20)
    state = models.CharField(max_length = 50)
    nationality = models.CharField(max_length = 50)
    email = models.EmailField()

    def __str__(self):
        return self.name