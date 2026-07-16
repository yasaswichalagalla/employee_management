from django import forms
from .models import Employee, Department



class EmployeeForm(forms.ModelForm):

    class Meta:

        model = Employee

        fields = [
            'name',
            'phone',
            'email',
            'salary',
            'dob'
        ]

        widgets = {

            'dob': forms.DateInput(
                attrs={
                    'type':'date'
                }
            )
        }



class DepartmentForm(forms.ModelForm):

    class Meta:

        model = Department

        fields = [
            'department_name',
            'subject'
        ]