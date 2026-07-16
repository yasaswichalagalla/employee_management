from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import authenticate, login, logout
from .models import Employee, Department


# LOGIN
def login_view(request):

    if request.method == "POST":

        username = request.POST.get("username")
        password = request.POST.get("password")

        user = authenticate(
            request,
            username=username,
            password=password
        )

        if user:

            login(request, user)

            return redirect("dashboard")

        else:

            return render(
                request,
                "employees/login.html",
                {
                    "error": "Invalid username or password"
                }
            )


    return render(
        request,
        "employees/login.html"
    )



# DASHBOARD
def dashboard(request):

    employees = Employee.objects.all()

    return render(
        request,
        "employees/dashboard.html",
        {
            "employees": employees
        }
    )



# ADD EMPLOYEE
def add_employee(request):

    if request.method == "POST":


        employee = Employee.objects.create(

            emp_id=request.POST.get("emp_id"),

            name=request.POST.get("name"),

            phone=request.POST.get("phone"),

            email=request.POST.get("email"),

            salary=request.POST.get("salary"),

            date_of_join=request.POST.get("date_of_join")

        )


        Department.objects.create(

            employee=employee,

            department_name=request.POST.get("department_name"),

            subject=request.POST.get("subject")

        )


        return redirect("dashboard")


    return render(
        request,
        "employees/add_employee.html"
    )



# EDIT EMPLOYEE
def edit_employee(request, id):

    employee = get_object_or_404(
        Employee,
        id=id
    )


    department = Department.objects.filter(
        employee=employee
    ).first()



    if request.method == "POST":


        employee.emp_id = request.POST.get("emp_id")

        employee.name = request.POST.get("name")

        employee.phone = request.POST.get("phone")

        employee.email = request.POST.get("email")

        employee.salary = request.POST.get("salary")

        employee.date_of_join = request.POST.get("date_of_join")


        employee.save()



        if department:

            department.department_name = request.POST.get(
                "department_name"
            )

            department.subject = request.POST.get(
                "subject"
            )

            department.save()


        else:

            Department.objects.create(

                employee=employee,

                department_name=request.POST.get(
                    "department_name"
                ),

                subject=request.POST.get(
                    "subject"
                )

            )


        return redirect("dashboard")



    return render(
        request,
        "employees/edit_employee.html",
        {
            "employee": employee,
            "department": department
        }
    )



# DELETE EMPLOYEE
def delete_employee(request, id):

    employee = get_object_or_404(
        Employee,
        id=id
    )

    employee.delete()

    return redirect("dashboard")



# LOGOUT
def logout_view(request):

    logout(request)

    return redirect("login_view")