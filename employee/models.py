from django.db import models
from django.urls import reverse
from departments.models import Department


# Create your models here.


from django.db import models
from django.urls import reverse

class Employee(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.EmailField(null=True, blank=True)
    salary = models.DecimalField(max_digits=8, decimal_places=2, default=5000)
    hire_date = models.DateField(auto_now_add=True, null=True, blank=True)
    dept = models.ForeignKey(Department, null=True, blank=True,
                             on_delete=models.CASCADE, related_name='dept_employee')

    def __str__(self):
        return self.first_name + ' ' + self.last_name
    
    def get_full_name(self):
        return self.first_name + ' ' + self.last_name

    @classmethod
    def get_all_employees(cls):
        return cls.objects.all()


    @classmethod
    def get_employee_by_id(cls, id):
        return cls.objects.get(id=id)
    
    def delete_employee_url(self):
        return reverse('delete_employee', args=[self.id])

    def show_employee_url(self):
        return reverse('show_employee', args=[self.id])
    
    def update_employee_url(self):
        return reverse('update_employee', args=[self.id])
