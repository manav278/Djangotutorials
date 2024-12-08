from django.contrib import admin
from api.models import Company,Employee
# Register your models here.

class CompanyAdmin(admin.ModelAdmin):
    list_display=('company_name','company_location')
    search_fields=('company_name',)

class EmployeeAdmin(admin.ModelAdmin):
    list_display=('employee_name','employee_email','employee_address')
    list_filter=('company',)

admin.site.register(Company,CompanyAdmin)
admin.site.register(Employee,EmployeeAdmin)