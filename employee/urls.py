from django.contrib import admin
from django.urls import path
from employee.views import helloworld, list_employees, create_employee, update_employee, show_employee,\
delete_employee





urlpatterns = [
    path('hello', helloworld),
    path('', list_employees, name="list_employees"),
    path('create', create_employee, name="create_employee"),
    path('<int:id>/update', update_employee, name='update_employee'),
    path('<int:id>/show', show_employee, name='show_employee'),
    path('<int:id>/delete', delete_employee, name='delete_employee'),
]
