from django.db import models

from employee.models import Employee


# Create your models here.

class Task(models.Model):
    PRIORITY_CHOICES = [
        ('important', 'Important'),
        ('normal', 'Normal'),
    ]

    parent_task = models.ForeignKey('self', on_delete=models.CASCADE, null=True, blank=True,
                                    related_name='dependencies')
    executor = models.ForeignKey(Employee, on_delete=models.CASCADE, null=True, blank=True)
    deadline = models.DateTimeField(null=True, blank=True)
    status = models.CharField(max_length=20, default='pending')
    priority = models.CharField(max_length=20, choices=PRIORITY_CHOICES, default='normal')
    title = models.CharField(max_length=255)

    def __str__(self):
        return self.title
