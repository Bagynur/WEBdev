from django.db import models

# Create your models here.

class Company(models.Model):
    name = models.CharField(max_length=30)
    description = models.TextField(default='')
    city = models.CharField(max_length=30)
    address = models.TextField(default='')

    def __str__(self):
        return '{}: {}'.format(self.id, self.name, self.description, self.city, self.address)

    def to_company_json(self):
        return {
            'id': self.id,
            'name': self.name,
            'description': self.description,
            'city': self.city,
            'address': self.address
        }


class Vacancy(models.Model):
    name = models.CharField(max_length=30)
    description = models.TextField(default='')
    salary = models.FloatField(max_length=30)
    company = models.ForeignKey(Company, on_delete=models.CASCADE, default=None)

    def __str__(self):
        return '{}: {}'.format(self.id, self.name, self.description, self.salary, self.company)

    def to_vacancy_json(self):
        return {
            'id': self.id,
            'name': self.name,
            'description': self.description,
            'salary': self.salary,
            'company': self.company
        }


