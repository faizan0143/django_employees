from django import forms
from .models import Employee
from crispy_forms.helper import FormHelper

class EmployeeForm(forms.ModelForm):
    class Meta:
        model = Employee
        fields = '__all__'
        widgets = {
           'joining_date': forms.DateInput(attrs={'type': 'date'}),
        }