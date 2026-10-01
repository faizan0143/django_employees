from django.shortcuts import render, redirect, get_object_or_404
# from django.http import HttpResponse
# from django.urls import reverse
from .models import Employee
from .forms import EmployeeForm
from django.contrib import messages

# Create your views here.

def view_employee(request, id):
    employee = get_object_or_404(Employee, id=id)
    
    context = {
        'employee': employee
    }
    return render(request, 'view_employee.html', context)


def create_employee(request):
    if request.method == "POST":
        form = EmployeeForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, 'Employee created successfully!')
            return redirect('home')
        else:
            form = EmployeeForm()
            messages.error(request, 'Error creating employee. Please check the form for errors.')
            return render(request, 'create_employee.html', {'form': form})
    form = EmployeeForm()
    
    context = {
        'form' : form
    }
    return render(request, 'create_employee.html', context)


def edit_employee(request, id):
    employee = get_object_or_404(Employee, id=id)
    form = EmployeeForm(instance=employee)
    
    context = {
        'form' : form
    }
    
    return render(request, 'edit_employee.html', context)