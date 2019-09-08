from rest_framework import serializers

from cap_employee.employee.models import Employee, Title, Department, DeptEmp, Salaries
from cap_employee.employee.utils import calculate_age

class EmployeeSerializer(serializers.ModelSerializer):

    class Meta:
        model = Employee
        fields = '__all__'

    def validate(self, data):
        dob = data.get('Birth_date')
        age = calculate_age(dob)
        if age < 18 or age > 60:
            raise serializers.ValidationError("Invalid age")

        hire_date = data.get('hire_date')
        if hire_date.year < 2015:
            raise serializers.ValidationError("Invalid hire date")

    def create(self, validated_data):
        employee_obj = Employee.objects.create(emp_no=validated_data.get('emp_no'), birth_date=validated_data.get('birth_date'),
                                           first_name=validated_data.get('first_name'), last_name=validated_data.get('last_name'),
                                           gender=validated_data.get('gender'), hire_date=validated_data.get('hire_date'))

        return employee_obj


