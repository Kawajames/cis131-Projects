# File Name: project1Employees.py
# Description: This program reads employee data from a file and lets the user view
#              either full job info or contact info using a menu.
# Author: Dakota Kartchner
# Date Created: 4/2/2025

from abc import ABC, abstractmethod
from datetime import date
import sys

# Abstract Person class
class Person(ABC):
    @abstractmethod
    def __init__(self, firstName, lastName, idNumber, emailAddress, phoneNumber):
        self.firstName = firstName
        self.lastName = lastName
        if isinstance(idNumber, int) and 1000 <= idNumber <= 9999:
            self.idNumber = idNumber
        else:
            raise ValueError("ID must be a 4-digit integer")
        self.emailAddress = emailAddress
        if len(phoneNumber) <= 12:
            self.phoneNumber = phoneNumber
        else:
            raise ValueError("Phone number must be 12 characters or less")

    def __str__(self):
        return f"{self.lastName}, {self.firstName} (ID: {self.idNumber})"

    def __repr__(self):
        return f"Person({self.firstName!r}, {self.lastName!r}, {self.idNumber!r}, {self.emailAddress!r}, {self.phoneNumber!r})"

# Employee class that inherits from Person
class Employee(Person):
    roleDictionary = {"001": "Staff", "002": "Faculty"}
    classificationDictionary = {"001": "Full", "002": "Part"}

    def __init__(self, firstName, lastName, idNumber, emailAddress, phoneNumber,
                 hireDate, classificationValue, roleValue, annualSalary):
        super().__init__(firstName, lastName, idNumber, emailAddress, phoneNumber)
        self.hireDate = hireDate
        
        self.classificationPerson = self._get_key(Employee.classificationDictionary, classificationValue)
        if self.classificationPerson is None:
            raise ValueError("Invalid classification")
            
        self.rolePerson = self._get_key(Employee.roleDictionary, roleValue)
        if self.rolePerson is None:
            raise ValueError("Invalid role")
            
        if annualSalary < 0:
            raise ValueError("Salary cannot be negative")
        self.annualSalary = round(annualSalary, 2)

    @staticmethod
    def _get_key(dictionary, value):
        for key, val in dictionary.items():
            if val.lower() == value.lower():
                return key
        return None

    def __str__(self):
        d = self.hireDate
        return f"{self.lastName}, {self.firstName} (ID: {self.idNumber}) | {d.month}/{d.day}/{d.year} | " \
               f"{Employee.classificationDictionary.get(self.classificationPerson)} | " \
               f"{Employee.roleDictionary.get(self.rolePerson)} | Salary: {self.annualSalary:,.2f}"

    def __repr__(self):
        return (f"Employee({self.firstName!r}, {self.lastName!r}, {self.idNumber!r}, "
                f"{self.emailAddress!r}, {self.phoneNumber!r}, {self.hireDate!r}, "
                f"{self.classificationPerson!r}, {self.rolePerson!r}, {self.annualSalary!r})")

# List to hold Employee objects
employees = []

def getEmployees():
    print("\nAdding employees...\n")
    try:
        with open("employees.txt", "r") as file:
            lines = file.readlines()
    except FileNotFoundError:
        print("Error: 'employees.txt' file not found.")
        sys.exit(1)
        
    # Skip the header line
    for line in lines[1:]:
        parts = line.strip().split()
        if len(parts) < 9:
            continue
        try:
            lastName, firstName = parts[0], parts[1]
            idNumber = int(parts[2])
            emailAddress = parts[3]
            phoneNumber = parts[4]
            # Parse hireDate from M/D/YYYY format
            m, d, y = map(int, parts[5].split("/"))
            hireDateObj = date(y, m, d)
            classificationValue = parts[6]
            roleValue = parts[7]
            annualSalary = float(parts[8])
            emp = Employee(firstName, lastName, idNumber, emailAddress, phoneNumber,
                           hireDateObj, classificationValue, roleValue, annualSalary)
            employees.append(emp)
            print(f"Added employee {firstName} {lastName}...")
        except Exception as e:
            print(f"Skipping employee record due to error: {e}")

def displayEmployment():
    print("\nEmployee Employment Information\n")
    header = f"{'LastName':15}{'FirstName':15}{'ID':8}{'Email':30}{'Phone':15}" \
             f"{'HireDate':12}{'Classif':15}{'Role':10}{'Salary':10}"
    print(header)
    print("-" * len(header))
    for emp in employees:
        hd = f"{emp.hireDate.month}/{emp.hireDate.day}/{emp.hireDate.year}"
        classification = Employee.classificationDictionary.get(emp.classificationPerson, "N/A")
        role = Employee.roleDictionary.get(emp.rolePerson, "N/A")
        print(f"{emp.lastName:15}{emp.firstName:15}{emp.idNumber:<8}{emp.emailAddress:30}"
              f"{emp.phoneNumber:15}{hd:12}{classification:15}{role:10}{emp.annualSalary:10.2f}")

def displayContact():
    print("\nEmployee Contact Information\n")
    header = f"{'LastName':15}{'FirstName':15}{'ID':8}{'Email':30}{'Phone':15}"
    print(header)
    print("-" * len(header))
    for emp in employees:
        print(f"{emp.lastName:15}{emp.firstName:15}{emp.idNumber:<8}{emp.emailAddress:30}{emp.phoneNumber:15}")

def menu():
    while True:
        print("\n1. Quit")
        print("2. Display Employee Employment Information")
        print("3. Display Employee Contact Information")
        choice = input("\n> ").strip()
        if choice == "1":
            print("\nThank you for using the system. Exiting...")
            sys.exit(0)
        elif choice == "2":
            displayEmployment()
        elif choice == "3":
            displayContact()
        else:
            print(f"\nI am sorry, {choice} is not an option.\n")

def main():
    print("Starting application...\n")
    getEmployees()
    menu()

if __name__ == "__main__":
    main()
