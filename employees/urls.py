from django.urls import path
from . import views

urlpatterns = [
    path('<int:id>/', views.view_employee, name='view_employee'),
    path('create/', views.create_employee, name='create_employee'),
    path('edit/<int:id>/', views.edit_employee, name='edit_employee'),
    path('delete/<int:id>/', views.delete_employee, name='delete_employee'),
]