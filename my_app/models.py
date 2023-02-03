from django.db import models

# Create your models here.


class Student(models.Model):
    name  = models.CharField(max_length=250)
    email = models.EmailField(unique=True)
    age   = models.PositiveIntegerField()

    