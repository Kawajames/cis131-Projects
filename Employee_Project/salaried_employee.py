# File Name: salaried_employee.py - CIS131
# Description: This file defines the SalariedEmployee class, a concrete subclass of Employee with a weekly salary.
# Author: Dakota Kartchner
# Date Created: 3/17/2025

from employee import Employee

class SalariedEmployee(Employee):
    def __init__(self, first, last, ssn, salary):
        super().__init__(first, last, ssn)
        self.salary = salary  # weekly salary

    @property
    def salary(self):
        return self._salary

    @salary.setter
    def salary(self, value):
        if value < 0:
            raise ValueError("Salary can't be negative")
        self._salary = value

    def earnings(self):
        return self.salary  # return the weekly salary

    def __repr__(self):
        return f"SalariedEmployee: {super().__repr__()}, Weekly Salary: ${self.salary:.2f}"