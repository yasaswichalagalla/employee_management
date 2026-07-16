from django.urls import path
from . import views


urlpatterns = [

    # Login
    path(
        'login/',
        views.login_view,
        name='login_view'
    ),


    # Dashboard
    path(
        'dashboard/',
        views.dashboard,
        name='dashboard'
    ),


    # Add Employee
    path(
        'add-employee/',
        views.add_employee,
        name='add_employee'
    ),


    # Edit Employee
    path(
        'edit/<int:id>/',
        views.edit_employee,
        name='edit_employee'
    ),


    # Delete Employee
    path(
        'delete/<int:id>/',
        views.delete_employee,
        name='delete_employee'
    ),


    # Logout
    path(
        'logout/',
        views.logout_view,
        name='logout'
    ),

]