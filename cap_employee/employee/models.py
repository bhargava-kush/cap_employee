# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models


# Create your models here.

class Employee(models.Model):
    GENDER_CHOICES = (
        ('M', 'Male'),
        ('F', 'Female'),
    )

    emp_no = models.AutoField(primary_key=True)
    birth_date = models.DateField()
    first_name = models.CharField(max_length=14)
    last_name = models.CharField(max_length=16)
    gender = models.CharField(max_length=1, choices=GENDER_CHOICES)
    hire_date = models.DateField()

    def __unicode__(self):
        return self.emp_no

    def __str__(self):
        return self.emp_no

    class Meta:
        verbose_name_plural = "Employees"


class Department(models.Model):
    dept_no = models.CharField(max_length=4, primary_key=True)
    dept_name = models.CharField(max_length=4, unique=True)

    def __unicode__(self):
        return self.dept_name

    def __str__(self):
        return self.dept_name

    class Meta:
        verbose_name_plural = "Departments"


class DeptEmp(models.Model):
    emp_no = models.ForeignKey(Employee, on_delete=models.CASCADE)
    dept_no = models.ForeignKey(Department, on_delete=models.CASCADE)
    from_date = models.DateField()
    to_date = models.DateField()

    def __unicode__(self):
        return self.emp_no.first_name

    def __str__(self):
        return self.emp_no.first_name

    class Meta:
        unique_together = (("emp_no", "dept_no"),)


class Title(models.Model):
    emp_no = models.ForeignKey(Employee, on_delete=models.CASCADE)
    title = models.CharField(max_length=50)
    from_date = models.DateField()
    to_date = models.DateField(null=True, blank=True)

    def __unicode__(self):
        return self.title

    def __str__(self):
        return self.title

    class Meta:
        unique_together = (("emp_no", "title", "from_date"),)


class Salaries(models.Model):
    emp_no = models.ForeignKey(Employee, on_delete=models.CASCADE)
    salary = models.IntegerField()
    from_date = models.DateField()
    to_date = models.DateField()

    def __unicode__(self):
        return self.emp_no.first_name

    def __str__(self):
        return self.emp_no.first_name

    class Meta:
        unique_together = (("emp_no", "from_date"),)


