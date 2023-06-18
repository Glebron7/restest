from django.db import models


class Employee(models.Model):
    team = models.CharField('Сотрудник', max_length=100)
    employee = models.TextField('Должность')

    def __ctr__(self):
        return self.team

    class Meta:
        verbose_name = 'Сотрудник'
        verbose_name_plural = 'Сотрудники'