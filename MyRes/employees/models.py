from django.db import models


class Employee(models.Model):
    name = models.CharField('Имя', max_length=200)
    position = models.CharField('Должность', max_length=200)
    charge_level = models.IntegerField('Заряд', default=100)