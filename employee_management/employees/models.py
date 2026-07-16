from django.db import models



class Employee(models.Model):

    emp_id = models.CharField(
        max_length=20,
        unique=True,
        null=True,
        blank=True
    )


    name = models.CharField(
        max_length=100
    )


    phone = models.CharField(
        max_length=15
    )


    email = models.EmailField()


    salary = models.DecimalField(
        max_digits=10,
        decimal_places=2
    )


    date_of_join = models.DateField()



    def __str__(self):

        return self.name





class Department(models.Model):

    employee = models.ForeignKey(
        Employee,
        on_delete=models.CASCADE
    )


    department_name = models.CharField(
        max_length=100
    )


    subject = models.CharField(
        max_length=100
    )



    def __str__(self):

        return self.department_name