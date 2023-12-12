from django.db import models


class EmployeeManager(models.Manager):
    def search(self, query):
        return self.filter(models.Q(first_name__icontains=query) | models.Q(last_name__icontains=query))

class Employee(models.Model):
    """
    Модель представляет сотрудника.

    Attributes:
        first_name (str): Имя сотрудника.
        last_name (str): Фамилия сотрудника.
        position (str): Должность сотрудника.
    """

    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    position = models.CharField(max_length=100)

    objects = EmployeeManager()

    def save(self, *args, **kwargs):
        self.full_name = f"{self.first_name} {self.last_name}"
        super().save(*args, **kwargs)

    @property
    def full_name(self):
        """
        Возвращает полное имя сотрудника.

        Returns:
            str: Полное имя сотрудника в формате "Имя Фамилия".
        """
        return f"{self.first_name} {self.last_name}"

    @full_name.setter
    def full_name(self, value):
        """
        Устанавливает полное имя сотрудника.

        Args:
            value (str): Полное имя сотрудника в формате "Имя Фамилия".
        """
        first_name, last_name = value.split(' ', 1)
        self.first_name = first_name
        self.last_name = last_name

    def __str__(self):
        """
        Возвращает строковое представление сотрудника.

        Returns:
            str: Строковое представление сотрудника в формате "Имя Фамилия".
        """
        return f"{self.first_name} {self.last_name}"
