from django.db import models

from Employee.models import Employee


# Create your models here.

class Task(models.Model):
    PRIORITY_CHOICES = [
        ('important', 'Important'),
        ('normal', 'Normal'),
    ]

    name = models.CharField(max_length=255)
    parent_task = models.ForeignKey('self', on_delete=models.CASCADE, null=True, blank=True,
                                    related_name='dependencies')
    executor = models.ForeignKey('Employee', on_delete=models.CASCADE, null=True, blank=True)  # Исправлено
    deadline = models.DateField()
    status = models.CharField(max_length=20, default='pending')
    priority = models.CharField(max_length=20, choices=PRIORITY_CHOICES, default='normal')

    def __str__(self):
        return self.name


class Employee(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    position = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"
