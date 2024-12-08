from django.db import models

# Company Model
class Company(models.Model):
    company_id=models.AutoField(primary_key=True)
    company_name=models.CharField(max_length=50)
    company_location=models.CharField(max_length=50)
    company_about=models.TextField()
    company_type=models.CharField(max_length=50,choices=(('IT','IT'),('Non IT','Non IT')))
    added_date=models.DateTimeField(auto_now=True)
    active=models.BooleanField(default=False)

    def __str__(self):
        return self.company_name + ","+ self.company_location

class Employee(models.Model):
    emp_id=models.AutoField(primary_key=True)
    employee_name=models.CharField(max_length=100)
    employee_email=models.CharField(max_length=50)
    employee_address=models.CharField(max_length=200)
    employee_phone=models.CharField(max_length=10)
    employee_about=models.TextField()
    employee_position=models.CharField(max_length=50,
                                       choices=(('Software Developer Engineer','SDE'),('Data Scientiest','DS'),('Project Manager','PM')))
    company=models.ForeignKey(Company,on_delete=models.CASCADE) 

    def __str__(self):
        return self.employee_name