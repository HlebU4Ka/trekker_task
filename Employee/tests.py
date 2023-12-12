from django.test import TestCase
from .models import Employee

class EmployeeModelTest(TestCase):

    def setUp(self):
        # Подготовка данных для тестов
        self.employee_data = {
            'first_name': 'John',
            'last_name': 'Doe',
            'position': 'Developer'
        }

    def test_employee_creation(self):
        # Тест создания сотрудника
        employee = Employee.objects.create(**self.employee_data)
        self.assertEqual(employee.full_name, 'John Doe')

    def test_employee_str_representation(self):
        # Тест строкового представления сотрудника
        employee = Employee.objects.create(**self.employee_data)
        self.assertEqual(str(employee), 'John Doe')

    def test_employee_search(self):
        # Тест метода поиска
        employee = Employee.objects.create(**self.employee_data)
        result = Employee.objects.search('John')
        self.assertEqual(result.first(), employee)

    def test_employee_update(self):
        # Тест обновления данных сотрудника
        employee = Employee.objects.create(**self.employee_data)
        employee.position = 'Senior Developer'
        employee.save()
        self.assertEqual(employee.position, 'Senior Developer')

    def test_employee_deletion(self):
        # Тест удаления сотрудника
        employee = Employee.objects.create(**self.employee_data)
        employee_id = employee.id
        employee.delete()
        with self.assertRaises(Employee.DoesNotExist):
            Employee.objects.get(id=employee_id)

    def test_employee_creation_without_position(self):
        employee_data_without_position = {
            'first_name': 'John',
            'last_name': 'Doe',
        }
        employee = Employee.objects.create(**employee_data_without_position)
        self.assertEqual(employee.position, '')