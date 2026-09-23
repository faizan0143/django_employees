from django.contrib import admin
from .models import Department, Employee
# Register your models here.

class DepartmentAdmin(admin.ModelAdmin):
    list_display = ['name','location'] 
    search_fields = ['name']
    

class EmployeeAdmin(admin.ModelAdmin):
    list_display = ['id','full_name','email','designation','salary','joining_date','active','department','manager']
    
    list_filter = ['manager']   
    list_editable = ['active']
    list_display_links = ['full_name','email']
    search_fields = ['first_name','email']
    ordering = ['id']
    
    
    
    
admin.site.register(Department,DepartmentAdmin)
admin.site.register(Employee,EmployeeAdmin)
admin.site.site_header = "Employee Management System"
admin.site.site_title = "Employee Management"