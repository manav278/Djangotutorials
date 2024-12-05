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
