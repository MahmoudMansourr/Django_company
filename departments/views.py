from django.shortcuts import render
from django.http import HttpResponse 
from django.urls import reverse
from departments.models import Department
from .forms import DepartmentForm
from django.shortcuts import redirect


# Create your views here.

def helloworld(request):
    return HttpResponse('Hello World')



def list_departments(request):
    departments = Department.get_all_departments()
    return render(request, 'departments/list.html', context={'departments': departments})


def create_department(request):
    form = DepartmentForm()
    if request.method =='GET':
        return render(request, 'departments/create.html', context={"form":form})
    else:
        form = DepartmentForm(request.POST)
        if form.is_valid():
            form.save()
        redirect_url = reverse('list_departments')
        return redirect(redirect_url)


def update_department(request,id):
    department = Department.get_department_by_id(id)
    form = DepartmentForm(instance=department)
    if request.method =='GET':
        return render(request, 'departments/update.html', context={"form":form})
    else:
        form = DepartmentForm(request.POST, instance=department)
        if form.is_valid():
            form.save() 
        redirect_url = reverse('list_departments')
        return redirect(redirect_url)


def show_department(request, id):
    department = Department.get_department_by_id(id)
    return render(request, 'departments/show.html', context={"department":department})


def delete_department(request, id):
    department = Department.get_department_by_id(id)
    department.delete()
    redirect_url= reverse('list_departments')
    return redirect(redirect_url)