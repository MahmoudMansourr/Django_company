from django.shortcuts import render
from django.http import HttpResponse
from .models import Employee
from .forms import EmployeeForm
from django.urls import reverse
from django.shortcuts import redirect






# Create your views here.

def helloworld(request):
    return HttpResponse('Hello World!')


def list_employees(request):
    employees = Employee.get_all_employees()
    return render(request, 'employees/list.html', context={'employees': employees})




def create_employee(request):
    form  = EmployeeForm()
    if request.method =='GET':
        return render(request, 'employees/create.html', context={"form":form})
    else:
        print(request.POST)
        ## upload image 000> request.FILES
        # print(request.FILES)
        ## use form object to save data
        form = EmployeeForm(request.POST)
        if form.is_valid():
            form.save()
        # return HttpResponse("POST request received")
        redirect_url = reverse('list_employees')
        return redirect(redirect_url)
    
def show_employee(request,id):
    employee = Employee.get_employee_by_id(id)
    return render(request, 'employees/show.html', context={"employee":employee})


def update_employee(request,id):
    employee = Employee.get_employee_by_id(id)
    if request.method =='GET':
            form = EmployeeForm(instance=employee)
            return render(request, 'employees/update.html', context={"form":form})
    else:
        print(request.POST)
        form = EmployeeForm(request.POST, instance=employee)
        if form.is_valid():
            form.save()
        redirect_url = reverse('list_employees')
        return redirect(redirect_url)
    
def delete_employee(request,id):
    employee= Employee.get_employee_by_id(id)
    employee.delete()
    redirect_url = reverse('list_employees')
    return redirect(redirect_url)