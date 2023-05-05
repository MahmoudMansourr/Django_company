from django.contrib import admin
from django.urls import path
from django.urls import include
from departments.views import list_departments, create_department, update_department, \
show_department, delete_department




urlpatterns = [
    path('', list_departments, name='list_departments'),
    path('create/', create_department, name='create_department'),
    path('update/<int:id>/', update_department, name='update_department'),
    path('show/<int:id>/', show_department, name='show_department'),
    path('delete/<int:id>', delete_department, name="delete_department")
]
