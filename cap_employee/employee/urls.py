from django.urls import path
from cap_employee.employee.views import EmployeeView

app_name = "employee"

urlpatterns = [
    path('employee_hire', EmployeeView.as_view(), name='employees'),
]
