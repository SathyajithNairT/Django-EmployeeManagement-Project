from django.shortcuts import render, redirect, get_object_or_404
from .models import Employee

# Create your views here.

def registration(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        designation = request.POST.get('designation')
        gender = request.POST.get('gender')
        state = request.POST.get('state')
        nationality = request.POST.get('nationality')
        email = request.POST.get('email')

        employee = Employee(
            name = name,
            designation = designation,
            gender = gender,
            state = state,
            nationality = nationality,
            email = email
        )

        employee.save()
        return redirect('manage')

    return render(request, 'employee_management/registration.html')



def manage(request):
    employee_data = Employee.objects.all()

    return render(request, 'employee_management/manage.html', {'employee_data': employee_data})



def view(request, emp_id):
    data = get_object_or_404(Employee, id = emp_id)

    return render(request, 'employee_management/view.html', {'data': data})



def edit(request, emp_id):
    data = get_object_or_404(Employee, id = emp_id)

    if request.method == 'POST':
        data.name = request.POST.get('name')
        data.designation = request.POST.get('designation')
        data.gender = request.POST.get('gender')
        data.email = request.POST.get('email')
        data.state = request.POST.get('state')
        data.nationality = request.POST.get('nationality')

        data.save()
        return redirect('manage')

    return render(request, 'employee_management/edit.html', {'data': data})



def delete(request, emp_id):
    data = get_object_or_404(Employee, id = emp_id)
    data.delete()
    
    return redirect('manage')