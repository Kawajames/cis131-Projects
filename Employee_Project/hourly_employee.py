# File Name: hourly_employee.py - CIS131
# Description: This file defines the HourlyEmployee class, a concrete subclass of Employee paid by the hour with overtime.
# Author: Dakota Kartchner
# Date Created: 3/17/2025

from employee import Employee

class HourlyEmployee(Employee):
    def __init__(self, first, last, ssn, hours, wage):
        super().__init__(first, last, ssn)
        self.hours = hours  # total hours worked
        self.wage = wage    # pay per hour

    @property
    def hours(self):
        return self._hours

    @hours.setter
    def hours(self, value):
        if not (0 <= value <= 168):
            raise ValueError("Hours must be between 0 and 168")
        self._hours = value

    @property
    def wage(self):
        return self._wage

    @wage.setter
    def wage(self, value):
        if value < 0:
            raise ValueError("Wage must be non-negative")
        self._wage = value

    def earnings(self):
        # regular pay for 40 or fewer hours, 1.5x pay for overtime
        if self.hours <= 40:
            return self.hours * self.wage
        else:
            overtime = self.hours - 40
            return 40 * self.wage + overtime * self.wage * 1.5

    def __repr__(self):
        return (f"HourlyEmployee: {super().__repr__()}, Hours Worked: {self.hours}, "
                f"Hourly Wage: ${self.wage:.2f}")