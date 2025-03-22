# File Name: hourly_employee.py - CIS131
# Description: This file defines the HourlyEmployee class, a concrete subclass of Employee paid by the hour with overtime.
# Author: Dakota Kartchner
# Date Created: 3/18/2025

from salaried_employee import SalariedEmployee
from hourly_employee import HourlyEmployee
from employee import Employee

# try to make an Employee object (should fail because it's abstract)
try:
    test_emp = Employee("John", "Doe", "123-45-6789")
except TypeError as error:
    print("TypeError caught:", error)

# create a salaried and hourly employee
salaried = SalariedEmployee("John", "Doe", "111-22-3333", 1200)
hourly = HourlyEmployee("Jane", "Doe", "222-33-4444", 45, 20)

# print their details and earnings
print(salaried)
print("Earnings:", salaried.earnings())

print(hourly)
print("Earnings:", hourly.earnings())

# use a list to process both employees the same way (polymorphism)
employees = [salaried, hourly]

for emp in employees:
    print("\nProcessing:", emp)
    print("Earnings:", emp.earnings())