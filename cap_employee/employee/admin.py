# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin

# Register your models here.
from cap_employee.employee.models import Employee, Title, Department, DeptEmp, Salaries

admin.site.register(Employee)
admin.site.register(Title)
admin.site.register(Department)
admin.site.register(DeptEmp)
admin.site.register(Salaries)
