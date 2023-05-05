from django.db import models
from django.urls import reverse


# Create your models here.

class Department(models.Model):
    name = models.CharField(max_length=100)
    description = models.CharField(max_length=300, null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name
    
    @classmethod
    def get_all_departments(cls):
        return cls.objects.all()

    @classmethod
    def get_department_by_id(cls, id):
        return cls.objects.get(id=id)
    
    def show_department_url(self):
        return reverse('show_department', args=[self.id])
    
    def update_department_url(self):
        return reverse('update_department', args=[self.id])
    
    def delete_department_url(self):
        return reverse('delete_department', args=[self.id])